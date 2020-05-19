from xgboost import XGBRegressor
import numpy as np
import sklearn as skl
from sklearn import linear_model

from pipey import Pipeable, use_first_arg_only


@Pipeable
def LogisticReg(m, **kwargs):
    m.instantiate_train_predict_eval(linear_model.LogisticRegression, kind='classifier')
    return m


