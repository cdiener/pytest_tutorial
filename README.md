[![Build Status](https://travis-ci.org/cdiener/pytest_tutorial.svg?branch=complete)](https://travis-ci.org/cdiener/pytest_tutorial)
[![Code Coverage](https://codecov.io/gh/cdiener/pytest_tutorial/branch/complete/graph/badge.svg)](https://codecov.io/gh/cdiener/pytest_tutorial)

The talk presented at PythonDay 2017 can be found interactively at
https://pythondaymx.github.io/taller_testing or as PDF in [talk.pdf](talk.pdf).

No te asustes que la presentación es en inglés. La plática es en español 😅.

# Example project for pytest tutorial

This example project implements a small app named "networker" that can draw
force layouts for a directory of JSON graphs.

## Installation

### Requirements

**Software**:

- Python >=2.7.11 or >3.3
- pip >= 8.1
- a recent web browser
- Optional: git, virtualenv

**Abilities that will help you**:

- know how to use your Terminal (changing directories, executing scripts)
- basic Python (functions, imports, decorators)

### Optional: set up a virtual environment

**For Python 2**:

```bash
pip install virtualenv
cd <tutorial folder>
pyvenv env
source env/bin/activate
```

**For Python 3**:

```bash
cd <tutorial folder>
python3 -m venv env
source env/bin/activate
```

### Install pytest and the package in developer mode

Run the following in the tutorial folder.

```bash
# May be pip3 on your system
pip install --user pytest pytest-cov
pip install --user -e .
```

## Try the app

Run the app in the tutorial folder with

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
