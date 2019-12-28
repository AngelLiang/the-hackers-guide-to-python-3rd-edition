"""
第一步：分离出检查部分代码
"""


def check_is_admin(username):
    if username != 'admin':
        raise Exception('This user is not allowed to get food')


class Store(object):

    def __init__(self):
        self.storage = {}

    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)
