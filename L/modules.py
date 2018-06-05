# /usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'zhin'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world')
    elif len(args) == 2:
        print('hello, {}'.format(args[1]))
    else:
        print('too many arguments')


if __name__ == '__main__':
    test()


def make_pizza(size, *toppings):
    """制作pizza"""
    print(
        '\nMaking a {} -inch pizza with the following toppings:'.format(size))
    for topping in toppings:
        print('- {}'.format(topping))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def named_kw(name, age, *, city, job):
    """命名关键词参数，city，job"""
    print(name, age, city, job)


named_kw('zhin', '28', city='shanghai', job='manong')


def named_kw_args(name, age, *args, city, job):
    """命名关键字参数+可变参数"""
    print(name, age, args, city, job)


named_kw_args('zhin', 28, 'lala', 'until', city='shanghai', job='musyoku')


def f1(a, b, c=0, *args, **kw):
    """必选参数，默认参数，可变参数，关键字参数"""
    pass


def f2(a, b, c=0, *, d, **kw):
    """必选参数，默认参数，命名关键字参数，关键字参数"""
    pass