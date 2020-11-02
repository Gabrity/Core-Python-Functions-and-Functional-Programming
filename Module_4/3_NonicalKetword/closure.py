# global keyword reaches up to the global scope
# nonlocal keyword binds from the enclosing scope to the local namespace
# how it works: it searches the enclosing scopes from inner to outer and uses the first match

message='global'
def enclosing():
    message = 'enclosing'
    def local():
        nonlocal message
        message='local'
    
    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)

