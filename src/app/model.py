# model.py
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TradingModel:
    def __init__(self, test_size, random_state):
        self.scaler = MinMaxScaler()
        self.model = LogisticRegression()
        self.test_size = test_size
        self.random_state = random_state
        self.model_trained = False
        self.logger = logging.getLogger(__name__)

    def train(self, features_df, target_series):
        scaled_features = self.scaler.fit_transform(features_df)
        X_train, X_test, y_train, y_test = train_test_split(scaled_features, target_series, test_size=self.test_size, random_state=self.random_state, shuffle=False)
        self.model.fit(X_train, y_train)
        self.model_trained = True
        self.logger.info("Model trained.")

    def predict(self, features_df):
        if not self.model_trained or features_df.empty:
            return 0
        scaled_features = self.scaler.transform(features_df)
        prediction = self.model.predict(scaled_features)
        return prediction[0]
