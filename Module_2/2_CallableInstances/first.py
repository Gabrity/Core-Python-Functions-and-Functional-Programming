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

r = Resolver()
print(r.has_host('pluralsight.com'))
r('pluralsight.com')
print(r.has_host('pluralsight.com'))
print(r._cache)
r('pluralsight.com') # quicker call, since it was cached already
