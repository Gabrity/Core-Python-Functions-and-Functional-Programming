g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l)
    inner()

outer()
# invalid, inner does not exist only when outer is executed
#outer.inner()