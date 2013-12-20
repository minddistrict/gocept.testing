# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

from gocept.testing import retry
import pytest


def test_passing_test_is_run_only_once():
    runs = []

    @retry()
    def test():
        runs.append(True)
    test()
    assert 1 == len(runs)


def test_first_time_passing_counts_as_passed():
    runs = []

    @retry()
    def test():
        runs.append(True)
        if len(runs) == 1:
            assert False
    test()
    assert 2 == len(runs)


def test_always_failing_counts_as_failed():
    runs = []

    @retry(5)
    def test():
        runs.append(True)
        assert False
    with pytest.raises(AssertionError):
        test()
    assert 5 == len(runs)


def test_decorator_preserves_function_name():

    @retry()
    def test():
        pass
    assert 'test' == test.__name__
