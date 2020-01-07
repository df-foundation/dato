"""
Matplotlib plotting functions.
"""

from sklearn.model_selection import train_test_split
from ..base import Pipeable


@Pipeable
def SpecifyLabel(df, Y_column, *args, **kwargs):
    """The label for
    """
    X_columns = [col for col in df.columns if col!=Y_column]
    return df[X_columns + [Y_column]]


@Pipeable
def TrainTestSplit(*args, **kwargs):
    return train_test_split(*args, **kwargs)

