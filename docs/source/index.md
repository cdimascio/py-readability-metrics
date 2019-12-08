# py-readability-metrics

[![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://lbesson.mit-license.org/) ![Python](https://img.shields.io/badge/python-%203.4%20%7C%203.5%20%7C%203.6-blue.svg)
.. image:: https://img.shields.io/badge/wheel-yes-ff00c9.svg
    :target: https://pypi.org/project/py-readability-metrics/
    :alt: wheel

Score the _readability_ of text using popular readability metrics including: [Flesch Kincaid Grade Level](#flesch-kincaid-grade-level), [Flesch Reading Ease](#flesch-reading-ease), [Gunning Fog Index](#gunning-fog), [Dale Chall Readability](#dale-chall-readability), [Automated Readability Index (ARI)](#automated-readability-index-ari), [Coleman Liau Index](#coleman-liau-index), [Lisnear Write](#linsear-write), and [SMOG](#smog)

<p align="center">
 <img src="https://raw.githubusercontent.com/cdimascio/py-readability-metrics/master/assets/py-readability-metrics.png" width="500"></>
</p>

## Install

.. code-block:: shell

    pip install py-readability-metrics
    python -m nltk.downloader punkt

## Usage

Here is some text explaining some complicated stuff

.. code-block:: python

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

## Readability Metrics

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    flesch
    flesch_kincaid
    dale_chall
    ari
    coleman_liau
    gunning_fog
    smog
    spache
    linsear_write

# Indices and tables

- :ref:`genindex`
- :ref:`modindex`
- :ref:`search`
