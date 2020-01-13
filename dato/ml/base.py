import inspect
import numpy as np
import sklearn as skl
import matplotlib.pyplot as plt


from ..style import mpl_style_decorator

FIT_KWS = [
    'sample_weight',
    'check_input',
    'X_idx_sorted',
    'eval_set',
    'eval_metric',
    'early_stopping_rounds',
    'verbose',
    'xgb_model',
    'sample_weight_eval_set',
    'callbacks',
]

def _separate_estimator_fit_params(Estimator, **kwargs):
    est_params = inspect.getfullargspec(Estimator)[0]
    fit_params = inspect.getfullargspec(Estimator().fit)[0]

    est_kwargs = {}
    fit_kwargs = {}
    for kw, val in kwargs.items():
        if kw in est_params:
            est_kwargs[kw] = val
        elif kw in fit_params:
            fit_kwargs[kw] = val

    return est_kwargs, fit_kwargs


def _print_regression_error(y_true, y_pred):
    print('Max error:', skl.metrics.max_error(y_true, y_pred))
    print('Mean absolute error:', skl.metrics.mean_absolute_error(y_true, y_pred))
    print('Mean squared error:', skl.metrics.mean_squared_error(y_true, y_pred))
    print('Root mean squared error:', np.sqrt(skl.metrics.mean_squared_error(y_true, y_pred)))


@mpl_style_decorator
def _plot_roc_curve(y_true, y_pred, **kwargs):
    roc = skl.metrics.roc_curve(y_true, y_pred, **kwargs)
    plt.plot(roc[0], roc[1], 'o-')
    plt.plot([0,0], [1,1], ':')


class _ModelSpec():
    def __init__(self, df):
        self.data = df
        self.original_data = df.copy()
        self.train = df
        self.test = None
        self.encoders = {}
        self.X_train = self.data.iloc[:,:-1]
        self.y_train = self.data.iloc[:,-1]
        self.X_test = None
        self.y_test = None

    def encode(self, Encoder, columns):
        enc_dict = {}
        for column in columns:
            enc = Encoder()
            self.data[column] = enc.fit_transform(self.data[column])
            enc_dict[column] = enc
        self.encoders.update(enc_dict)

        return self.data, enc_dict

    def train_test_split(self, **kwargs):
        self.train, self.test = skl.model_selection.train_test_split(self.data, **kwargs)
        self.X_train = self.train.iloc[:,:-1]
        self.y_train = self.train.iloc[:,-1]
        self.X_test = self.test.iloc[:,:-1]
        self.y_test = self.test.iloc[:,-1]
        return self.train, self.test

    def instantiate_estimator(self, Estimator, **kwargs):
        self.estimator = Estimator(**kwargs)

    def predict(self, kind='regressor'):
        if kind=='regressor':
            self.y_train_pred = self.estimator.predict(self.X_train)
            if self.test is not None:
                self.y_test_pred = self.estimator.predict(self.X_test)
        elif kind=='classifier':
            self.y_train_pred = self.estimator.predict_proba(self.X_train)
            if self.test is not None:
                self.y_test_pred = self.estimator.predict_proba(self.X_test)

    def evaluate(self, kind='regressor'):
        if kind=='regressor':
            if self.test is not None:
                print('\033[1mTraining set')
                print(len('Training set')*'-','\033[0m')
            _print_regression_error(self.y_train, self.y_train_pred)
            print('\n')
            if self.test is not None:
                print('\033[1mTest set')
                print(len('Test set')*'-','\033[0m')
                _print_regression_error(self.y_test, self.y_test_pred)
        elif kind=='classifier':
            if self.test is not None:

                # Binary classification.
                if self.y_test_pred.shape[1] == 2:
                    _plot_roc_curve(self.y_test, self.y_test_pred[:,1])
                    print('\033[1mAUC: \033[0m')
                    print(skl.metrics.roc_auc_score(self.y_test, self.y_test_pred[:,1]))

                # Multiclass classification.
                else:
                    pass

    def instantiate_train_predict_eval(self, Estimator, kind='regressor', **kwargs):
        """
        Instantiate, fit, predict, train.
        """
        est_kwargs, fit_kwargs = _separate_estimator_fit_params(Estimator)
        self.instantiate_estimator(Estimator, **est_kwargs)
        self.estimator.fit(self.X_train, self.y_train, **fit_kwargs)
        self.predict(kind=kind)
        self.evaluate(kind=kind)
        return self.estimator
