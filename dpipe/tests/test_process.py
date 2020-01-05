import pytest
import pandas as pd

from .fixtures import mock_data_a, mock_data_b, mock_user_data
from dpipe.base import Pipeable
from dpipe.process import Drop, GroupBy, Mean, Merge, Sample, Select, Sum

import dpipe


def test_Drop(mock_data_a: pd.DataFrame):
    # GIVEN
    dropped = mock_data_a >> Drop('b')

    # THEN
    assert len(dropped.columns) == 1
    assert set(dropped.columns) == {'id'}


def test_Groupby_type(mock_user_data: pd.DataFrame):
    # WHEN
    gb = mock_user_data >> GroupBy('state_name')

    # THEN
    assert type(gb) == pd.core.groupby.generic.DataFrameGroupBy


def test_Mean_type_DataFrame(mock_user_data: pd.DataFrame):
    # WHEN
    df = mock_user_data >> GroupBy('state_name') >> Mean()

    # THEN
    assert type(df) == pd.core.frame.DataFrame


def test_Mean_type_Series(mock_user_data: pd.DataFrame):
    # WHEN
    series = mock_user_data >> GroupBy('state_name') >> Mean('population')

    # THEN
    assert type(series) == pd.core.series.Series


def test_Merge(mock_data_a: pd.DataFrame, mock_data_b: pd.DataFrame):
    # GIVEN
    merged = (mock_data_a, mock_data_b) >> Merge(on='id')

    # THEN
    assert len(merged) == 3
    assert set(merged.columns) == {'id', 'b', 'c'}


def test_Mean_value(mock_user_data: pd.DataFrame):
    # WHEN
    series = mock_user_data >> GroupBy('state_name') >> Mean('population')

    # THEN
    assert round(series.California) == 45187


def test_Sample_type(mock_user_data: pd.DataFrame):
    # WHEN
    sampled_df = mock_user_data >> Sample()

    # THEN
    assert sampled_df.shape == (1, 17)


def test_Select(mock_user_data: pd.DataFrame):
    # WHEN
    columns_to_select = ['state_name']
    subset = mock_user_data >> Select(*columns_to_select)

    # THEN
    assert set(subset.columns) == set(columns_to_select)


def test_Sum_type_DataFrame(mock_user_data: pd.DataFrame):
    # WHEN
    df = mock_user_data >> GroupBy('state_name') >> Sum()

    # THEN
    assert type(df) == pd.core.frame.DataFrame


def test_Sum_type_Series(mock_user_data: pd.DataFrame):
    # WHEN
    series = mock_user_data >> GroupBy('state_name') >> Sum('population')

    # THEN
    assert type(series) == pd.core.series.Series


def test_Sum_value(mock_user_data: pd.DataFrame):
    # WHEN
    series = mock_user_data >> GroupBy('state_name') >> Sum('population')

    # THEN
    assert series.California == 497057
