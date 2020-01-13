from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import numpy as np
import sklearn as skl

from ..base import Pipeable, use_first_arg_only


@Pipeable
def LinearReg(m, **kwargs):
    m.instantiate_train_predict_eval(LinearRegression, kind='regressor')
    return m


@Pipeable
def DecisionTreeReg(m, **kwargs):
    m.instantiate_train_predict_eval(DecisionTreeRegressor, kind='regressor')
    return m


@Pipeable
def XGBReg(m, **kwargs):
    m.instantiate_train_predict_eval(XGBRegressor, kind='regressor')
    return m


