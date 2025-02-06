import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class ExtractDateFromTimestamp(BaseEstimator, TransformerMixin):
    def __init__(self, date_format='%d-%m-%Y'):
        self.date_format = date_format

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        if 'Timestamp' in X.columns:
            X['Timestamp'] = pd.to_datetime(X['Timestamp'])
            X['Date'] = X['Timestamp'].dt.strftime(self.date_format)
            X = X.drop(columns=['Timestamp'], axis = 1)
        return X