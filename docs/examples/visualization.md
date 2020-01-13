# Visualization

Visualization methods are located in `./dato/plot.py` \(the `dato.plot` module\). By default, all plotting functions use `matplotlib` as the base plotting library, but with \(in our opinion\) improved default styles, specified in `./dato/style.py`.

We again follow the same naming convention where possible -- we name `Pipeable`-decorated functions with the same name as the underlying `matplotlib` functions, but formatted in UpperCamelCase with underscores removed.

## Styling

We currently support two modes: `dark_mode` and `light_mode`, which can be toggled as follows:

```text
import dato
dato.style.use('dato_dark')
dato.style.use('dato_light')
```

The colors specifying these styles are located in the `dpipe.plot.STYLES` dictionary. These default styles are implemented using the `mpl_style_decorator` function, which can be applied as a decorator before applying the `Pipeable` decorator.

By default, the above commands apply `dato` styles globally, but these can be restricted to `dato` plots only by using the `dato_only` keyword argument:

```text
dato.style.use('dato_dark', dato_only=True)
```

