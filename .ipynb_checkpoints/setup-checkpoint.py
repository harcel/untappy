#!/usr/bin/env python

from distutils.core import setup

long_description = open('README').read()

setup(
    name='untappy',
    version="0.1",
    py_modules = ['untappy'],
    description='A python library to wrap the Untappd.com API',
    author='Marcel Haas',
    author_email='datascience@marcelhaas.com',
    license='BSD 2 Clause',
    url='http://github.com/harcel/pythonUntappd',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 2 Clause',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
