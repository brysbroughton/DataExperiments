from setuptools import setup, find_packages

with open('requirements.txt', mode='r', encoding='utf8') as f:
    requirements = f.read().splitlines()

setup(
    name="mypackage",
    version='0.1',
    packages=find_packages(),
    install_requires=requirements
)