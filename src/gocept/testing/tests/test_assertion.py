# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import unittest
import gocept.testing.assertion


class EllipsisTest(unittest.TestCase, gocept.testing.assertion.Ellipsis):

    def test_match_found_nothing_happens(self):
        # assert nothing is raised
        self.assertEllipsis('...bar...', 'foo bar baz')

    def test_no_match_found_fails(self):
        try:
            self.assertEllipsis('foo', 'bar')
        except AssertionError, e:
            self.assertEqual(
                'Differences (ndiff with -expected +actual):\n- foo\n+ bar\n',
                str(e))
        else:
            self.fail('nothing raised')

    def test_unicode_matches_encoded(self):
        # assert nothing is raised
        self.assertEllipsis(u'...bar...', u'foo bar baz'.encode('utf-8'))

    def test_encoded_matches_unicode(self):
        # assert nothing is raised
        self.assertEllipsis(u'...bar...'.encode('utf-8'), u'foo bar baz')

    def test_inverse_assertion(self):
        # assert nothing is raised
        self.assertNotEllipsis('foo', 'bar')

        try:
            self.assertNotEllipsis('...bar...', 'foo bar baz')
        except AssertionError, e:
            self.assertEqual(
                "Value unexpectedly matches expression '...bar...'.",
                str(e))
        else:
            self.fail('nothing raised')


class ExceptionsTest(unittest.TestCase, gocept.testing.assertion.Exceptions):

    def add(self, *args):
        self.sum = sum(args)

    def provoke(self):
        raise RuntimeError('provoked')

    def test_no_exception_passes(self):
        self.assertNothingRaised(lambda: self.add(5, 5))
        self.assertEqual(10, self.sum)

    def test_exception_raised_fails(self):
        try:
            self.assertNothingRaised(self.provoke)
        except AssertionError, e:
            self.assertEqual(
                'AssertionError("Exception raised: '
                'RuntimeError(\'provoked\',)",)',
                repr(e))
        else:
            self.fail('Nothing raised')

    def test_usable_as_context_manager(self):
        with self.assertNothingRaised():
            self.add(5, 5)
        self.assertEqual(10, self.sum)

    def test_context_manager_failure_case(self):
        try:
            with self.assertNothingRaised():
                self.provoke()
        except AssertionError, e:
            self.assertEqual(
                'AssertionError("Exception raised: '
                'RuntimeError(\'provoked\',)",)',
                repr(e))
        else:
            self.fail('Nothing raised')
