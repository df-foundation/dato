# Visualization

Visualization methods are located in `./dpipe/plot.py` \(the `dpipe.plot` module\). By default, all plotting functions use `matplotlib` as the base plotting library, but with \(in our opinion\) improved default styles, specified in `./dpipe/style.py`. 

We again follow the same naming convention where possible -- we name `Pipeable`-decorated functions with the same name as the underlying `matplotlib` functions, but formatted in UpperCamelCase with underscores removed.

## Styling

We currently support two modes: `dark_mode` and `light_mode`, which can be toggled as follows:

```text
import dpipe
dpipe.style.rc['style'] = 'dark_mode'   # Dark mode.
dpipe.style.rc['style'] = 'light_mode'  # Light mode.
```

The colors specifying these styles are located in the `dpipe.plot.STYLES` dictionary, keyed by `dark_mode` or `light_mode`.

These default styles are implemented using the `mpl_style_decorator` function, which can be applied as a decorator before applying the `Pipeable` decorator. 

