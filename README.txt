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


Development
===========

The source code is available in the mercurial repository at
https://code.gocept.com/hg/public/gocept.testing

Please report any bugs you find at
https://projects.gocept.com/projects/projects/gocept-testing/issues
