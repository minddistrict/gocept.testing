import contextlib


class Patches:
    # XXX Maybe this should be a context manager, too.

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


@contextlib.contextmanager
def Dict(dict, **changes):
    """Patch a dict with new keys and restore it at exit."""
    # XXX Maybe `Patches` should be able to do this, too.
    orig = dict.copy()
    dict.update(changes)
    try:
        yield
    finally:
        dict.clear()
        dict.update(orig)
