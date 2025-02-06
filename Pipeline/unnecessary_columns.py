from sklearn.base import BaseEstimator, TransformerMixin

class RemoveUnnecessaryColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_remove=['Date', 'Usage']):
        self.columns_to_remove = columns_to_remove

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(columns=self.columns_to_remove, axis = 1)
