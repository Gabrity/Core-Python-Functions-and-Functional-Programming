# def binds the function name to a function object (body)
# so far have seen module level functions and class methods
# local functions are just local name bindings in the function body
# local functions are similar to lambdas, but more general

# local funcions are defined when def is executed
# a new instance of the local function is made for all enclosing invocation
# it is bound each time when it is called
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    print(last_letter)
    return sorted(strings, key= last_letter)

sort_by_last_letter(['ghi','def','abc'])
sort_by_last_letter(['ghi','def','abc'])
sort_by_last_letter(['ghi','def','abc'])

# returning local functions
def enclosing():
    def local():
        print('local')
    return local

lf = enclosing()
lf()