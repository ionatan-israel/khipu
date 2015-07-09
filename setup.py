#!/usr/bin/env python
from setuptools import setup, find_packages

exec(open("facebook/version.py").read())

setup(
    name='khipu',
    version=__version__,
    description='A client for the khipu API.',
    author='Jonatan Rodriguez',
    author_email='jrperdomoz@gmail.com',
    maintainer='Jonatan Rodriguez',
    maintainer_email='jrperdomoz@gmail.com',
    url='https://github.com/jrperdomoz/khipu',
    license="BSD",
    packages=['khipu'],
    # long_description=open("README.md").read(),
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Programming Language :: Python :: 2.7'
        # 'License :: OSI Approved :: Apache Software License',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
    ],
    install_requires=[
        'requests',
    ],
    keywords='khipu chile',
)
