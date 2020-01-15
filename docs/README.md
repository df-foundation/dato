# dataframehq/dato



![](https://github.com/dataframehq/dato/blob/master/docs/_static/img/dato.png?raw=true)

`dato` is an open source library that provides a **rapid, declarative ecosystem for reproducible data science** within python. `dato` accomplishes this by \(1\) enabling piping with `>>` and \(2\) unifying common data science libraries under a common syntax.

```text
df >> GroupBy('country') >> Sum >> Hist('revenue', col='age')
```

Dato has four major components: 

* **`dato.base.Pipeable`** Decorator that enables piping with `>>`. 
* **`dato.process`** Sub-module with pipe-compatible `pandas` operations.
* **`dato.plot`** Sub-module with pipe-compatible plotting operations, following a consistent `pandas`-inspired syntax with `seaborn`-esque extended functionality.
* **`dato.ml`**_\(in development\)_  Simplifies and standardizes syntax across popular ML libraries.

## Installation

```text
pip install dato
```

## Why pipe?

Although piping has some downside as a general programming paradigm \(particularly in obscuring code errors and being naturally difficult to debug\), we argue that these downsides are outweighed by a level of concision and maintainability it lends to _data workflows_. When working with data in development environments which contain hidden states \(such as jupyter or R markdown\), reproducibility of code can be difficult to consistently achieve. Piping mitigates this danger by \(1\) enforcing a consistent order of operations, and \(2\) disallowing hidden states. Consequently, **the piping paradigm is naturally reproducible, production-ready, and stable as soon as it is written** -- properties that are of paramount importance in data work.

