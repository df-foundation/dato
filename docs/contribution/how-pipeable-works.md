# How Pipeable works

We find that a substantial roadblock in contributing to open-source libraries is **not understanding the underlying code**. We note that this is actually quite easy, as the `Pipeable` class is only about 20 lines long and contains almost the entirety of the logic supporting the `dpipe` framework. We briefly describe this here.

## Overview

The `Pipeable` class is defined in `./dpipe/base.py`, and is entirely self-contained therein. The primary feature of the class is that it overloads `__rrshift__`, allowing for any `Pipeable` object to define the behavior of a right bitshift \(`>>`\) operator to its left.

The base functions being decorated by this class are stored in `Pipeable.base_object`, and later referenced by our modified methods.

Overall, a few other methods are modified by `Pipeable`, primarily to support extensions in future work and edge cases.

* `__rshift__`: to allow for explicit typing of inputs, in case input variables already have a `__rshift__` method already defined.
* `__rrshift__`: provides most of the functionality behind the `Pipeable` class.
* `__getattr__`: not entirely necessary, but included to allow the underlying object to be accessed and used normally without accessing the `base_object` attribute.
* `__call__`: calls `__init__`, to enable class decoration in the case where arguments are passed to `Pipeable`.



