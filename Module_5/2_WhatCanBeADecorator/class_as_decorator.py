# __call__ is used to set up what is called when the decoreated method is called

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print(f'Hello, {name}!')

hello('Ringo')
hello('Paul')
hello('George')
hello('John')
print(hello.count)

