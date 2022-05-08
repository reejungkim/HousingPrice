

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, feature_names):
        self.feature_names = feature_names

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X.loc[:, self.feature_names].copy(deep=True)


def num_pipeline:
    Pipeline(steps=[
        ("num_selector", FeatureSelector(num_x_training)),
        ("imputer", SimpleImputer(strategy="median")),
        ("std_scaler", StandardScaler())
    ])


# Defining the steps in the categorical pipeline
def cat_pipeline:
    Pipeline([
        ('cat_selector', FeatureSelector(cat_x_training)),
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('one_hot_encoder', OneHotEncoder(sparse=False, handle_unknown='ignore'))
    ])
