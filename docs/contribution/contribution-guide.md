# Contribution guide

_**We welcome contributions!**_ The space of data-science/ML tooling is quite large, so we need help to incorporate as much as we can into `dpipe`. We simply ask that you adhere to the following:

* **Follow our naming convention.** Where possible, follow the UpperCamelCase convention in naming your `Pipeable`-decorated functions, while, if wrapping a function from another library, keeping the name as close to the original function as possible.
* **Add a unit test.** Add a unit test to `./dpipe/tests`, under the appropriate `test_*.py` file \(these files are organized so the `*` parallels the location of the `Pipeable`-decorated function -- e.g. tests for functions in `process.py` should be contained in `test_process.py`\). Test datasets can be found in `./dpipe/tests/fixtures.py`.

