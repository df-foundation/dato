import numpy as np
import sklearn as skl


def _print_regression_error(y_true, y_pred):
    print('Max error:', skl.metrics.max_error(y_true, y_pred))
    print('Mean absolute error:', skl.metrics.mean_absolute_error(y_true, y_pred))
    print('Mean squared error:', skl.metrics.mean_squared_error(y_true, y_pred))
    print('Root mean squared error:', np.sqrt(skl.metrics.mean_squared_error(y_true, y_pred)))


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

    def predict(self):
        self.train_y_prediction = self.estimator.predict(self.X_train)
        if self.test is not None:
            self.test_y_prediction = self.estimator.predict(self.X_test)

    def evaluate(self, kind='regressor'):
        if kind=='regressor':
            if self.test is not None:
                print('\033[1mTraining set')
                print(len('Training set')*'-','\033[0m')
            _print_regression_error(self.y_train, self.train_y_prediction)
            print('\n')
            if self.test is not None:
                print('\033[1mTest set')
                print(len('Test set')*'-','\033[0m')
                _print_regression_error(self.y_test, self.test_y_prediction)
        elif kind=='classifier':
            if self.test is not None:
                # Plot roc auc curve.
                pass


