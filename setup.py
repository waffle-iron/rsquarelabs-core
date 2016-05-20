#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'rrmerugu'


from distutils.core import setup
from setuptools import find_packages

readme = open('README.txt').read()

setup(name='rsquarelabs-core',
version='0.0.5dev3',
description='This is the library of automation pipeline modules developed at RSQUARE LABS.',
long_description= readme,
author='Ravi RT Merugu',
author_email='rrmerugu@gmail.com',
url = 'http://github.com/rsquarelabs/rsquarelabs-core',
packages = find_packages(),
package_data={'rsquarelabs_core.websuite.static' : ['*']},
install_requires=['bottle','termcolor','requests'],
keywords = ['Computational Biology', 'Molecular Modelling', 'Bioinformatics', 'Automation'])