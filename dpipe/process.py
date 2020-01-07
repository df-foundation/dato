"""
Matplotlib plotting functions.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .base import Pipeable, unpack_input
from .style import mpl_style, mpl_style_decorator
from .utils import series_is_date

plot_style = {
    'marker': 'o',
    'linestyle': '--',
}


@Pipeable
def Drop(df, *args, axis=1, **kwargs):
    """
    Implements `pd.DataFrame.drop()`.

    I have never once in my life dropped a row by index. Therefore I set the default to dropping columns.

    :param *args:
        Any args accepted by `pd.DataFrame.drop`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.drop()`.

    """
    return df.drop(*args, axis=axis, **kwargs)


@Pipeable
def DropNA(df, *args, **kwargs):
    """
    Implements `pd.DataFrame.dropna()`.

    :param *args:
        Any args accepted by `pd.DataFrame.dropna`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.dropna()`.

    """
    return df.dropna(*args, **kwargs)



@Pipeable
def FillNA(df, value=None, columns=None, **kwargs):
    """
    Implements `pd.DataFrame.fillna()`. If a scalar value is passed it is used to fill all missing values. Alternatively, an array-like 'value' can be given. It's expected that the array-like have the same length as 'self'.

    :param value: the value used to fill
    :type value: scalar, array-like
    :param columns: columns to apply fillna to
    :type columns: array-like
    :param **kwargs:
        Anything accepted by the `pd.DataFrame.fillna()` method.

    """
    df1 = df.copy()
    if columns is not None:
        for column in columns:
            df1[column] = df1[column].fillna(value=value, **kwargs)
    else:
        df1 = df1.fillna(value=value, **kwargs)
    return df1


@Pipeable
def GroupBy(df, *args, **kwargs):
    """
    Implements `pd.DataFrame.groupby()`.

    :param *args:
        Any args accepted by `pd.DataFrame.groupby()`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.groupby()`.


    """
    gb = df.groupby(*args, **kwargs)
    return gb


@Pipeable
def Mean(gb, column=None, **kwargs):
    if column is not None:
        grouped_mean = gb.mean(**kwargs)[column]
    else:
        grouped_mean = gb.mean(**kwargs)
    return grouped_mean


@unpack_input
@Pipeable
def Merge(*args, unpack_input=True, **kwargs):
    merged = pd.merge(*args, **kwargs)
    return merged


@Pipeable
def Sample(df, **kwargs):
    return df.sample(**kwargs)


@Pipeable
def Select(df, *args):
    return df[list(args)]


@Pipeable
def Sum(gb, column=None, **kwargs):
    if column is not None:
        grouped_sum = gb.sum(**kwargs)[column]
    else:
        grouped_sum = gb.sum(**kwargs)
    return grouped_sum


@Pipeable
def ToDatetime(df, *args, **kwargs):
    if not args:
        df = pd.to_datetime(df)
    else:
        for column in args:
            df[column] = pd.to_datetime(df[column], **kwargs)
    return df

