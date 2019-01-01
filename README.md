# py-readability-metrics

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Score the _readability_ of text using popular readability metrics including: Flesch-Kincaid Grade Level, Flesch Reading Ease, Gunning Fog and more

<p align="center">
 <img src="https://raw.githubusercontent.com/cdimascio/py-readability-metrics/master/assets/py-readability-metrics.png" width="500"></>
</p>

## Install

```shell
pip install py-readability-metrics
```

## Usage

```python
from readability import Readability

r = Readability(text)

r.flesch_kincaid()
r.flesch()
r.gunning_fog()
r.coleman_liau()
```

***Note:** `text` must contain >= 100 words*

## Details

In all examples below `r` is:

```python
r = Readability(text)
```

### Flesch-Kincaid Grade Level

***method:***

```python
r.flesch_kincaid()
```

***example:***

```python
fk = r.flesch_kincaid()
print(fk.score)
print(fk.grade_level)
```


### Flesch Reading Ease

***method:***

```python
r.flesch()
```

***example:***

```python
f = r.flesch()
print(f.score)
print(f.ease)
print(f.grade_levels)
```

### Coleman Liau Index

***method:***

```python
r.coleman_liau()
```

***example:***

```python
cl = r.coleman_liau()
print(cl.score)
print(cl.grade_level)
```


### Gunning Fog

***method:***

```python
r.gunning_fog()
```

***example:***

```python
gf = r.gunning_fog()
print(gf.score)
print(gf.grade_level)
```


## [Contributing](CONTRIBUTING.md)

Contributions are welcome!

## License

[MIT](LICENSE)
