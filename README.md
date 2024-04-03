# 📗 py-readability-metrics
![Travis Build](https://travis-ci.org/cdimascio/py-readability-metrics.svg?branch=master) ![Python](https://img.shields.io/badge/python-3.x-blue.svg) [![Documentation Status](https://readthedocs.org/projects/py-readability-metrics/badge/?version=latest)](https://py-readability-metrics.readthedocs.io/en/latest/?badge=latest) [![wheel](https://img.shields.io/badge/wheel-yes-ff00c9.svg)](https://pypi.org/project/py-readability-metrics/) [![](https://img.shields.io/gitter/room/cdimascio-oss/community?color=%23eb205a)](https://gitter.im/cdimascio-oss/community) [![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
 [![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://lbesson.mit-license.org/)

Score the _readability_ of text using popular readability formulas and metrics including: [Flesch Kincaid Grade Level](#flesch-kincaid-grade-level), [Flesch Reading Ease](#flesch-reading-ease), [Gunning Fog Index](#gunning-fog), [Dale Chall Readability](#dale-chall-readability), [Automated Readability Index (ARI)](#automated-readability-index-ari), [Coleman Liau Index](#coleman-liau-index), [Linsear Write](#linsear-write), [SMOG](#smog), [SPACHE](#spache) and [Lix](#lix). 📗

[![GitHub stars](https://img.shields.io/github/stars/cdimascio/py-readability-metrics.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/cdimascio/py-readability-metrics/stargazers/) [![Twitter URL](https://img.shields.io/twitter/url/https/github.com/cdimascio/py-readability-metrics.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20py-readability-metrics%20by%20%40CarmineDiMascio%20https%3A%2F%2Fgithub.com%2Fcdimascio%2Fpy-readability-metrics%20%F0%9F%91%8D)


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
r.dale_chall()
r.ari()
r.linsear_write()
r.smog()
r.spache()
r.lix()
```

**\*Note:** `text` must contain >= 100 words\*

## Supported Metrics

- [Flesch Kincaid Grade Level](#flesch-kincaid-grade-level)
- [Flesch Reading Ease](#flesch-reading-ease)
- [Dale Chall Readability](#dale-chall-readability)
- [Automated Readability Index (ARI)](#automated-readability-index-ari)
- [Coleman Liau Index](#coleman-liau-index)
- [Gunning Fog](#gunning-fog)
- [SMOG](#smog)
- [Spache](#spache)
- [Linsear Write](#linsear-write)
- [Lix](#lix)

## Readability Metric Details and Properties

All metrics provide a `score` attribute. Indvidual metrics provide additional properties to increased interpretability. See details below to capture per metric details.

_Note:_ In all examples below `r` is:

```python
r = Readability(text)
```

### Flesch-Kincaid Grade Level

The U.S. Army uses Flesch-Kincaid Grade Level for assessing the difficulty of technical manuals. The commonwealth of Pennsylvania uses Flesch-Kincaid Grade Level for scoring automobile insurance policies to ensure their texts are no higher than a ninth grade level of reading difficulty. Many other U.S. states also use Flesch-Kincaid Grade Level to score other legal documents such as business policies and financial forms.

**_call:_**

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

**_call:_**

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

**_call:_**

```python
r.dale_chall()
```

**_example:_**

```python
dc = r.dale_chall()
print(dc.score)
print(dc.grade_levels)
```

### Automated Readability Index (ARI)

Unlike the other indices, the ARI, along with the Coleman-Liau, relies on a factor of characters per word, instead of the usual syllables per word. ARI is widely used on all types of texts.

**_call:_**

```python
r.ari()
```

**_example:_**

```python
ari = r.ari()
print(ari.score)
print(ari.grade_levels)
print(ari.ages)
```

### Coleman Liau Index

The Coleman-Liau Formula usually gives a lower grade value than any of the Kincaid, ARI and Flesch values when applied to technical documents.

**_call:_**

```python
r.coleman_liau()
```

**_example:_**

```python
cl = r.coleman_liau()
print(cl.score)
print(cl.grade_level)
```

### Gunning Fog

The Gunning fog index measures the readability of English writing. The index estimates the years of formal education needed to understand the text on a first reading. A fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old).

**_call:_**

```python
r.gunning_fog()
```

**_example:_**

```python
gf = r.gunning_fog()
print(gf.score)
print(gf.grade_level)
```

### SMOG

The SMOG Readability Formula (Simple Measure of Gobbledygook) is a popular method to use on health literacy materials.

**_call:_**

```python
r.smog()
```

**_example:_**

```python
s = r.smog()
print(s.score)
print(s.grade_level)
```

The original SMOG formula uses a sample of 30 sentences from the original text. However, the formula can be generalized to any number of sentences. You can use the generalized formula by passing the `all_sentences=True` argument to `smog()`

**_call:_**

```python
r.smog(all_sentences=True)
```

**_example:_**

```python
s = r.smog(all_sentences=True)
print(s.score)
print(s.grade_level)
```

### SPACHE

The Spache Readability Formula is used for Primary-Grade Reading Materials, published in 1953 in The Elementary School Journal. The Spache Formula is best used to calculate the difficulty of text that falls at the 3rd grade level or below. 

**_call:_**

```python
r.spache()
```

**_example:_**

```python
s = r.spache()
print(s.score)
print(s.grade_level)
```

### Linsear Write

Linsear Write is a readability metric for English text, purportedly developed for the United States Air Force to help them calculate the readability of their technical manuals.

**_call:_**

```python
r.linsear_write()
```

**_example:_**

```python
lw = r.linsear_write()
print(lw.score)
print(lw.grade_level)
```

### Lix

Lix (abbreviation of Swedish läsbarhetsindex, "readability index") is a readability measure for Scandinavian and West European languages developed by Carl-Hugo Björnsson. It is defined as the sum of average sentence length and the percentage of words with more than six letters. 

**_call:_**

```python
r.lix()
```

**_example:_**

```python
s = r.lix()
print(s.score)
print(s.ease)
```

## [Contributing](CONTRIBUTING.md)

Contributions are welcome!

## References

- [Readability Formulas](http://readabilityformulas.com/)

## License

[MIT](LICENSE)

<a href="https://www.buymeacoffee.com/m97tA5c" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/rbamos"><img src="https://avatars1.githubusercontent.com/u/49767442?v=4" width="100px;" alt=""/><br /><sub><b>rbamos</b></sub></a><br /><a href="https://github.com/cdimascio/py-readability-metrics/commits?author=rbamos" title="Code">💻</a> <a href="https://github.com/cdimascio/py-readability-metrics/commits?author=rbamos" title="Tests">⚠️</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
