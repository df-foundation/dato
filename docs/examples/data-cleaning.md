# Data cleaning

Data cleaning and processing functions are located in `./dato/process.py` \(the `dato.process` module\). This module is largely comprised of `pandas`-wrapped functions.

In general, any `pandas` function should have an analogue in `dato`, following an UpperCamelCase naming convention, and dropping underscores. For example, `pd.merge` becomes `dato.Merge`, `pd.to_datetime` becomes `dato.ToDatetime`, and `pd.DataFrame.groupby` becomes `dato.GroupBy`.

```text
df >> GroupBy('a') >> Sum('b') >> ValueCounts
```

However, aside from declarative-ready operations like this \(that are attributes in pandas\), it can  require some deep knowledge of `pandas` to understand how to do simple operations like filtering or mutation \(to use R's terminology\). We'll briefly cover these within this page.

## Mutating with `Eval`

A common operation in dealing with dataframes is to make a new column out of some combination of other columns. For example, in our work, the following is a common pattern:

```text
df['C'] = df[df.A + df.B]
```

In R, this is called mutation, but in pandas, a little-known fact is that it is included as a function called `eval`. This thus can be implemented easily in `dato` as:

```text
df >> Eval('C = A + B')
```

For those familiar with `mutate`, we've also implemented a function called `Mutate` which does the same thing. See the [pandas documentation on `eval`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.eval.html) for a full overview of the the functionality.

## Filtering with `Query`

Another common pattern in dataframe munging is to filter a dataframe on some condition \(e.g. two columns are both true\). For example:

```text
df = df[df.A > df.B]
```

This can be accomplished with the `Query` function as follows:

```text
df >> Query('A > B')
```

See the [pandas documentation on `query`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) for a full overview of the functionality.

## Selecting with `Select`

Another common operation is to simply select columns.

```text
df = df[['A', 'B']]
```

We enable this in `dato`  using the `Select` operation:

```text
df >> Select('A', 'B')
```



