# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import difflib
import doctest
import sys
import traceback


def text(arg):
    if sys.version_info < (3,):
        return arg
    if not isinstance(arg, str):
        arg = arg.decode('utf-8')
    return arg


class Ellipsis(object):
    """Assertion helper that provides doctest-style ellipsis matching.

    Inherit from this class in additition to unittest.TestCase.
    """

    def assertEllipsis(self, expected, actual):
        expected = text(expected)
        actual = text(actual)
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
            self.fail(
                'Value unexpectedly matches expression %r.' % expected)


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
        exc_name = exc_type.__name__
        message = (
            'Unexpectedly raised %s, original traceback follows:\n'
            % exc_name)
        # cut off "Traceback: (most recent call last)" and the original
        #  message, since we're printing that ourselves
        stack = ''.join(
            traceback.format_exception(exc_type, exc_value, tb)[1:-1])
        text = message + stack + 'Unexpected %s: %s' % (exc_name, exc_value)
        raise self.failureException(text)
