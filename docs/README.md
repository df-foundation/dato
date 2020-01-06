# dataframehq/dpipe



![](https://github.com/dataframehq/dpipe/blob/master/docs/_static/img/dpipe.png?raw=true)

`dpipe` is an open source library that provides **declarative syntactic sugar** within python to improve the readability of data manipulations. For those familiar with the R tidyverse ecosystem, `dpipe` facilitates magrittr-style piping using the right bitshift operator `>>`, while staying largely pythonic in implementation. Unlike other `pandas`-oriented systems \(e.g. [dfply](https://github.com/kieferk/dfply) or [pandas-ply](https://github.com/coursera/pandas-ply)\), `dpipe` is meant to be flexible, and therefore does not enforce any particular object input types.

Simply put, nested functions can be decorated so that

```text
d(c(b(a)))
```

can be rewritten

```text
a >> b >> c >> d
```

Though the basic piping behavior is supported in R, `dpipe` enables it within Python for easier debugging and productionization support, while also forcing this pattern to be explicitly scoped for safety \(we also support piping of multiple arguments!\). In addition, we supply convenient, opinionated sub-modules that we personally use to quickly execute simple data science tasks.

Our primary objective here is not to provide a new library that supersedes data science staples such as `pandas`, `matplotlib`, or `scikit-learn` but rather, to:

1. Provide a flexible way to safely and easily use _any_ library, declaratively, in support of declarative data workflows.
2. Introduce opinionated versions of common data operations to improve QOL.

## Why pipe?

Although piping has some downside as a general programming paradigm \(particularly in obscuring code errors and being naturally difficult to debug\), we argue that these downsides are outweighed by a level of concision and maintainability it lends to _data workflows_. When working with data in development environments which contain hidden states \(such as jupyter or R markdown\), reproducibility of code can be difficult to consistently achieve. Piping mitigates this danger by \(1\) enforcing a consistent order of operations, and \(2\) disallowing hidden states. Consequently, **the piping paradigm is naturally reproducible, production-ready, and stable as soon as it is written** -- properties that are of paramount importance in data work.

## Installation

```text
pip install dpipe
```

