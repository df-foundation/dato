import sklearn as skl

from dato.ml import InitModel, LabelEnc, TrainTestSplit, LinearReg


def full_mock_model(df, Encoder, Estimator):
    le = Encoder()
    df['x2'] = le.fit_transform(df.x2)
    X = df[['x1', 'x2']]
    y = df['y']
    X_train, X_test, y_train, y_test = skl.model_selection.train_test_split(X, y, random_state=2701)
    reg = Estimator()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    y_train_pred = reg.predict(X_train)
    mse_manual = skl.metrics.mean_squared_error(y_train, y_train_pred)

    # Use pipeables to create model.
    model_output = df \
        >> InitModel(label='y') \
        >> LabelEnc(columns=['x2']) \
        >> TrainTestSplit(random_state=2701) \
        >> LinearReg

    modelspec = model_output
    mse_piped = skl.metrics.mean_squared_error(modelspec.y_train, modelspec.y_train_pred)
    return mse_manual, mse_piped


def compare_encoders(df, Encoder, Enc):
    """
    Given a scikit-learn encoder and a Pipeable-wrapped encoder object, ensure they encode the same way.

    :param Encoder: scikit-learn encoder.
    :param Enc: pipeable encoder.
    """
    le = Encoder()
    new_x2_manual = le.fit_transform(df.x2)

    output = df >> InitModel(label='y') >> Enc(columns=['x2'])
    modelspec = output
    return (new_x2_manual == modelspec.data.x2).all()
