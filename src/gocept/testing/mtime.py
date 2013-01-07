# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import os.path
import datetime


class Newer(object):

    source_ext = NotImplemented
    target_ext = NotImplemented
    message = NotImplemented

    # SVN seems to use the check-in time as mtime, which can cause a difference
    # of up to 3 seconds
    delta = 3

    def check_files(self, path):
        os.path.walk(path, self._check_files_in_list, None)

    def _check_files_in_list(self, args, path, names):
        for filename in names:
            # Exclude target_ext in the source_ext
            if filename.endswith(self.target_ext):
                continue
            if not filename.endswith(self.source_ext):
                continue
            if filename.startswith('_'):
                continue
            target_filename = filename.replace(
                self.source_ext, self.target_ext)
            filepath = os.path.join(path, filename)
            target_path = os.path.join(path, target_filename)

            self.assertTrue(
                os.path.exists(target_path),
                "%s does not exist.\n%s" % (target_filename, self.message))
            target_mtime = os.path.getmtime(target_path)
            file_mtime = os.path.getmtime(filepath)
            delta = file_mtime - target_mtime
            self.assertTrue(
                delta < self.delta,
                "%s is out of date: %s (%s) > %s (%s), Delta: %s.\n%s" % (
                    target_path, self.to_str(file_mtime), filename,
                    self.to_str(target_mtime), target_filename,
                    delta, self.message))

    @staticmethod
    def to_str(mtime):
        return datetime.datetime.fromtimestamp(mtime).strftime(
            '%Y-%m-%dT%H:%M:%S')
