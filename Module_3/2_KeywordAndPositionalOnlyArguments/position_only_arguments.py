# arguments after / can only be positional
# useful to have parity with modules implemented in other languages
# or in apis if you don't want users to depend on keys

#can only be used from python 3.8
def number_length(x, /):
    return len(str(x))

print(number_length(2112))