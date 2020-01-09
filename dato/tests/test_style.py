import pytest
import matplotlib as mpl

from .fixtures import mock_user_data, mock_class_object
from dato.base import Pipeable
from dato.style import mpl_style_decorator

import dato


def test_mpl_style_decorator_state_restoration():
    # GIVEN
    pipeable_styled_lambda = mpl_style_decorator(Pipeable(lambda x: x))
    state_before_call = dict(mpl.rcParams).copy()

    # WHEN
    1 >> pipeable_styled_lambda()

    # THEN
    state_after_call = dict(mpl.rcParams)

    assert state_before_call == state_after_call
