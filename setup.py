#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="django_bend",
    description="Database dump conversion to Django fixtures",
    version="0.0.6",
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
    ],
    keywords='django fixture database dump',
    packages=find_packages(exclude=['tests','tests.*','*.tests','*.tests.*']),
    install_requires=[
        'simplejson>=3.8.0',
    ],
)
