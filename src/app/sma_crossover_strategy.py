# sma_crossover_strategy.py
import pandas as pd
from feature_engineering import calculate_sma
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def predict_action_sma_crossover(df, fast_sma_period, slow_sma_period):
    logger = logging.getLogger(__name__)
    if len(df) < max(fast_sma_period, slow_sma_period) + 1:
        logger.info("Not enough data to check for SMA crossover.")
        return 0  # Not enough data to check for crossover

    fast_sma = calculate_sma(df, fast_sma_period).iloc[-1]
    slow_sma = calculate_sma(df, slow_sma_period).iloc[-1]

    previous_fast_sma = calculate_sma(df, fast_sma_period).iloc[-2]
    previous_slow_sma = calculate_sma(df, slow_sma_period).iloc[-2]

    if previous_fast_sma is not None and previous_slow_sma is not None:
        if previous_fast_sma <= previous_slow_sma and fast_sma > slow_sma:
            logger.info("SMA Crossover: BUY signal.")
            return 1  # BUY
        elif previous_fast_sma >= previous_slow_sma and fast_sma < slow_sma:
            logger.info("SMA Crossover: SELL signal.")
            return -1  # SELL
    logger.info("SMA Crossover: HOLD signal.")
    return 0  # HOLD