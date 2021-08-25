import shutil
import tempfile


class TempDir:
    """Offer a temporary directory."""

    def setUp(self):
        super().setUp()
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        super().tearDown()
        shutil.rmtree(self.tmpdir)
