# py-readability-metrics

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

text = ... # a text containing 100 or more words

r = Readability(text)
print(r.flesch_kincaid())
print(r.flesch())
print(r.gunning_fog())
print(r.coleman_liau())
```

### Flesch-Kincaid Grade Level

**method:**

```python
r.flesch_kincaid()
```

**returns:**

```python
Result(
    score, # float
    grade_level # string
)
```

### Flesch Reading Ease

**method:**

```python
r.flesch()
```

**returns:**

```python
Result(
    score, # float
    ease, # string
    grade_levels, # list<str>
)
```

### Coleman Liau Index

**method:**

```python
r.coleman_liau()
```

**returns:**

```python
Result(
    score, # float
    grade_level # string
)
```

### Gunning Fog

**method:**

```python
r.gunning_fog()
```

**returns:**

```python
Result(
    score, # float
    grade_level, # str
)
```

## Contributing

[see contributing](CONTRIBUTING.md)

## License

[MIT](LICENSE)
