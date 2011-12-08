# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from __future__ import absolute_import
import gocept.testing.mock
import mock
import sys
import unittest


# for use in the test
something = mock.sentinel.Something
something_else = mock.sentinel.SomethingElse

PTModule = sys.modules[__name__]


class PatcherTest(unittest.TestCase):

    def test_add_should_patch_dotted_name_and_return_mock(self):
        patches = gocept.testing.mock.Patches()
        patched = patches.add(
            '%s.something' % __name__, mock.sentinel.Something2)
        self.assertEqual(mock.sentinel.Something2, patched)
        patches.add('%s.something_else' % __name__, mock.sentinel.Something3)

        self.assertEqual(PTModule.something, mock.sentinel.Something2,
                         "reseted")
        self.assertEqual(PTModule.something_else, mock.sentinel.Something3,
                         "reseted")
        patches.reset()
        self.assertEqual(PTModule.something, mock.sentinel.Something,
                         "patch not restored")
        self.assertEqual(PTModule.something_else, mock.sentinel.SomethingElse,
                         "patch not restored")

    def test_add_object_should_delegate_to_patch_object(self):
        patches = gocept.testing.mock.Patches()
        subject = mock.Mock()
        subject.foo = mock.sentinel.Something
        patches.add_object(subject, 'foo', mock.sentinel.Something2)
        self.assertEqual(subject.foo, mock.sentinel.Something2, "unpatched")
        patches.reset()
        self.assertEqual(
            subject.foo, mock.sentinel.Something, "patch not restored")

    def test_add_dict_should_delegate_to_patch_dict(self):
        patches = gocept.testing.mock.Patches()
        subject = {}
        subject['key'] = mock.sentinel.Something
        patches.add_dict(subject, {'key': mock.sentinel.Something2})
        self.assertEqual(subject['key'], mock.sentinel.Something2, "unpatched")
        patches.reset()
        self.assertEqual(subject['key'], mock.sentinel.Something,
                         "patch not restored")

    def test_reset_multiple_times_does_no_harm(self):
        patches = gocept.testing.mock.Patches()
        subject = mock.Mock()
        subject.foo = mock.sentinel.Something
        patches.add_object(subject, 'foo', mock.sentinel.Something2)
        self.assertEqual(subject.foo, mock.sentinel.Something2, "unpatched")
        patches.reset()
        self.assertEqual(
            subject.foo, mock.sentinel.Something, "patch not restored")
        patches.reset()
        self.assertEqual(
            subject.foo, mock.sentinel.Something, "patch not restored")


class AssertionTest(unittest.TestCase, gocept.testing.mock.Assertions):

    def test_should_delegate_to_mock_method(self):
        dummy = mock.Mock()
        dummy(True)
        self.assertCalledWith(dummy, True)


class Dummy(object):

    @property
    def foo(self):
        return False


class PropertyTest(unittest.TestCase):

    def test_usable_to_patch_property(self):
        dummy = Dummy()
        with mock.patch('gocept.testing.tests.test_mock.Dummy.foo',
                        gocept.testing.mock.Property()) as foo:
            foo.return_value = True
            self.assertTrue(dummy.foo)
