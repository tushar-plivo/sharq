# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
from setuptools import setup

setup(
    name='SharQ',
    version='0.5.0',
    url='https://github.com/plivo/sharq',
    author='Plivo Team',
    author_email='hello@plivo.com',
    packages=['sharq'],
    package_data={
        'sharq': ['scripts/lua/*.lua']
    },
    license="The MIT License (MIT)",
    description='An API queueing system built at Plivo.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'redis==2.10.1',
        'msgpack-python==0.4.2',
        'rediscluster>=0.5.3'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
