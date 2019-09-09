# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

    
'''This is we were supposed to add a licence to the project    
with open('LICENSE') as f:
    license = f.read()
'''

setup(
    name='BEAT',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Team 10',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=('tests', 'docs'))
)

