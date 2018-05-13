#!/usr/bin/python3
import sys

print('Hello, World')
if True:
    print('true')
else:
    print('else')

print('---------------------python import mode-------------------------')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print('----------python3 基本数据类型-----------------')
counter = 100
miles = 1000.00
name = 'zhin'

print(counter, miles, name)

dict = {}
dict['one'] = 1
dict[2] = 2
dict['2'] = '2'
print(dict)

list1 = list('bbbbbb')
print(list1)
set1 = set(list1)
print(set1)
print(ord('1'))