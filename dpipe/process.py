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
def ToDatetime(df, *args, **kwargs):
    for column in args:
        df[column] = pd.to_datetime(df[column], **kwargs)
    return df


@Pipeable
def Drop(df, *args, axis=1, **kwargs):
    """
    Implements `df.DataFrame.drop()`.

    I have never once in my life dropped a row by index. Therefore I set the default to dropping columns.
    """
    return df.drop(*args, axis=axis, **kwargs)


@Pipeable
def GroupBy(df, column, **kwargs):
    gb = df.groupby(column, **kwargs)
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

