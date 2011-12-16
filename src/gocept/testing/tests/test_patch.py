# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.testing.assertion
import gocept.testing.patch
import mock
import unittest


class PatchTest(unittest.TestCase, gocept.testing.assertion.Exceptions):

    def test_changes_attribute_and_resets(self):
        patches = gocept.testing.patch.Patches()
        subject = mock.Mock()
        subject.foo = mock.sentinel.foo
        patches.set(subject, 'foo', mock.sentinel.bar)
        self.assertEqual(mock.sentinel.bar, subject.foo)
        patches.reset()
        self.assertEqual(mock.sentinel.foo, subject.foo)

    def test_callable_attribute_called_and_reset(self):
        class Dummy(object):
            def foo(self, arg):
                self.arg = arg

        patches = gocept.testing.patch.Patches()
        subject = Dummy()
        subject.foo(mock.sentinel.foo)
        self.assertEqual(mock.sentinel.foo, subject.arg)
        patches.call(subject, 'foo', mock.sentinel.foo, mock.sentinel.bar)
        self.assertEqual(mock.sentinel.bar, subject.arg)
        patches.reset()
        self.assertEqual(mock.sentinel.foo, subject.arg)

    def test_multiple_reset_does_no_harm(self):
        patches = gocept.testing.patch.Patches()
        subject = mock.Mock()
        subject.foo = mock.sentinel.foo
        patches.set(subject, 'foo', mock.sentinel.bar)
        self.assertEqual(mock.sentinel.bar, subject.foo)
        patches.reset()
        self.assertEqual(mock.sentinel.foo, subject.foo)
        with self.assertNothingRaised():
            patches.reset()
        self.assertEqual(mock.sentinel.foo, subject.foo)
