# py-readabilitiy-metrics

Scores text usings a variety of _readability_ scores including: Flesch-Kincaid Grade Level, Flesch Reading Ease, and more

## Install

```shell
pip install py-readability-metrics
```

## Usage

```python
from readability import Readability

 r = Readability(text)
 print(r.flesch_kincaid())
 print(r.flesch())
```

### Flesch-Kincaid Grade Level

method:

```python
r.flesch_kincaid()
```

returns:

```python
Result(
    score, # float
    grade_level # string
)
```

### Flesch Reading Ease

method:

```python
r.flesch()
```

returns:

```python
Result(
    score, # float
    ease, # string
    grade_levels, # list<str>
)
```

## Contributing

[see contributing](CONTRIBUTING.md)

## License

[MIT](LICENSE)
