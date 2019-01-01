#!/user/bin/env python

from setuptools import setup, find_packages

setup(
    name='py-readability-metrics',
    version='0.1.6',
    author='Carmine DiMAscio',
    author_email='cdimascio@gmail.com',
    description='Calculate readability scores. e.g. Flesch, Flesch-Kincaid, and more',
    url='https://github.com/cdimascio/py-readability-metrics',
    keywords="readability metrics text difficulty grade level",
    packages=find_packages(),
    license='MIT',
    install_requires=[
         'nltk'
    ]
)
