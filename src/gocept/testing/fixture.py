import shutil
import tempfile


class TempDir(object):
    """Offer a temporary directory."""

    def setUp(self):
        super(TempDir, self).setUp()
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        super(TempDir, self).tearDown()
        shutil.rmtree(self.tmpdir)
