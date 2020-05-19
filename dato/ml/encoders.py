from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import numpy as np
import sklearn as skl

from pipey import Pipeable, use_first_arg_only
from .preprocessing import TrainTestSplit
from .base import _ModelSpec


@Pipeable
def LabelEnc(m, columns):
    """Label encoder.

    :param df: Dataframe to be encoded
    :type df: pandas.DataFrame
    :param columns: list of columns to be encoded
    :type columns: array-like
    """
    encoded_df, enc_dict = m.encode(skl.preprocessing.LabelEncoder, columns)

    return m

