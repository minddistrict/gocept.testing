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
