Changelog
=========

4.1 (unreleased)
----------------

- Nothing changed yet.


4.0 (2024-05-21)
----------------

Backwards incompatible changes
++++++++++++++++++++++++++++++

- Drop support for Python 3.7, 3.8.

Features
++++++++

- Add support for Python 3.11, 3.12 and 3.13 (as of beta 1).


3.0 (2021-08-26)
----------------

Backwards incompatible changes
++++++++++++++++++++++++++++++

- Change license form ZPL to MIT.

- Drop support for Python 2, 3.4, 3.5 and 3.6

Features
++++++++

- Add support for Python 3.8, 3.9 and 3.10 (as of rc.1).


2.0.post1 (2018-11-22)
----------------------

- Fix PyPI page rendering.


2.0 (2018-11-22)
----------------

- Drop Python 2.6 an 3.3 support.

- Add support for Python 3.6, 3.7, PyPy and PyPy3.

- Choose explicit ``[mock]`` extra to use ``gocept.testing.mock`` on Python <
  3.3.


1.11 (2016-01-18)
-----------------

- Fix homepage URL.

- Declare Python 3.4 and Python 3.5 support.

- Drop Python 3.2 support.


1.10.1 (2014-04-28)
-------------------

- Make ``assertNotEllipsis()`` compatible with `py.test`.

- Declare Python 3.3 support.


1.10 (2014-02-13)
-----------------

- Remove ``retry`` decorator, it is rather useless since it does not take
  setUp/tearDown into account.


1.9 (2013-12-20)
----------------

- Add ``retry`` decorator that runs flaky tests several times and only fails
  when they fail each time.

- Use py.test instead of zope.testrunner for this package's own tests.


1.8 (2013-07-17)
----------------

- Python 3 compatibility.
- Depend on setuptools rather than distribute now that the projects have
  merged.
- Use current buildout and recipes for development.


1.7 (2013-04-18)
----------------

- Fix Python-2.6 compatibility of our own test suite.
- Introduce ``PatchHelper``.


1.6.0 (2013-01-07)
------------------

- Add newer mtime check.


1.5.2 (2012-09-14)
------------------

- ``.patch.Dict`` did not restore the keys if an exception occured while the
  `with` call.


1.5.1 (2012-09-12)
------------------

- Fixed documentation and faulty 1.5 release.


1.5 (2012-07-10)
----------------

- Add ``.patch.Dict``, a dict patching context manager.


1.4 (2012-06-04)
----------------

- Add ``TempDir`` fixture.
- Add ``assertStartsWith``, ``assertEndsWith``.


1.3.2 (2012-05-09)
------------------

- Allow ``assertEllipsis`` to work with mixed unicode/bytes argument
  (assuming the bytes are UTF-8, as they are with zope.testbrowser).


1.3.1 (2012-02-03)
------------------

- Display original traceback in ``assertNothingRaised``.


1.3 (2011-12-16)
----------------

- Add patch helper for attributes and simple callables.


1.2.1 (2011-12-09)
------------------

- Make Python-3 compatible (at least syntactically).


1.2 (2011-12-09)
----------------

- Add Patches context for mock (upstream implementation pending,
  see <http://code.google.com/p/mock/issues/detail?id=30>)
- Add ``assertCalledWith``.
- Add ``mock.Property``.


1.1 (2011-11-10)
----------------

- Add ``assertNothingRaised``.


1.0 (2011-11-02)
----------------

- first release: ``assertEllipsis``
