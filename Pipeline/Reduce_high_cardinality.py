from sklearn.base import BaseEstimator, TransformerMixin

class ReduceHighCardinality(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_reduce):
        self.columns_to_reduce = [col for col in columns_to_reduce if col != 'Id']  # Exclude 'Id'

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for col in self.columns_to_reduce:
            if col in X.columns:
                top_values = X[col].value_counts().index[:3].tolist()  # Get top 3 frequent values
                X[col] = X[col].apply(lambda x: x if x in top_values else "Others")
        return X