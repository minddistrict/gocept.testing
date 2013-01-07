# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

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
        with self.assertRaises(AssertionError):
            self.check_files(self.tmpdir)

    def test_fails_if_target_file_is_older(self):
        self.touch('foo.min.js')
        time.sleep(0.02)
        self.touch('foo.js')
        with self.assertRaises(AssertionError):
            self.check_files(self.tmpdir)
