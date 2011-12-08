==============
gocept.testing
==============

This package collects various helpers for writing tests.


assertEllipsis
==============

An assertion which is very helpful when using Testbrowser with
unittest.TestCase (instead of doctests).

Some examples::

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