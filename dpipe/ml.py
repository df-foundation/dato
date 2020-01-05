"""
Matplotlib plotting functions.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import numpy as np
import sklearn as skl
from .base import Pipeable


@Pipeable
def SpecifyLabel(df, Y_column, *args, **kwargs):
    """The label for
    """
    X_columns = [col for col in df.columns if col!=Y_column]
    return df[X_columns + [Y_column]]


@Pipeable
def TrainTestSplit(*args, **kwargs):
    return train_test_split(*args, **kwargs)


def _print_regression_error(y_true, y_pred):
    print('Max error:', skl.metrics.max_error(y_true, y_pred))
    print('Mean absolute error:', skl.metrics.mean_absolute_error(y_true, y_pred))
    print('Mean squared error:', skl.metrics.mean_squared_error(y_true, y_pred))
    print('Root mean squared error:', np.sqrt(skl.metrics.mean_squared_error(y_true, y_pred)))


class _ModelSpec():
    def __init__(self, dpipe_output, estimator=None, **kwargs):

        # Handle if train test split has been used (and so the input is a two-element list).
        if type(dpipe_output) == list:
            self.train = dpipe_output[0]
            self.test = dpipe_output[1]
            self.test_X = self.test.iloc[:,:-1]
            self.test_y = self.test.iloc[:,-1]
        else:
            self.train = dpipe_output[0]
            self.test = None

        self.train_X = self.train.iloc[:,:-1]
        self.train_y = self.train.iloc[:,-1]
        self.estimator = estimator(**kwargs)

    def predict(self):
        self.train_y_prediction = self.estimator.predict(self.train_X)
        if self.test is not None:
            self.test_y_prediction = self.estimator.predict(self.test_X)

    def evaluate(self, kind='regressor'):
        if self.test is not None:
            print('\033[1mTraining set')
            print(len('Training set')*'-','\033[0m')
        _print_regression_error(self.train_y, self.train_y_prediction)
        print('\n')
        if self.test is not None:
            print('\033[1mTest set')
            print(len('Test set')*'-','\033[0m')
            _print_regression_error(self.test_y, self.test_y_prediction)


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


