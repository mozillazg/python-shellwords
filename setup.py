#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import shellwords

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

packages = [
    'shellwords',
]


def long_description():
    readme = open('README.rst', encoding='utf8').read()
    text = readme + '\n\n' + open('CHANGELOG.rst', encoding='utf8').read()
    return text

setup(
    name=shellwords.__title__,
    version=shellwords.__version__,
    description=shellwords.__doc__,
    long_description=long_description(),
    url='https://github.com/mozillazg/python-shellwords',
    author=shellwords.__author__,
    author_email='mozillazg101@gmail.com',
    license=shellwords.__license__,
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'shellwords': 'shellwords'},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    keywords='shell, shellwords',
)
