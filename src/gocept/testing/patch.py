# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt


class Patches(object):

    def __init__(self):
        self.attributes = []
        self.calls = []

    def set(self, subject, attribute, value):
        self.attributes.append(
            (subject, attribute, getattr(subject, attribute)))
        setattr(subject, attribute, value)

    def call(self, subject, attribute, old, new):
        self.calls.append(
            (subject, attribute, old))
        getattr(subject, attribute)(new)

    def reset(self):
        self._reset_attributes()
        self._reset_calls()
        self.__init__()

    def _reset_attributes(self):
        for subject, attribute, value in self.attributes:
            setattr(subject, attribute, value)

    def _reset_calls(self):
        for subject, attribute, value in self.calls:
            getattr(subject, attribute)(value)
