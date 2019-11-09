#!/usr/bin/python3
# coding:UTF8
#---------Library-------------------------#
from setuptools import setup
#-----------------------------------------#

with open ("README.md", "r") as fileR :
    description_library  = fileR.read()


setup (
    name = "test_technique",
    version = "1.0",
    description = "Un package python permettant d’enregistrer et consulter des évènements liés à des dates.",
    license='MIT',
    long_description = description_library,
    url = "https://github.com/AnselmeChans/storage.git",
    author_email = "anselmeceril@gmail.fr",
    keywords='storage event source date',
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Developper',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
     ],
    install_requires = ["setuptools","datetime"],
    package_data = {
        '': ['*.gz', '*.tbi'],
        },
)
