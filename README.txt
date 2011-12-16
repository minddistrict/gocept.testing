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
both the new value and the old value (to which it should be reset)::

    class MyTest(unittest.TestCase):

        def setUp(self):
            self.patches = gocept.testing.patch.Patches()

        def tearDown(self):
            self.patches.reset()

        def test_something(self):
            self.patches.call(
                zope.component.hooks, 'setSite',
                my_site, zope.component.hooks.getSite())



Development
===========

The source code is available in the mercurial repository at
https://code.gocept.com/hg/public/gocept.testing

Please report any bugs you find at
https://projects.gocept.com/projects/projects/gocept-testing/issues
