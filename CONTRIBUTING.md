# 🚧 Contributing

![Travis Build](https://travis-ci.org/cdimascio/py-readability-metrics.svg?branch=master) ![Python](https://img.shields.io/badge/python-%203.4%20%7C%203.5%20%7C%203.6-blue.svg) [![Documentation Status](https://readthedocs.org/projects/py-readability-metrics/badge/?version=latest)](https://py-readability-metrics.readthedocs.io/en/latest/?badge=latest) [![wheel](https://img.shields.io/badge/wheel-yes-ff00c9.svg)](https://pypi.org/project/py-readability-metrics/) [![](https://img.shields.io/gitter/room/cdimascio-oss/community?color=%23eb205a)](https://gitter.im/cdimascio-oss/community)
 [![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://lbesson.mit-license.org/)
 
## How To

Need help? Reach out on [gitter](https://gitter.im/cdimascio-oss/community)

### Prequisites

1. Install deps
```
pip install .
python -m nltk.downloader punkt
```

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

Prequisites:
1. Install Sphinx

```shell
pip install -U sphinx m2r
```

Modify Documentation

1. Fork the repo
2. Navigate to `docs`
3. Make a change
4. Rebuild docs

   ```shell
   make html
   open build/html/index.html # open index.html for review in browser
   ```

## Publish docs

Contributors should ignore the steps below.

1. Login to https://readthedocs.org/
2. Run build

## Package

Contributors should ignore the steps below.

Prerequisites:

```shell
pip install twine
```

publish 

```shell
rm -rf build dist py_readability_metrics.egg-info && python setup.py sdist bdist_wheel
twine upload dist/*
```
