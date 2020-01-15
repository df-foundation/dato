# Enable normal calls

By default, `Pipeable`-decorated functions can **only be called with `>>`**. For example, `a >> b(c=1)` is the only way to run `b(a, c=1)`.

We disable this to prevent accidental calls, in case `b(c=1)` is in fact a valid function call. While such accidental calls won't happen unless `b` accepts only named optional arguments, we chose to prioritize safety and explicit behavior over convenience.

Nonetheless, we do support the keyword argument `try_normal_call_first` , which can be passed to the `Pipeable` decorator to have objects try the normal function call first, then try the piping behavior. For `Pipeable` objects created in this way, we strongly suggest **having one un-named positional parameter**, to mitigate the above problem.

An example illustrating this behavior:

```text
@Pipeable(try_normal_call_first=True)
def b(a, c=1):
    pass

# Both of these will now work:
b(a, c=1)
a >> b(c=1)
```

