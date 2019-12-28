def identity(f):
    return f


@identity
def foo():
    return 'bar'


def foo2():
    return 'bar'


foo2 = identity(foo2)
