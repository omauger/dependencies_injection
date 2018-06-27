from setuptools import setup

setup(
    name='dependencies-injection',
    url='https://github.com/omauger/dependencies_injection',
    author='Ophélie Mauger',
    packages=['dependencies_injection'],
    install_requires=[
        'inject==3.3.*'
    ],
    extras_require={
        'ci': ['flake8', 'coverage'],
    },
    version='1.0',
    license='MIT',
    description='A module to implement easily dependencies injection in python project.',
)