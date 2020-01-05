import pytest
import pandas as pd
import matplotlib as mpl

from .fixtures import mock_user_data, mock_class_object
from dpipe.base import Pipeable
from dpipe.utils import is_date, series_is_date

import dpipe


def test_is_date():
    # GIVEN
    date_as_string = '2019-08-08'

    # WHEN
    string_is_date = is_date(date_as_string)

    # THEN
    assert string_is_date == True


def test_series_is_date():
    # GIVEN
    mock_series = pd.Series(['2019-09-01', '2019-08'])

    # WHEN
    mock_series_is_date = series_is_date(mock_series)

    # THEN
    assert mock_series_is_date == True

