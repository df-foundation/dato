# Data cleaning

Data cleaning and processing functions are located in `./dato/process.py` \(the `dato.process` module\). This module is largely comprised of `pandas`-wrapped functions.

In general, any `pandas` function should have an analogue in `dato`, following an UpperCamelCase naming convention, and dropping underscores. For example, `pd.merge` becomes `dato.Merge`, `pd.to_datetime` becomes `dato.ToDatetime`, and `pd.DataFrame.groupby` becomes `dato.GroupBy`.

```text
df >> GroupBy('a') >> Sum('b') >> ValueCounts
```

