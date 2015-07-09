#!/usr/bin/env python
from setuptools import setup, find_packages
exec(open("src/version.py").read())

setup(
    name='khipu',
    author='Jonatan Rodriguez',
    author_email='jrperdomoz@gmail.com',
    description='A client for the khipu API.',
    include_package_data=True,
    install_requires=['requests>=2.7.0'],
    keywords='khipu chile',
    license="BSD",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jrperdomoz/khipu',
    version=__version__
)
