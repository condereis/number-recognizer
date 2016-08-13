#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'numpy',
    'pandas'
]



setup(
    name='number-recognizer',
    version='0.1.2',
    description="A software for the recognition of handwritten numbers.",
    long_description=readme + '\n\n' + history,
    author="Rafael Lopes Conde dos Reis",
    author_email='rafael.lcreis@gmail.com',
    url='https://github.com/condereis/number-recognizer',
    packages=[
        'recognizer',
    ],
    package_dir={'recognizer':
                 'recognizer'},
    entry_points={
        'console_scripts': [
            'recognizer=recognizer.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='recognizer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
