<img width="250" src="https://github.com/dataframehq/dpipe/blob/master/docs/_static/img/dpipe.png?raw=true">

----------------------------------------

`dpipe` is an open source library that provides **declarative syntactical sugar** within python to improve the readability of data manipulations. For those familiar with the R tidyverse ecosystem, `dpipe` facilitates magrittr-style piping using the right bitshift operator `>>`, while staying largely pythonic in implementation. Unlike other `pandas`-oriented systems (e.g. [dfply](https://github.com/kieferk/dfply) or [pandas-ply](https://github.com/coursera/pandas-ply)), `dpipe` is meant to be flexible, and therefore does not enforce any particular object input types.

We used this framework to implement data science-specific methods to improve QOL when performing repetitive data-related tasks (and to illustrate the potential of `dpipe`). Our biggest pain points in this domain have been:

* Remembering pandas syntax and defaults.
* Styling matplotlib visualizations.
* Remembering scikit-learn model creation syntax, best practices, and evaluation metrics.


## Installation
```
pip install dpipe
```

## Examples

### More readable pandas

A common pattern in exploratory analyses is to aggregate one value with respect to another. In pandas, this is typically accomplished as follows:

```
df['date'] = pd.to_datetime(df.date)
gb = df.groupby('date').sum()['sale_value']
gb.plot()
```

While `pandas` has already done an incredible amount of heavy lifting to make this aggregation syntactically quite simple, it still takes some thought, trial, and error to correctly write the above few commands. The same command in `dpipe` can be rewritten as follows:

```
df >> GroupBy('date') >> Sum('sale_value') >> Plot()
```


### Auto-styled matplotlib
`matplotlib` is a staple in data visualization, primarily for its flexibility and speed. However, generating a presentation-ready plot takes an extraordinarily long time with substantial cognitive load, owing to library-specific syntax and an immense styling dictionary (`mpl.rcParams`). Below is an example from `./examples/sample.ipynb` here to illustrate how cumbersome this can be.

```
plt.figure(figsize=(8.5,5.2))
plt.scatter(a.lat, a.lng, alpha=0.5, s=100)
plt.scatter(b.lat, b.lng, alpha=0.1, s=100)
plt.scatter(c.lat, c.lng, alpha=0.1, s=100)
plt.grid('on', linestyle=':')
plt.rcParams.update({'font.size': 15})
```

While this script isn't particularly long, each argument (`s` for `scatter`, the `'on'` arg for `grid`, the keys for `rcParams`), in our experience, warrants a stackoverflow crawl. Even with almost a decade of experience using matplotlib, it still takes about 5 minutes to write up that snippet.

We therefore implement some improved basic styling to reduce the overhead of using matplotlib (granted, style is incredibly subjective, and you may find our decisions horrendous). At the least, we hope that this will improve the readability of your code, and at best, reduce the need to use any matplotlib styling.


```
(a.lat, a.lng) >> Scatter
(b.lat, b.lng) >> Scatter(alpha=0.1)
(c.lat, c.lng) >> Scatter(alpha=0.1)
```

### Cleaner sklearn
We also provide limited, but ever-growing ML tooling, wrapping sklearn and xgboost. We do not intend this to replace existing libraries, but to more quickly test the feasibility of a model.

A disclaimer regarding ML: while, in general, `dpipe` does not modify outputs, because of the complex, branching nature of machine-learning workflows (creating and holding onto a validation set, for example), we created a hidden `_ModelSpec` method that holds model-related information (the train and test sets). A `_ModelSpec` class object (here represented as `m`) contains the following attributes:

* `m.train`: the training data.
* `m.test`: the test data.
* `m.estimator`: the underlying scikit-learn estimator.

A typical full-on ML effort (without any sort of categorical encoding) can be condensed as follows:

```
df = pd.merge(users, purchases, on='id_user')
df = df[['population', 'density', 'sale_value']]
X = df[['population', 'density']]
y = df['sale_value']
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y)
reg = sklearn.linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
y_train_pred = reg.predict(X_train)
print('Mean squared error:', sklearn.metrics.mean_squared_error(y_train, y_train_pred))
print('Mean absolute error:', sklearn.metrics.mean_absolute_error(y_train, y_train_pred))
print('Root mean squared error:', np.sqrt(sklearn.metrics.mean_squared_error(y_train, y_train_pred)))
print('Mean squared error:', sklearn.metrics.mean_squared_error(y_test, y_pred))
print('Mean absolute error:', sklearn.metrics.mean_absolute_error(y_test, y_pred))
print('Root mean squared error:', np.sqrt(sklearn.metrics.mean_squared_error(y_test, y_pred)))
```

But it's still clearly quite cumbersome, even without the imports. With `dpipe` tooling, this entire process can be condensed as follows:

```
modelspec = (users, purchases) \
    >> Merge(on='id_user') \
    >> Select('population', 'density', 'sale_value') \
    >> SpecifyLabel('sale_value') \
    >> TrainTestSplit \
    >> LinearReg
```

## Custom functions

`dpipe` is meant to be flexible, and therefore can accept (almost) anything as input. Creating custom functions compatible with the `dpipe` framework is therefore quite easy. The class `dpipe.base.Pipeable` can wrap or decorate any method to enable compatibility with the `>>` operator. For example, the `Sum` method above is very simply defined as follows:

```
@Pipeable
def Sum(gb, column):
    grouped_sum = gb.sum()[column]
    return grouped_sum
```

Or even more concisely, any existing function `func` that you'd like to use with `dpipe` can be trivially implemented as follows:

```
Func = Pipeable(func)
```

The entire piping framework is incredibly simple (it only takes up around 20 lines of code), and can be found in `dpipe.base.Pipeable`. If you write a custom function (even a wrapper around something trivial, like `Sum` above), please consider making a pull request. Happy piping!
