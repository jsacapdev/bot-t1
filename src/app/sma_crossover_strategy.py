# sma_crossover_strategy.py
import pandas as pd
from feature_engineering import calculate_sma

def predict_action_sma_crossover(df, fast_sma_period, slow_sma_period):
    if len(df) < max(fast_sma_period, slow_sma_period) + 1:
        return 0  # Not enough data to check for crossover

    fast_sma = calculate_sma(df, fast_sma_period).iloc[-1]
    slow_sma = calculate_sma(df, slow_sma_period).iloc[-1]

    previous_fast_sma = calculate_sma(df, fast_sma_period).iloc[-2]
    previous_slow_sma = calculate_sma(df, slow_sma_period).iloc[-2]

    if previous_fast_sma is not None and previous_slow_sma is not None:
        if previous_fast_sma <= previous_slow_sma and fast_sma > slow_sma:
            return 1  # BUY
        elif previous_fast_sma >= previous_slow_sma and fast_sma < slow_sma:
            return -1  # SELL
    return 0  # HOLD