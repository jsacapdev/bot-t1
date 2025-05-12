# exchange_connector.py
import ccxt
import pandas as pd


class ExchangeConnector:
    def __init__(self, exchange_id):
        self.exchange_id = exchange_id
        self.exchange = self._initialize_exchange()

    def _initialize_exchange(self):
        try:
            exchange = getattr(ccxt, self.exchange_id)()
            return exchange
        except AttributeError:
            raise ValueError(f"Error: Exchange '{self.exchange_id}' not found.")

    def fetch_historical_data(self, symbol, timeframe, limit):
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            df = pd.DataFrame(
                ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"]
            )
            df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
            df = df.set_index("datetime")
            return df
        except ccxt.NetworkError as e:
            print(f"Network error fetching data: {e}")
            return None
        except ccxt.ExchangeError as e:
            print(f"Exchange error fetching data: {e}")
            return None
