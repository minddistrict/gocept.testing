# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import functools
import sys


def retry(count=3):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kw):
            error = None
            for i in range(count):
                try:
                    func(*args, **kw)
                except Exception:
                    error = sys.exc_info()[1]
                else:
                    return
            raise error
        return inner
    return decorator
