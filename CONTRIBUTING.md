# 🚧 Contributing

## How To

### Code

1. Fork the repo
2. Make a change
3. Create and/or update tests
4. Run tests and ensure they pass

```shell
python -m unittest discover -v
```

5. Submit a PR

### Tips: Implmementing a new scorer

All scorers follow a very similar implementation pattern: 
_The following use [ARI](https://github.com/cdimascio/py-readability-metrics/blob/master/readability/scorers/ari.py) as an example_
- each scorer lives in the [scorers](https://github.com/cdimascio/py-readability-metrics/blob/master/readability/scorers) directory  
- each scorer has a [constructor](https://github.com/cdimascio/py-readability-metrics/blob/master/readability/scorers/ari.py#L17) that takes `statistics` and is registered [here](https://github.com/cdimascio/py-readability-metrics/blob/master/readability/readability.py#L11). 
- each scorer implements a method `score` and returns a `Result`. See [ARI](https://github.com/cdimascio/py-readability-metrics/blob/master/readability/scorers/ari.py#L16) for an example
- each scorer provides a test(s) in [test/test_readability](https://github.com/cdimascio/py-readability-metrics/blob/master/test/test_readability.py#L13)

### Docs

1. Fork the repo
2. Navigate to `docs`
3. Make a change
4. Rebuild docs

   ```shell
   make html
   open build/html/index.html # open index.html for review in browser
   ```

## Package

Contributors should ignore the steps below.

```shell
rm -rf build dist py_readability_metrics.egg-info && python setup.py sdist bdist_wheel
twine upload dist/*
```
