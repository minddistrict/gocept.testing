# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.testing.fixture
import os.path
import unittest


class TempDirTest(gocept.testing.fixture.TempDir, unittest.TestCase):

    def setUp(self):
        super(TempDirTest, self).setUp()
        open(os.path.join(self.tmpdir, 'foo'), 'w').write('bar')

    def test_aaa_directory_is_created_in_setUp(self):
        self.assertEqual('bar', open(os.path.join(self.tmpdir, 'foo')).read())
        open(os.path.join(self.tmpdir, 'bar'), 'w').write('qux')

    def test_bbb_directory_is_removed_in_tearDown(self):
        self.assertFalse(os.path.isfile(os.path.join(self.tmpdir, 'bar')))
