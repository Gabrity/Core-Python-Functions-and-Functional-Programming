# decorators allow you to change existing functions without changing their definition
# you do not need to update the callers
# decorator is a wrapper around the method it decorates


def escape_unicode(f, *arg, **kwarg):
    def wrap(*arg, **kwarg):
        x = f(*arg, **kwarg)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Nyíregyháza'

print(northern_city())
