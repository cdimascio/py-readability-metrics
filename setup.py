#!/user/bin/env python

from setuptools import setup

setup(
    name='py-readability-metrics',
    version='0.1.1',
    description='Calculate readability scores. e.g. Flesch, Flesch-Kincaid, and more',
    author='Carmine DiMAscio',
    url='https://github.com/cdimascio/py-readability-metrics',
    packages=['readability'],
    install_requires=['nltk'],
    package_data={'readability': [], '': ['README.md', 'LICENSE']},
    package_dir={'readabiliity': 'readabiliity'},
    include_package_data=True,
    author_email='cdimascio@gmail.com',
    license='MIT',
    zip_safe=False,
)
