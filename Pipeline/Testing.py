import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from missing_values import Droppingmissingvalues
from Extract_date import ExtractDateFromTimestamp
from Test_samples import SampleDataset
from unnecessary_columns import RemoveUnnecessaryColumns
from Reduce_high_cardinality import ReduceHighCardinality
from label_encoding import LabelEncodingTransformer

class Testing_Data:
    def __init__(self,n_samples=1500000):
        # Define columns to reduce high cardinality
        self.columns_to_reduce = [
            "OrgId", "IncidentId", "AlertId", "DetectorId", "AlertTitle", "DeviceId", "Sha256", "IpAddress", "Url", "AccountSid",
            "AccountUpn", "AccountObjectId", "AccountName", "DeviceName", "NetworkMessageId", "RegistryKey", "RegistryValueName",
            "RegistryValueData", "ApplicationId", "ApplicationName", "OAuthApplicationId", "FileName", "FolderPath", "ResourceIdName",
            "OSVersion", "CountryCode", "State", "City", "Category", "EntityType"
        ]

        # Create the pipeline
        self.pipeline = Pipeline([
            ("drop_missing", Droppingmissingvalues(threshold=0.5)),
            ("extract_date", ExtractDateFromTimestamp()),
            ("sample_data", SampleDataset(n_samples=n_samples)),
            ("remove_columns", RemoveUnnecessaryColumns(columns_to_remove=['Date', 'Usage'])),
            ("reduce_cardinality", ReduceHighCardinality(columns_to_reduce=self.columns_to_reduce)),
            ("label_encoding", LabelEncodingTransformer())
        ])

    def fit(self, X, y=None):
        """Fit the pipeline to the data."""
        self.pipeline.fit(X, y)
        return self

    def transform(self, X):
        """Transform the data using the fitted pipeline."""
        return self.pipeline.transform(X)

    def fit_transform(self, X, y=None):
        """Fit and transform the data."""
        return self.pipeline.fit_transform(X, y)