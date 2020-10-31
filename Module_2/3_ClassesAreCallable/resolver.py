import socket

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host): # this makes a class callable
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

print(Resolver) # this is a Class object, not instance object
r = Resolver() # init is called, classes are invokable

