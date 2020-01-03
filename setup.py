from setuptools import setup, find_packages


setup(
    name='gocept.testing',
    version='2.1.dev0',
    author='gocept <mail at gocept dot com>',
    author_email='mail@gocept.com',
    url='https://github.com/gocept/gocept.testing',
    description="""\
A collection of test helpers, additional assertions, and the like.""",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    long_description=(
        open('README.rst').read()
        + '\n\n'
        + open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    keywords="testing unittest assertions",
    namespace_packages=['gocept'],
    install_requires=[
        'setuptools',
    ],
    extras_require=dict(
        test=[
            'mock ; python_version<"3.3"',
        ],
        mock=[
            'mock ; python_version<"3.3"',
        ],
    ),
)
