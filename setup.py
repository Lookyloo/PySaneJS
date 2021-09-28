#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup  # type: ignore


setup(
    name='pysanejs',
    version='1.6-dev',
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    maintainer='Raphaël Vinot',
    url='https://github.com/CIRCL/sanejs/client',
    description='Python client for SaneJS',
    packages=['pysanejs'],
    install_requires=['requests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet',
    ]
)
