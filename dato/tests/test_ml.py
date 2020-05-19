import pytest
import sklearn as skl

from .fixtures import mock_data_a, mock_data_b, mock_data_date, mock_data_training, mock_user_data
from .helpers import full_mock_model, compare_encoders
from pipey import Pipeable
from dato.process import Drop, GroupBy, Mean, Merge, Sample, Select, Sum, ToDatetime
from dato.ml import LabelEnc

import dato

EPS = 1e-10


def test_full_LinearReg(mock_data_training):
    # GIVEN
    df = mock_data_training
    encoder = skl.preprocessing.LabelEncoder
    reg = skl.linear_model.LinearRegression

    # WHEN
    mse_manual, mse_piped = full_mock_model(mock_data_training, encoder, reg)

    # THEN
    assert (mse_piped - mse_manual) < EPS


def test_LabelEnc(mock_data_training):
    # WHEN
    encoder_outputs_are_same = compare_encoders(mock_data_training, skl.preprocessing.LabelEncoder, LabelEnc)

    # THEN
    assert encoder_outputs_are_same == True

