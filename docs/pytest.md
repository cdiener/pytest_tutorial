<!-- .slide: data-background="assets/front.jpg" -->
# Writing tests with pytest

### Christian Diener
### Pythonday 2017 <!-- .element: class="accent" -->

===

### Our example project

https://github.com/pythondaymx/taller_testing

Clone/download please <i class="fa fa-smile-o"></i>.

---

## What is testing?

Writing code to verify that other code works.

Developer usually participates only in <span class="accent">unit testing</span>
or integration testing.

---

## unit testing

A unit test is a small fragment of code that tests one *functional unit* of
our software.

What in the world is the *unit*? Depends on you, most people test *functions* or
*classes*.

---

## What is a good unit test?

A good unit test...

- isolates as much as possible
- can be scripted on paper
- tests edge cases
- is fast
- is not alone

---

## How much testing is sufficient?

---

## Test coverage

<span class="accent">Coverage</span> is the percentage of your code that is
covered by tests.

There is no need to get 100% of coverage but it might help to identify sections
of your code that are not well tested.

Many big companies go for coverage in the ninety-ish area.

---

There are limits to what a unit test can do though...<br><br>
> “No amount of testing can prove a software right, a single test can prove a software wrong.”
> <br>\- Amir Ghahrai

---

Ok got it!

## But <span class="accent">how</span> do I write and execute unit tests?

---

![](assets/demo.jpg)

---

```bash
git clone https://github.com/pythondaymx/taller_testing
cd pytest_tutorial

pip install --user flask pytest pytest-cov  # or pip3 ...
pip install --user -e .
```

---

## Running pytest

Just running `py.test` in your package directory is ususall sufficient.

```shell
cdiener@pest [corda] py.test
=========================== test session starts ============================
platform linux -- Python 3.5.3, pytest-3.1.1, py-1.4.34, pluggy-0.4.0
rootdir: /home/cdiener/code/corda, inifile:
plugins: cov-2.4.0
collected 27 items

tests/test_large.py ......ss
tests/test_simple.py .......
tests/test_util.py ............

=================== 25 passed, 2 skipped in 1.25 seconds ===================
```

---

pytest will discover tests with the following rules:

- filename must start or end with "test"
- if the test is a function it also must start with "def test_"
- if the test is a class it should start with "class Test*`

---

If you have `pytest-cov` installed you can get coverage output using the
`--cov` flag.

```bash
py.test --cov=networker

# with HTML output
py.test --cov=networker --cov-report=html

# To see missed lines afterwards
# might be coverage3 on your system
coverage report -m
```

---

To exclude files from coverage reports add the following section to your
`setup.cfg` file.

```toml
[coverage:run]
omit = tests/*, */__main__.py
```

---

## Writing unit tests for pytest

---

A pytest unit test is simply a function that includes an `assert` statement.

```Python
def test_something():
    x = 2 + 3
    assert x > 2 and x > 3
    assert x == 5
```

---

## Fixtures and set up

A <span class="accent">fixture</span> is a function that creates a configured
object and can be <span class="accent">injected</span> into test functions.

```Python
import pytest
...

@pytest.fixture
def test_app():
    app = AppClass("option 1", value=3)
    app.secret_key = "test_key"
    app.validate()
    app.build_cache(2000)
    return app


def test_app(test_app):
    response = test_app.get("/rest/api/1234")
    assert response
```

---

Some cool builtin fixtures:

- `capsys`: capture output to stdout/stderr
- `monkeypatch`: modify/delete system functions temporarily
- `tmpdir`: creates temporary directories and files
- `benchmark`: high accuracy benchmarking (requires `pytest-benchmark`)

---

## Iterating over parameters

Sometimes we want to run a test with several different inputs.

```Python
import pytest

@pytest.mark.parametrize("string", ["name123", "123 456", "ab123cd"])
def test_find_123(string):
    assert "123" in string
```

---

## Checking for exceptions

Sometimes we expect code to raise an Exception.

```python
import pytest

def test_raises_error():
    with pytest.raises(ZeroDivisionError):
        a = 1/0
```

---

## Skipping tests conditionally

```python
import pytest

try:
    import numpy
except ImportError:
    numpy = False

@pytest.mark.skipif(numpy, reason="requires numpy")
def test_numpy_code() {
...
}
```

---

## Test coverage and CI

You can use https://travis-ci.org and http://codecov.io to generate coverage
reports from your builds.

```yaml
language: python
cache: pip
sudo: false

python:
    - 2.7
    - 3.5

before_install:
    - pip install -U pip
    - pip install -U pytest pytest-cov codecov

install:
    - pip install -e .

script:
    - py.test --cov=networker

after_success:
    - codecov
```

---

### Ok, we know pytest now 🎉

![](assets/pr_giphy.gif) <!-- .element: style="width: 80%;"-->

---

Questions/comments?
