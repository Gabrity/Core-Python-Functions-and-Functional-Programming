# **kwargs lets us pass arbitrary amount of named parameters as a dictionary

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k = key, v = str(value))
    result += '>'
    return result

print(tag("Monet", scr = 'Monet.jpg', alt = 'Sunrise by Claude Monet', border = 1))
#<Monet scr="Monet.jpg" alt="Cunrise by Claude Monet" border="1">


# invalid definition in this order:
#def print_args(**kwargs, *args):


# everything before args are taken as positional arguments
def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)
print_args(1,2,3,4,5)


# any arguments after args must be manadorty keyword arguments
def print_args2(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
print_args2(1,2,3,4,5, kwarg1 = 6, kwarg2 = 7)


# not passing kwargs is an error
#print_args2(1,2,3,4,5, kwarg1 = 6, 7)


# using * defines all arguments following it as positional arguments
def name_tag(first_name, last_name, *, title = ''):
    print(title, first_name, last_name)
name_tag('Kirk', 'Tiberius', title='Galactic Commander')


# last argument must be **kwargs
def print_args3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)
print_args3(1, 2, 3, 4, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)
#1
#2
#(3, 4)
#6
#7
#{'kwarg3': 8, 'kwarg4': 9}

