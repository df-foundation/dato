# Visualization

Visualization methods are located in `./dato/plot.py` \(the `dato.plot` module\). We also support improved \(in our opinion\) default styles, specified in `./dato/style.py`.

## dato.Plot

 We have a single main plotting function, `Plot`, which loosely follows the `pandas.DataFrame.plot()` syntactical structure.

```text
df >> Plot('a', 'b', kind='line')
```

While we originally intended the plotting sub-module to simply wrap `matplotlib`, `pandas`, and/or `seaborn`, we very quickly realized a pain point in doing this is that each of these libraries has **vastly different syntactical structures** \(even internally!\). We decided to prioritize simplicity over universal inclusion, and therefore ultimately decided on having a single base plotting function.

`kind` can take the following arguments:

* scatter
* line
* hist
* bar
* barh
* box

We implement each of these as stand-alone Pipeable objects as well \(capitalized\) -- `Scatter`, `Hist` , `Bar`, etc \(`Line` doesn't exist, as it's the default functionality of `Plot`\).

Although `dato.Plot` does borrow most of its base syntactical structure from `pandas`, it does have some extended functionality inherited from `seaborn`. For example, facet grids \(and so the arguments `row`, `col` and `hue`\)  are natively supported:

```text
df >> Hist('Age', col='Sex', hue='Survived', alpha=0.5)
```

![](../.gitbook/assets/image%20%283%29.png)

## Styling

We currently support three modes: `dark_mode`, `light_mode`, and `default` \(which disables all styling\), which can be toggled as follows:

```text
import dato
dato.style.use('dato_dark')
dato.style.use('dato_light')
dato.style.use('default')
```

The colors specifying these styles are located in the `dpipe.plot.STYLES` dictionary. These default styles are implemented using the `mpl_style_decorator` function, which can be applied as a decorator before applying the `Pipeable` decorator.

By default, the above commands apply `dato` styles globally, but these can be restricted to `dato` plots only by using the `dato_only` keyword argument:

```text
dato.style.use('dato_dark', dato_only=True)
```

![](../.gitbook/assets/image%20%282%29.png)



