"""
考虑这样一组方法，它们在被调用时检查“用户名”参数
"""


class Store(object):

    def __init__(self):
        self.storage = {}

    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('This user is not allowed to get food')
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception('This user is not allowed to put food')
        return self.storage.put(food)
