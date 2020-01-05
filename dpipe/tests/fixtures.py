import pytest
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
    return  pd.DataFrame({'id': [0,1,2], 'c': [9,8,0]})


@pytest.fixture()
def mock_purchase_data():
    return purchase_data(100, random_state=2701)


@pytest.fixture()
def mock_class_object():
    class NewObject:
        def mock_method(self):
            return True

    return NewObject()

