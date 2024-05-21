from setuptools import find_packages
from setuptools import setup


setup(
    name='gocept.testing',
    version='4.0',
    author='minddistrict <mail at minddistrict dot com>',
    author_email='mail@minddistrict.com',
    url='https://github.com/minddistrict/gocept.testing',
    description="""\
A collection of test helpers, additional assertions, and the like.""",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    long_description=(open('README.rst').read() + '\n\n' +
                      open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    keywords="testing unittest assertions",
    namespace_packages=['gocept'],
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
    ],
)
