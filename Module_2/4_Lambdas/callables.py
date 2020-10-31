import socket

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host): # this makes a class callable
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

def is_even(x):
    return x % 2 == 0
print(f'Regular methods are callable: {callable(is_even)}')

is_odd = lambda x: x % 2 == 1
print(f'Lambdas are callable: {callable(is_odd)}')

print(f'Methods are callable: {callable(list.append)}')

resolver = Resolver()
print(f'Instance objects are callable if __call__ is implemented: {callable(resolver)}')

print(f'Some objects, like string instances are callable: {callable("I am callable?")}')


