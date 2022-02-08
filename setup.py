from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='ba_ex',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Examples using ArcGIS Business Analyst with Python.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
