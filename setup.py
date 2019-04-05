import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-sql-explorer-moni",
    version='moni_version',
    author="Chris Clark",
    author_email="chris@untrod.com",
    description=("A pluggable app that allows users (admins) to execute SQL,"
                 " view, and export the results."),
    license="MIT",
    keywords="django sql explorer reports reporting csv database query",
    url="https://github.com/moni-team/django-sql-explorer",
    packages=['moni-explorer'],
    long_description=read('README.rst'),
    classifiers=[
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'Django>=1.7.0',
        'sqlparse>=0.1.18',
        'unicodecsv>=0.14.1',
        'six>=1.10.0',
    ],
    include_package_data=True,
    zip_safe=False,
)
