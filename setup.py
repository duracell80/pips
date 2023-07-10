from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Pips - The Speaking Clock'
LONG_DESCRIPTION = 'Inject a little retro timekeeping into a script with this speaking clock'

setup(
    name="pips",
    version=VERSION,
    author="Lee Jordan",
    author_email="<lee.jordan@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=['pips', 'pips.*']),
    install_requires=[
        "pyAudio>=0.2.13",
        "pysine>=0.9.2",
        "numpy>=1.23.2"
    ]
)
