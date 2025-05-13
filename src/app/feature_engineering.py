# feature_engineering.py
import pandas as pd
import numpy as np
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def calculate_sma(df, period):
    return df["close"].rolling(window=period).mean()


def engineer_features(df, fast_sma_period, slow_sma_period):
    df["fast_sma"] = calculate_sma(df, fast_sma_period)
    df["slow_sma"] = calculate_sma(df, slow_sma_period)
    df["sma_above"] = np.where(df["fast_sma"] > df["slow_sma"], 1, 0)
    df = df.dropna()
    return df[
        ["open", "high", "low", "close", "volume", "fast_sma", "slow_sma", "sma_above"]
    ]


def create_target(df, future_periods):
    df["future_close"] = df["close"].shift(-future_periods)
    df["target"] = np.where(
        df["future_close"] > df["close"],
        1,
        np.where(df["future_close"] < df["close"], -1, 0),
    )
    df = df.dropna()
    return df["target"]
