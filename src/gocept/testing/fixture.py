import tempfile
import shutil


class TempDir(object):

    def setUp(self):
        super(TempDir, self).setUp()
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        super(TempDir, self).tearDown()
        shutil.rmtree(self.tmpdir)
