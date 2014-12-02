#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='Online judge',
    version='0.1.0',
    description='Compile and run programs written in any language and check results',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Grzegorz Parka',
    author_email='grzegorz.parka@gmail.com',
    url='https://github.com/parkag/Online-judge',
    packages=[
        'online-judge',
    ],
    package_dir={'oj': 'oj'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='tester',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
