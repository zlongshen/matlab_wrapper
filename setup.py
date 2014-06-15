#!/usr/bin/python

from setuptools import setup,find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(
    name = "matlab_wrapper",
    version = "0.2",
    author = "Marek Rudnicki",
    author_email = "marekrud@gmail.com",

    description = "MATLAB wrapper",
    license = "GPLv3",
    url = "https://github.com/mrkrd/matlab_wrapper",

    packages = find_packages(),
    long_description = long_description,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],

    platforms = ["Linux"],
    install_requires=["numpy"],
)
