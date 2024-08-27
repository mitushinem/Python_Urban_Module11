import inspect
import math
import pprint
import random


def func(a, *, b: int, **kwargs):
    pass


class MyClass:

    def __init__(self):
        self.attr = 2

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def func(self):
        pass


def introspection_info(obj):
    res = dict()
    res['type'] = str(type(obj)).split('\'')[1]
    res['magic_method'] = [i[0] for i in inspect.getmembers(obj, inspect.ismethod(obj)) if i[0].startswith('__')]
    res['method'] = [i[0] for i in inspect.getmembers(obj, inspect.ismethod(obj)) if not i[0].startswith('__')]
    res['module'] = inspect.getmodule(obj)

    return res


if __name__ == '__main__':
    number_info = introspection_info(['1', '2', '3'])
    print(number_info)

    number_info = introspection_info('func')
    print(number_info)

    number_info = introspection_info(MyClass)
    print(number_info)

    number_info = introspection_info(func)
    print(number_info)
