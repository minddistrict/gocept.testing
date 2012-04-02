import sys
exec(open('bootstrap1.py' if sys.version_info[0] == 2 else 'bootstrap2.py').read())
