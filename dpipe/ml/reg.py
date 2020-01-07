from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import numpy as np
import sklearn as skl

from ..base import Pipeable
from .preprocessing import SpecifyLabel, TrainTestSplit
from .base import _ModelSpec


@Pipeable
def LinearReg(dpipe_output, sample_weight=None, **kwargs):
    m = _ModelSpec(dpipe_output, estimator=LinearRegression, **kwargs)
    m.estimator.fit(m.train_X, m.train_y, sample_weight=sample_weight)
    m.predict()
    m.evaluate(kind='regressor')
    return m


@Pipeable
def DecisionTreeReg(dpipe_output, sample_weight=None, check_input=True, X_idx_sorted=None, **kwargs):
    m = _ModelSpec(dpipe_output, estimator=DecisionTreeRegressor, **kwargs)
    m.estimator.fit(m.train_X, m.train_y, sample_weight=sample_weight, check_input=check_input, X_idx_sorted=X_idx_sorted)
    m.predict()
    m.evaluate(kind='regressor')
    return m


@Pipeable
def XGBReg(dpipe_output, sample_weight=None, eval_set=None, eval_metric=None, early_stopping_rounds=None, verbose=True, xgb_model=None, sample_weight_eval_set=None, callbacks=None, **kwargs):
    m = _ModelSpec(dpipe_output, estimator=XGBRegressor, **kwargs)
    m.estimator.fit(m.train_X, m.train_y, sample_weight=sample_weight, eval_set=eval_set, eval_metric=eval_metric, early_stopping_rounds=early_stopping_rounds, verbose=verbose, xgb_model=xgb_model, sample_weight_eval_set=sample_weight_eval_set, callbacks=callbacks)
    m.predict()
    m.evaluate(kind='regressor')
    return m


