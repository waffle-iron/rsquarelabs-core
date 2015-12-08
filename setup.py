#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'rrmerugu'


from distutils.core import setup

readme = open('README.txt').read()

setup(name='rsquarelabs',
version='0.0.4',
description='This is the library of automation pipeline modules developed at RSQUARE LABS.',
long_description= readme,
author='Ravi RT Merugu',
author_email='rrmerugu@gmail.com',
url = 'http://github.com/rsquarelabs/rsquarelabs',
packages = ['rsquarelabs', 'rsquarelabs.gromacs', 'rsquarelabs.jmol'],
keywords = ['Computational Biology', 'Molecular Modelling', 'Bioinformatics', 'Automation'])