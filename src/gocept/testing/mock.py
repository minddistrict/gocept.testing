from unittest import mock


class Patches:

    def __init__(self):
        self.patches = []

    def add(self, *args, **kw):
        patch = mock.patch(*args, **kw)
        self.patches.append(patch)
        return patch.start()

    def add_object(self, *args, **kw):
        patch = mock.patch.object(*args, **kw)
        self.patches.append(patch)
        return patch.start()

    def add_dict(self, *args, **kw):
        patch = mock.patch.dict(*args, **kw)
        self.patches.append(patch)
        return patch.start()

    def reset(self):
        for patch in self.patches:
            patch.stop()
        self.patches[:] = []


class Assertions:

    def assertCalledWith(self, mock, *args, **kw):
        return mock.assert_called_with(*args, **kw)


class Property(mock.Mock):

    def __get__(self, instance, class_):
        return self()


class PatchHelper:

    def setUp(self):
        super().setUp()
        self.patches = Patches()

    def tearDown(self):
        self.patches.reset()
        super().tearDown()
