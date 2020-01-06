# Data cleaning

Data cleaning and processing functions are located in `./dpipe/process.py` \(the `dpipe.process` module\). This module is largely comprised of `pandas`-wrapped functions.

In general, any `pandas` function should have an analogue in `dpipe`, following an UpperCamelCase naming convention, and dropping underscores. For example, `pd.merge` becomes `dpipe.Merge`, `pd.to_datetime` becomes `dpipe.ToDatetime`, and `pd.DataFrame.groupby` becomes `dpipe.GroupBy`.

 

