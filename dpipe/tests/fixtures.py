import pytest
import numpy as np
import pandas as pd
from dpipe.sampledata.datagen import user_data, purchase_data


@pytest.fixture()
def mock_user_data():
    return user_data(100, random_state=2701)


@pytest.fixture()
def mock_data_a():
    return pd.DataFrame({'id': [0,1,2], 'b': [2,3,4]})


@pytest.fixture()
def mock_data_b():
    return pd.DataFrame({'id': [0,1,2], 'c': [9,9,8]})


@pytest.fixture()
def mock_data_date():
    return pd.DataFrame({'id': [0,1,2], 'date': ['2019-01-01', '2019-01-02', '2019-01']})


@pytest.fixture()
def mock_data_null():
    return pd.DataFrame({'id': [0,1,2], 'value': [np.nan, np.nan, 1]})

@pytest.fixture()
def mock_data_training():
    return pd.DataFrame({'x1': [0,1,2], 'x2':['sad', 'happy', 'okay'], 'y': [0,2,1]})


@pytest.fixture()
def mock_purchase_data():
    return purchase_data(100, random_state=2701)


@pytest.fixture()
def mock_class_object():
    class NewObject:
        def mock_method(self):
            return True

    return NewObject()

