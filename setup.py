#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

setup(
    name='django-logstash-logger',
    version='0.0.1',
    description='Simple logstash-compatible log handler for Django-based projects',
    url='https://github.com/astrikov-d/django-logstash-logger',
    packages=['django_logstash_logger'],
    license='Apache License 2.0',
    author='Dmitry Astrikov',
    author_email='astrikov.d@gmail.com',
    install_requires=['pytz', 'django'],
    tests_require=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
