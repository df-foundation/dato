# Passing multiple arguments

Unlike R's `magrittr`, `dpipe` allows for any number of arguments to be passed through `>>`, and used in order as arguments in the receiving `Pipeable` object. While this can be implemented using special tuple-processing logic, we provide the `unpack_input` decorator to simplify this process.

For example, a common example is the `pandas.merge` method, which merges two tables

```text
df = pd.merge(a, b, on='id') # pandas implementation.
(a, b) >> Merge # dpipe implementation. 
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



