# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import difflib
import doctest


class Ellipsis(object):
    """Assertion helper that provides doctest-style ellipsis matching.

    Inherit from this class in additition to unittest.TestCase.
    """

    def assertEllipsis(self, expected, actual):
        # normalize whitespace
        norm_expected = ' '.join(expected.split())
        norm_actual = ' '.join(actual.split())
        if doctest._ellipsis_match(norm_expected, norm_actual):
            return True
        # report ndiff
        engine = difflib.Differ(charjunk=difflib.IS_CHARACTER_JUNK)
        diff = list(engine.compare(expected.splitlines(True),
                                   actual.splitlines(True)))
        kind = 'ndiff with -expected +actual'
        diff = [line.rstrip() + '\n' for line in diff]
        self.fail('Differences (%s):\n' % kind + ''.join(diff))

    def assertNotEllipsis(self, expected, actual):
        try:
            self.assertEllipsis(expected, actual)
        except AssertionError:
            pass
        else:
            self.fail('Value unexpectedly matches expression %r.' % expected)


class Exceptions(object):

    def assertNothingRaised(self, callable=None, *args, **kw):
        context = AssertNothingRaisedContext(self)
        if callable is None:
            return context
        with context:
            callable(*args, **kw)


class AssertNothingRaisedContext(object):

    def __init__(self, test_case):
        self.failureException = test_case.failureException

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is None:
            return True
        raise self.failureException('Exception raised: ' + repr(exc_value))
