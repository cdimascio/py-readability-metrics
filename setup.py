#!/user/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py-readability-metrics',
    version='0.13.1',
    author='Carmine DiMAscio',
    author_email='cdimascio@gmail.com',
    description='Calculate readability scores. e.g. Flesch, Flesch-Kincaid, and more',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cdimascio/py-readability-metrics',
    keywords="readability metrics text difficulty grade level",
    packages=find_packages(exclude=['tests']),
    license='MIT',
    install_requires=[
         'nltk'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
