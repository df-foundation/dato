# Special handling of inputs

Unlike R's `magrittr`, `dato` allows for any number of arguments to be passed through `>>`, and used in order as arguments in the receiving `Pipeable` object. While this can be implemented using some simple array-processing logic, we provide a number of decorators and arguments to make this process more convenient:

* `unpack_input`: pass `input` as `*input`.
* : pass only the first element of `input`.

For example, a common example is the `pandas.merge` method, which merges two tables

```text
df = pd.merge(a, b, on='id') # pandas implementation.
(a, b) >> Merge # dato implementation.
```

The above can be implemented without the `unpack_input` decorator as follows:

```text
def Merge(df_tuple, args, **kwargs):
    a = df_tuple[0] b = df_tuple[1]
    return pd.merge(a, b, args, **kwargs)
```

Or, more simply with `unpack_input` as:

```text
@unpack_input
@Pipeable
def Merge(args, **kwargs):
    pd.merge(args, **kwargs)
```



