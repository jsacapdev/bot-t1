# main.py
import time
from datetime import datetime
from config import config
from exchange_connector import ExchangeConnector
from feature_engineering import engineer_features, create_target
from model import TradingModel
from sma_crossover_strategy import predict_action_sma_crossover
from binance_trading_executor import BinanceTradingExecutor  # Updated import
import pandas as pd


def main():
    exchange_connector = ExchangeConnector(config["exchange"])
    bot_config = config
    binance_trading_executor = BinanceTradingExecutor(
        bot_config["symbol"]
    )  # Updated instantiation

    historical_data = exchange_connector.fetch_historical_data(
        bot_config["symbol"], bot_config["timeframe"], bot_config["limit"]
    )

    if historical_data is not None:
        features_df = engineer_features(
            historical_data.copy(),
            bot_config["fast_sma_period"],
            bot_config["slow_sma_period"],
        )
        target_series = create_target(
            historical_data.copy(), bot_config["future_periods"]
        )

        # Align features and target
        merged_df = pd.merge(
            features_df, target_series, left_index=True, right_index=True, how="inner"
        ).dropna()
        if not merged_df.empty:
            model = TradingModel(bot_config["test_size"], bot_config["random_state"])
            model.train(
                merged_df[
                    [
                        "open",
                        "high",
                        "low",
                        "close",
                        "volume",
                        "fast_sma",
                        "slow_sma",
                        "sma_above",
                    ]
                ],
                merged_df["target"],
            )

            while True:
                print(
                    f"\n--- {datetime.now(tz=None).strftime('%Y-%m-%d %H:%M:%S')} ---"
                )
                latest_data = exchange_connector.fetch_historical_data(
                    bot_config["symbol"], bot_config["timeframe"], bot_config["limit"]
                )

                if latest_data is not None and not latest_data.empty:
                    if len(latest_data) >= bot_config["slow_sma_period"] + 1:
                        latest_features = engineer_features(
                            latest_data.copy().tail(
                                max(
                                    bot_config["fast_sma_period"],
                                    bot_config["slow_sma_period"],
                                )
                            ),
                            bot_config["fast_sma_period"],
                            bot_config["slow_sma_period"],
                        )

                        ml_prediction = 0
                        if not latest_features.empty and model.model_trained:
                            ml_prediction = model.predict(latest_features.tail(1))
                            print(
                                f"ML Prediction: {'BUY' if ml_prediction == 1 else 'SELL' if ml_prediction == -1 else 'HOLD'}"
                            )
                            if ml_prediction == 1:
                                binance_trading_executor.buy()  # Updated reference
                            elif ml_prediction == -1:
                                binance_trading_executor.sell()  # Updated reference
                            else:
                                binance_trading_executor.hold()  # Updated reference
                        else:
                            print(
                                "ML Prediction: Model not trained or not enough data for features."
                            )
                            binance_trading_executor.hold()  # Updated reference

                        sma_prediction = predict_action_sma_crossover(
                            latest_data.copy(),
                            bot_config["fast_sma_period"],
                            bot_config["slow_sma_period"],
                        )
                        print(
                            f"SMA Crossover Signal: {'BUY' if sma_prediction == 1 else 'SELL' if sma_prediction == -1 else 'HOLD'}"
                        )

                    else:
                        print(
                            f"Waiting for {bot_config['slow_sma_period'] + 1} data points."
                        )
                        binance_trading_executor.hold()  # Updated reference
                else:
                    print("Failed to fetch latest data.")
                    binance_trading_executor.hold()  # Updated reference

                time.sleep(60)
        else:
            print("Not enough aligned data for training.")
    else:
        print("Failed to fetch initial historical data.")


if __name__ == "__main__":
    main()
