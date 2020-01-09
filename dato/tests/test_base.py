import pytest
import pandas as pd

from .fixtures import mock_user_data, mock_class_object
from dato.base import Pipeable
from dato.process import GroupBy

import dato


def test_Pipeable_base_object_type(mock_class_object):
    """Ensure that Pipeable doesn't change the type of a function.
    """

    # WHEN
    pipeable_object = Pipeable(mock_class_object)
    assert type(pipeable_object.base_object) == type(mock_class_object)


def test_Pipeable_getattr(mock_class_object):
    """Ensure Pipeable inherits the methods of the base object class.
    """
    # WHEN
    pipeable_object = Pipeable(mock_class_object)

    # THEN
    assert pipeable_object.mock_method() == True
