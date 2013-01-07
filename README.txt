==============
gocept.testing
==============

This package collects various helpers for writing tests.

.. contents:: :depth: 1


assertEllipsis
==============

An assertion which is very helpful when using Testbrowser with
unittest.TestCase (instead of doctests).

Some examples::

    class MyTest(unittest.TestCase, gocept.testing.assertion.Ellipsis):
    # [...]


    self.assertEllipsis('...bar...', 'foo bar qux')
    # -> nothing happens

    self.assertEllipsis('foo', 'bar')
    # -> AssertionError: Differences (ndiff with -expected +actual):
         - foo
         + bar

    self.assertNotEllipsis('foo', 'foo')
    # -> AssertionError: "Value unexpectedly matches expression 'foo'."

To use, inherit from ``gocept.testing.assertion.Ellipsis`` in addition to
``unittest.TestCase``.


assertStartsWith, assertEndsWith
================================

::

    class MyTest(unittest.TestCase, gocept.testing.assertion.String):

        def test_something(self):
            self.assertStartsWith('foo', 'foobar') # --> pass
            self.assertEndsWith('bar', 'foobar') # --> pass
            self.assertStartsWith('qux', 'foobar') # --> fail
            self.assertEndsWith('qux', 'foobar') # --> fail


assertNothingRaised
===================

The opposite of assertRaises(), this is an assertion that makes some tests more
readable. As assertRaises(), it can be used as as context manager, too::

    class MyTest(unittest.TestCase, gocept.testing.assertion.Exceptions):
    # [...]

    self.assertNothingRaised(do_something, 1, 2, 3)

    with self.assertNothingRaised():
        do_something(1, 2, 3)


mock patch context
==================

``gocept.testing.mock.Patches`` collects `mock`_ patches that are valid for the
whole TestCase, and resets them all in one go in tearDown (this is pending
incluion upstream as ``mock.patcher()``, see `issue 30`_)::

    class MyTest(unittest.TestCase):

        def setUp(self):
            self.patches = gocept.testing.mock.Patches()

        def tearDown(self):
            self.patches.reset()

        def test_something(self):
            compile = self.patches.add('re.compile')

It offers three methods:

:add: wraps ``mock.patch()``
:add_object: wraps ``mock.patch.object``
:add_dict: wraps ``mock.patch.dict``

Note that ``gocept.testing`` does not declare a dependency on ``mock`` to be as
lightweight as possible, so clients need to do that themselves.


.. _`mock`: http://www.voidspace.org.uk/python/mock/
.. _`issue 30`: http://code.google.com/p/mock/issues/detail?id=30


assertCalledWith
================

This is syntactic sugar around ``mock.assert_called_with``, so you can write::

    class MyTest(unittest.TestCase, gocept.testing.mock.Assertions):

        def test_something(self):
            dummy = mock.Mock()
            dummy(True)
            self.assertCalledWith(dummy, True)

instead of::

    dummy.assert_called_with(True)


Mocking properties
==================

``gocept.testing.mock.Property`` is syntactic sugar directly lifted from the
`mock documentation`_ that allows you to patch properties like this::

    class Dummy(object):

        @property
        def foo(self):
            return False


    with mock.patch('Dummy.foo', gocept.testing.mock.Property()) as foo:
        foo.return_value = 'something else'


.. _`mock documentation`: http://www.voidspace.org.uk/python/mock/examples.html


Attribute patch context
=======================

This has nothing to do with mocks, it's a convenience helper for setting and
automatically resetting attributes of objects::

    class MyTest(unittest.TestCase):

        def setUp(self):
            self.patches = gocept.testing.patch.Patches()
            self.subject = MyClass()

        def tearDown(self):
            self.patches.reset()

        def test_something(self):
            self.assertEqual('one', self.subject.foo)
            self.patches.set(self.subject, 'foo', 'two')
            self.assertEqual('two', self.subject.foo)


Method call patch context
=========================

This allows to call a method and reset it later on automatically. At the
moment, only methods that take a single parameter are supported, by passing in
both the old value (to which it should be reset) and the new value::

    class MyTest(unittest.TestCase):

        def setUp(self):
            self.patches = gocept.testing.patch.Patches()

        def tearDown(self):
            self.patches.reset()

        def test_something(self):
            self.patches.call(
                zope.component.hooks, 'setSite',
                zope.component.hooks.getSite(), new_site)


Dict patching context manager
=============================

``gocept.testing.patch.Dict`` is a context manager allowing to change values
in a dict. It restores the original dict at exit. E. g. it can be used to
temporarily change values in ``os.environ``::

    >>> with gocept.testing.patch.Dict(os.environ, foo='bar', qwe='asdf'):
            print os.environ.get('foo')
    bar
    >>> print os.environ.get('foo')
    None


Temporary directory
===================

``gocept.testing.fixture.TempDir`` encapsulates the common pattern to create a
temporary directory and delete it after the test has run. The name of the
directory is avaliable as ``self.tmpdir``. Note that since
``unittest.TestCase`` does not call `super`, you need to mix in ``TempDir``
first::

    class MyTest(gocept.testing.fixture.TempDir, unittest.TestCase):

        def test_something(self):
            self.assertTrue(os.path.isdir(self.tmpdir))


Comparing mtimes
================

``gocept.testing.mtime.Newer`` checks that generated files are at least as new
as their source counterparts (similar like ``make`` works)::

    class MyTest(gocept.testing.mtime.Newer, unittest.TestCase):

        source_ext = '.js'
        target_ext = '.min.js'
        message = 'run jsmin to correct this'

        def test_minified_js_files_are_younger_than_non_minified_ones(self):
            self.check_files(pkg_resources.resource_filename(
                'my.package', 'resources/js'))


Development
===========

The source code is available in the mercurial repository at
https://code.gocept.com/hg/public/gocept.testing

Please report any bugs you find at
https://projects.gocept.com/projects/projects/gocept-testing/issues
