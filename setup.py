import os.path

from setuptools import setup, find_packages


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
            return f.read()
    except (IOError, OSError):
        pass


version = '0.0.1a'

setup(
    name='manmail',
    version=version,
    packages=find_packages(exclude=['example.py']),
    description='Send e-mail, easier',
    long_description=readme(),
    url='https://github.com/nerogit/manmail',
    author='Dohyeon Kim',
    author_email='nero.union12' '@' 'gmail.com',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Email',
    ]
)
