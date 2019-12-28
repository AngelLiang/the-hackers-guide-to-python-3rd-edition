"""
示例9.1 注册装饰器
"""

_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'
