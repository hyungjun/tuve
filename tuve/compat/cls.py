from tuve.compat import PY3

if PY3:
    from functools import singledispatch
    func = lambda f: f
else:
    from singledispatch import singledispatch
    func = lambda f: f.im_func
