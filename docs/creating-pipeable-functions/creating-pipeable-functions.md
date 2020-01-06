# Creating pipeable functions

`dpipe` is meant to be flexible, and therefore can accept \(almost\) anything as input. Creating custom functions compatible with the `dpipe` framework is therefore quite easy, as long as an existing `__rshift__` method doesn't exist for the object being piped. 

The class `dpipe.base.Pipeable` can wrap or decorate any method to enable compatibility with the `>>` operator. For example:

```text
@Pipeable
def Func(*args, **kwargs):
    return func(*args, **kwargs)
```

Or even more concisely, any existing function `func` that you'd like to use with `dpipe` can be trivially implemented as follows:

```text
Func = Pipeable(func)
```

The entire piping framework is incredibly simple \(it only takes up around 20 lines of code\), and can be found in `dpipe.base.Pipeable`. If you write a custom function, please consider making a pull request. _Happy piping!_

