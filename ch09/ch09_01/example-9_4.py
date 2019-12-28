"""
使用 inspect 获取函数参数

从被装饰的函数的参数提取需要的参数
"""
import functools
import inspect


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # 不必检查参数 username 是位置参数还是关键字参数
        func_args = inspect.getcallargs(f, *args, **kwargs)

        if func_args.get('username') != 'admin':
            raise Exception('This user is not allowed to get food')
        return f(*args, **kwargs)
    return wrapper


class Store(object):

    def __init__(self):
        self.storage = {}

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)
