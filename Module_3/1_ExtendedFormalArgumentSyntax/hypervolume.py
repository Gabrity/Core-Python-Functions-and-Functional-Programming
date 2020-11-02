# this * can only go to the end of the argument list 
# there can be only of of these
# only collects positional arguments

#arguments can be: positional or keyword arguments

# lengths will be passed as a tuple
def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

print(hypervolume(3))
print(hypervolume(3, 2))
