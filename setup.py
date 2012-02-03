# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages


setup(
    name='gocept.testing',
    version='1.3.1',
    author='Wolfgang Schnerring <ws at gocept dot com>',
    author_email='ws@gocept.com',
    url='https://code.gocept.com/hg/public/gocept.testing',
    description="""\
A collection of test helpers, additional assertions, and the like.
""",
    long_description=(
        open('README.txt').read()
        + '\n\n'
        + open('CHANGES.txt').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    namespace_packages=['gocept'],
    install_requires=[
        'setuptools',
    ],
    extras_require=dict(test=[
        'mock',
        'six',
    ]),
)
