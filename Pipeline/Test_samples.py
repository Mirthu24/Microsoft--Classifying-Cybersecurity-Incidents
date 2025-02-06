from sklearn.base import BaseEstimator, TransformerMixin

class SampleDataset(BaseEstimator, TransformerMixin):
    def __init__(self, n_samples=1500000):
        self.n_samples = n_samples

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.sample(n=self.n_samples, random_state=42)