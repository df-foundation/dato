import numpy as np
import sklearn as skl


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
        if kind=='regressor':
            if self.test is not None:
                print('\033[1mTraining set')
                print(len('Training set')*'-','\033[0m')
            _print_regression_error(self.train_y, self.train_y_prediction)
            print('\n')
            if self.test is not None:
                print('\033[1mTest set')
                print(len('Test set')*'-','\033[0m')
                _print_regression_error(self.test_y, self.test_y_prediction)
        elif kind=='classifier':
            if self.test is not None:
                # Plot roc auc curve.
                pass


