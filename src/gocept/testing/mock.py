# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from __future__ import absolute_import

try:
    import mock
except ImportError:
    # soft dependency
    pass


class Patches(object):

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


class Assertions(object):

    def assertCalledWith(self, mock, *args, **kw):
        return mock.assert_called_with(*args, **kw)


class Property(mock.Mock):

    def __get__(self, instance, class_):
        return self()
