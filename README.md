# py-readability-metrics

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Score the _readability_ of text using popular readability metrics including: Flesch-Kincaid Grade Level, Flesch Reading Ease, Gunning Fog and more

<p align="center">
 <img src="https://raw.githubusercontent.com/cdimascio/py-readability-metrics/master/assets/py-readability-metrics.png" width="500"></>
</p>

## Install

```shell
pip install py-readability-metrics
python -m nltk.downloader punkt
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

**\*Note:** `text` must contain >= 100 words\*

## Details

In all examples below `r` is:

```python
r = Readability(text)
```

### Flesch-Kincaid Grade Level

The U.S. Army uses Flesch-Kincaid Grade Level for assessing the difficulty of technical manuals. The commonwealth of Pennsylvania uses Flesch-Kincaid Grade Level for scoring automobile insurance policies to ensure their texts are no higher than a ninth grade level of reading difficulty. Many other U.S. states also use Flesch-Kincaid Grade Level to score other legal documents such as business policies and financial forms.

**_method:_**

```python
r.flesch_kincaid()
```

**_example:_**

```python
fk = r.flesch_kincaid()
print(fk.score)
print(fk.grade_level)
```

### Flesch Reading Ease

The U.S. Department of Defense uses the Reading Ease test as the standard test of readability for its documents and forms. Florida requires that life insurance policies have a Flesch Reading Ease score of 45 or greater.

**_method:_**

```python
r.flesch()
```

**_example:_**

```python
f = r.flesch()
print(f.score)
print(f.ease)
print(f.grade_levels)
```

### Dale Chall Readability

The Dale-Chall Formula is an accurate readability formula for the simple reason that it is based on the use of familiar words, rather than syllable or letter counts. Reading tests show that readers usually find it easier to read, process and recall a passage if they find the words familiar.

**_method:_**

```python
r.dale_chall	()
```

**_example:_**

````python
cl = dale_chall()
print(cl.score)
print(cl.grade_levels)

### Coleman Liau Index

The Coleman-Liau Formula usually gives a lower grade value than any of the Kincaid, ARI and Flesch values when applied to technical documents.

**_method:_**

```python
r.coleman_liau()
````

**_example:_**

```python
cl = r.coleman_liau()
print(cl.score)
print(cl.grade_level)
```

### Gunning Fog

the Gunning fog index measures the readability of English writing. The index estimates the years of formal education needed to understand the text on a first reading. A fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old).

**_method:_**

```python
r.gunning_fog()
```

**_example:_**

```python
gf = r.gunning_fog()
print(gf.score)
print(gf.grade_level)
```

## [Contributing](CONTRIBUTING.md)

Contributions are welcome!

## License

[MIT](LICENSE)
