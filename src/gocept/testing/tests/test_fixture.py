import gocept.testing.fixture
import os.path
import unittest


class TempDirTest(gocept.testing.fixture.TempDir, unittest.TestCase):
    """Testing ..fixture.TempDir."""

    def setUp(self):
        super().setUp()
        with open(os.path.join(self.tmpdir, 'foo'), 'w') as f:
            f.write('bar')

    def test_aaa_directory_is_created_in_setUp(self):
        with open(os.path.join(self.tmpdir, 'foo')) as f:
            self.assertEqual('bar', f.read())
        with open(os.path.join(self.tmpdir, 'bar'), 'w') as f:
            f.write('qux')

    def test_bbb_directory_is_removed_in_tearDown(self):
        self.assertFalse(os.path.isfile(os.path.join(self.tmpdir, 'bar')))
