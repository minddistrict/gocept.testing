from gocept.testing.mock import mock
import gocept.testing.assertion
import gocept.testing.patch
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
        class Dummy:
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


class DictTests(unittest.TestCase):
    """Testing ..patch.Dict."""

    def test_stores_keys_in_given_dict(self):
        import gocept.testing.patch
        dict = {}
        with gocept.testing.patch.Dict(dict, foo='bar'):
            self.assertEqual({'foo': 'bar'}, dict)

    def test_overwrites_existing_keys_in_dict(self):
        import gocept.testing.patch
        dict = {'foo': 'qwe'}
        with gocept.testing.patch.Dict(dict, foo='bar'):
            self.assertEqual({'foo': 'bar'}, dict)

    def test_removes_previously_not_existing_key_from_dict(self):
        import gocept.testing.patch
        dict = {}
        with gocept.testing.patch.Dict(dict, foo='bar'):
            pass
        self.assertEqual({}, dict)

    def test_restores_keys_on_exit(self):
        import gocept.testing.patch
        dict = {'foo': 'qwe'}
        with gocept.testing.patch.Dict(dict, foo='bar'):
            pass
        self.assertEqual({'foo': 'qwe'}, dict)

    def test_restores_keys_on_exit_if_exception_occurred_inside_with(self):
        import gocept.testing.patch
        dict = {'foo': 'qwe'}
        try:
            with gocept.testing.patch.Dict(dict, foo='bar'):
                raise RuntimeError()
        except RuntimeError:
            pass
        self.assertEqual({'foo': 'qwe'}, dict)
