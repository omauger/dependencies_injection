from setuptools import setup

setup(
    name='Dependencies Injection',
    url='https://github.com/omauger/dependencies_injection',
    author='Ophélie Mauger',
    packages=['dependencies_injection'],
    install_requires=[
        'inject==3.3.*'
    ],
    version='0.1',
    license='MIT',
    description='A module to implement easily dependencies injection in python project.',
)