# Machine learning

We provide basic machine learning tooling by wrapping `scikit-learn` objects, contained in `./dpipe/ml.py` \(the `dpipe.ml` module\). Where possible, we following our typical naming convention - UpperCamelCase w/underscores removed, but because many scikit-learn objects are classes, this is not always possible. For `Regressor` and `Classifier` objects, we therefore simply abridge these terms to `Reg` and `Clf` in our `Pipeable`-wrapped versions. For example, the `LinearRegression` implementation is called `LinearReg`, and `XGBRegressor` is named `XGBReg`

## The `_ModelSpec` accumulator

Unfortunately, machine learning modeling does not always follow a single-i/o workstream. Data is often split off and reserved for validation, requiring an accumulator to be passed through our pipelines, storing this data for downstream consumption. We do this by initiating a `_ModelSpec` object once `InitModel` is called. Users may want to access the following components of this class while debugging their models:

```text
_ModelSpec.X_train
_ModelSpec.y_train
_ModelSpec.X_test
_ModelSpec.y_test
_ModelSpec.estimator
```

The `train_` and `test_` objects contain the training and test data, respectively. The `estimator` is the instantiated class object for the underlying `scikit-learn` class.

## A typical ML example

Because there is typically a standard set of tasks for creating simple machine learning models, we lay out the necessary functions here. The following steps are generally required:

1. Encode categorical variables.
2. Fill nulls.
3. Split data into a training and test set.
4. Train the model over the training set.
5. Predict and evaluate the model.

This can be accomplished as follows:

```text
df \
    >> InitModel(label='y')
    >> OneHotEncode('x1', 'x2') \
    >> FillNA(-1) \
    >> TrainTestSplit \
    >> LinearReg
```

