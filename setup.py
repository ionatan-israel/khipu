from setuptools import setup, find_packages
from src.khipu.version import __version__ as version


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
    version=version,
)
