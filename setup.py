# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='alchemist',
    version='1.0.0',
    description='A Java code generation tool',
    long_description=readme,
    author='Wembley G. Leach, Jr.',
    author_email='wembley.gl@gmail.com',
    url='https://github.com/WemGL/alchemist',
    license=license,
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    entry_points={
        'console_scripts': ['alchemist-java=alchemist.core:main']
    }
)
