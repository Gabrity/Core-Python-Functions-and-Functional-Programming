def trace(f, *args, **kwargs):
    print(args)
    print(kwargs)
    result = f(*args, **kwargs)
    print('result=', result)
    return result

trace(int, 'ff', base=16)