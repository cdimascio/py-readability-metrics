# Contributing

### Make change

### Create/update tests

### Run tests

```shell
python -m unittest discover -v
```

### Package

```shell
python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
