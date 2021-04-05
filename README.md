# pycharm-demo

A simple Python / data science project for demonstrating PyCharm shortcuts. 

## Prerequisites

- Python3

## Setup

```shell script
# install project dependencies
bin/setup.sh
```

Configure your IDE to use the python virtual environment (`./.venv/`) created by `setup.sh` 
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Tasks that you can run

```shell script
# run unit tests
source .venv/bin/activate 
python -m unittest discover ./tests/
```
