from tuve.compat import PY3

if PY3:
    unicode = str
else:
    unicode = unicode

def format(fmt, *args, **kwargs):
    return unicode(fmt).format(*args, **kwargs)
