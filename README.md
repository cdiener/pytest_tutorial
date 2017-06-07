[![Build Status](https://travis-ci.org/cdiener/pytest_tutorial.svg?branch=complete)](https://travis-ci.org/cdiener/pytest_tutorial)
[![Code Coverage](https://codecov.io/gh/cdiener/pytest_tutorial/branch/complete/graph/badge.svg)](https://codecov.io/gh/cdiener/pytest_tutorial)

The talk presented at PythonDay 2017 can be found in [talk.pdf](talk.pdf).

No te asustes que la presentación es en inglés. La platicá sería en español 😅.

# Example project for pytest tutorial

This example project implements a small app named "networker" that can draw
force layouts for a directory of JSON graphs.

## Installation

### Optional: set up a virtual environment

**For Python 2**:

```bash
pip install virtualenv
cd pytest_tutorial
pyvenv env
source env/bin/activate
```

**For Python 3**:

```bash
cd pytest_tutorial
python3 -m venv env
source env/bin/activate
```

### Install pytest and the package in developer mode

Run the following in the `pytest_tutorial` folder.

```bash
# May be pip3 on your system
pip install --user pytest pytest-cov
pip install --user -e .
```

## Try the app

Run the app in the `pytest_tutorial` folder with

```bash
# may be python3 on your system
python -m networker
```

Open your browser at https://localhost:5000/miserables and check whether you
see the graph.

In total the app has the following routes:

- `/<filename>` - create the graph for the file `<filename>` (you can omit the extension)
- `/json/<filename>` - get the JSON from a file `<filename>`
- `/validate/<filename>` - check whether `<filename>` contains a valid JSON graph
