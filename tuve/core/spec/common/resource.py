class Resource(str):
    @property
    def as_rlist(self):
        return Resources([self])

class Resources(list):
    def __str__(self):
        return '/'.join(self)

