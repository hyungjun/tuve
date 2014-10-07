import sys

if sys.version_info.major == 3:
    PY2, PY3 = False, True
else:
    PY2, PY3 = True, False
