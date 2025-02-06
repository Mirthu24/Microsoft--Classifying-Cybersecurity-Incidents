from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder

class LabelEncodingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoders = {}

    def fit(self, X, y=None):
        for col in X.columns:
            if col != 'Id':
                le = LabelEncoder()
                le.fit(X[col].astype(str))
                self.encoders[col] = le
        return self

    def transform(self, X):
        X = X.copy()
        for col, le in self.encoders.items():
            if col in X.columns:
                X[col] = le.transform(X[col].astype(str))
        return X