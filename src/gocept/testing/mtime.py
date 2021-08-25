import datetime
import os
import os.path


class Newer:

    source_ext = NotImplemented
    target_ext = NotImplemented
    message = NotImplemented

    # SVN seems to use the check-in time as mtime, which can cause a difference
    # of up to 3 seconds
    delta = 3

    def check_files(self, path):
        for root, dirs, files in os.walk(path):
            self._check_files_in_list(root, dirs + files)

    def _check_files_in_list(self, path, names):
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
                f"{target_filename} does not exist.\n{self.message}")
            target_mtime = os.path.getmtime(target_path)
            file_mtime = os.path.getmtime(filepath)
            delta = file_mtime - target_mtime
            self.assertTrue(
                delta < self.delta,
                "{} is out of date: {} ({}) > {} ({}), Delta: {}.\n{}".format(
                    target_path, self.to_str(file_mtime), filename,
                    self.to_str(target_mtime), target_filename,
                    delta, self.message))

    @staticmethod
    def to_str(mtime):
        return datetime.datetime.fromtimestamp(mtime).strftime(
            '%Y-%m-%dT%H:%M:%S')
