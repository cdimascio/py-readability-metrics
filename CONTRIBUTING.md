# Contributing

## How To

1. Fork the repo
2. Make a change
3. Create and/or update tests
4. Run tests and ensure they pass

```shell
python -m unittest discover -v
```

5. Submit a PR

## Packaging

Contributors should ignore the steps below.

```shell
rm -rf build dist py_readability_metrics.egg-info && python setup.py sdist bdist_wheel 
twine upload dist/*
```
