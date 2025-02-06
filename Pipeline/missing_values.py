import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class Droppingmissingvalues(BaseEstimator, TransformerMixin):
    def __init__(self, threshold = 0.5):
        self.threshold = threshold
        
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        missing_percentage = X.isnull().mean()
        drop_columns = missing_percentage[missing_percentage>self.threshold].index
        return X.drop(columns = drop_columns,axis=1)
        