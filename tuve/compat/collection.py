from tuve.compat import PY3

if PY3:
    items = lambda mapping: mapping.items()
else:
    items = lambda mapping: mapping.viewitems()
