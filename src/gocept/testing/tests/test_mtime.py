import gocept.testing.assertion
import gocept.testing.fixture
import gocept.testing.mtime
import os.path
import time
import unittest


class NewerTest(gocept.testing.fixture.TempDir,
                gocept.testing.assertion.Exceptions,
                gocept.testing.mtime.Newer,
                unittest.TestCase):

    source_ext = '.js'
    target_ext = '.min.js'
    delta = 0.01

    def touch(self, filename):
        open(os.path.join(self.tmpdir, filename), 'w').close()

    def test_passes_if_target_file_is_newer(self):
        self.touch('foo.js')
        self.touch('foo.min.js')
        with self.assertNothingRaised():
            self.check_files(self.tmpdir)

    def test_fails_if_target_file_is_missing(self):
        self.touch('foo.js')
        self.assertRaises(AssertionError, self.check_files, self.tmpdir)

    def test_fails_if_target_file_is_older(self):
        self.touch('foo.min.js')
        time.sleep(1)
        self.touch('foo.js')
        self.assertRaises(AssertionError, self.check_files, self.tmpdir)

    def test_mtime__Newer__4(self):
        """It ignores files starting with underscore and raises nothing."""
        self.touch('_foo.js')
        with self.assertNothingRaised():
            self.check_files(self.tmpdir)

    def test_mtime__Newer__5(self):
        """It ignores files which do not end with source_ext."""
        self.touch('foo.jsx')
        with self.assertNothingRaised():
            self.check_files(self.tmpdir)
