# Contributing

### Make change

### Create/update tests

### Run tests

```shell
python -m unittest discover -v
```

### Package

```shell
rm -rf build dist py_readability_metrics.egg-info/
python setup.py sdist bdist_wheel
twine upload dist/*
```
