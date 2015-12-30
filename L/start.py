Python 3.4.0 (v3.4.0:04f714765c13, Mar 15 2014, 23:02:41) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list([1, 2, 3, 4])
[1, 2, 3, 4]
>>> ''.join('hello')
'hello'
>>> x = [1, 2, 3]
>>> x[1] = 3;
>>> x
[1, 3, 3]
>>> names =['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
>>> del names[2]
>>> names
['Alice', 'Beth', 'Dee-Dee', 'Earl']
>>> name = list('Perl')
>>> name[1:2]
['e']
>>> name[1:1]
[]
>>> name
['P', 'e', 'r', 'l']
>>> name[1:] = list('ython')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name[1:] = []
>>> name
['P']
>>> name[1:] = list('ython')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name[::2] = []
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[::2] = []
ValueError: attempt to assign sequence of size 0 to extended slice of size 3
>>> name[::2]
['P', 't', 'o']
>>> name[::2] = list['abc']
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[::2] = list['abc']
TypeError: 'type' object is not subscriptable
>>> name[::2] = 'a'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name[::2] = 'a'
ValueError: attempt to assign sequence of size 1 to extended slice of size 3
>>> name[::2] = ['a']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name[::2] = ['a']
ValueError: attempt to assign sequence of size 1 to extended slice of size 3
>>> name[::2] = ['a', 'b', 'c']
>>> name
['a', 'y', 'b', 'h', 'c', 'n']
>>> list['abc']
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list['abc']
TypeError: 'type' object is not subscriptable
>>> name[::2] = list('Pto')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name[::2] = list('PP')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[::2] = list('PP')
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
>>> name[::-2]
['n', 'h', 'y']
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name + ['m']
['P', 'y', 't', 'h', 'o', 'n', 'm']
>>> name.append('k')
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k']
>>> name +
SyntaxError: invalid syntax
>>> name + ['m']
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm']
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k']
>>> name = name + ['m']
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm']
>>> [1, 2, 3, 3, 2, 3, 1, 4].count(1)
2
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm']
>>> name.append([1, 2])
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm', [1, 2]]
>>> name.extend([3, 4, 5])
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm', [1, 2], 3, 4, 5]
>>> name[len(name):] = [6, 7, 8]
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm', [1, 2], 3, 4, 5, 6, 7, 8]
>>> name.extend(['a', 'b', ['c', 'd']])
>>> name
['P', 'y', 't', 'h', 'o', 'n', 'k', 'm', [1, 2], 3, 4, 5, 6, 7, 8, 'a', 'b', ['c', 'd']]
>>> del name[6:]
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> del name[2:3]
>>> name
['P', 'y', 'h', 'o', 'n']
>>> name.insert(2, 't')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name.pop()
'n'
>>> name.extend('n')
>>> name.reverse()
>>> name
['n', 'o', 'h', 't', 'y', 'P']
>>> name.reverse()
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name2 = name
>>> name3 = name
>>> name3 = name[:]
>>> name2
['P', 'y', 't', 'h', 'o', 'n']
>>> name3
['P', 'y', 't', 'h', 'o', 'n']
>>> name.sort()
>>> name2
['P', 'h', 'n', 'o', 't', 'y']
>>> name
['P', 'h', 'n', 'o', 't', 'y']
>>> x = [4, 5, 3, 1]
>>> y = x
>>> z = x[:]
>>> y
[4, 5, 3, 1]
>>> x
[4, 5, 3, 1]
>>> x.sort()
>>> x
[1, 3, 4, 5]
>>> y
[1, 3, 4, 5]
>>> z
[4, 5, 3, 1]
>>> xx = z["]
       
SyntaxError: EOL while scanning string literal
>>> xx = z[:]
>>> xx
[4, 5, 3, 1]
>>> xx = sorted(z)
>>> xx
[1, 3, 4, 5]
>>> z
[4, 5, 3, 1]
>>> ================================ RESTART ================================
>>> number
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> y
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> number = [1, 3, 2, 6, 4]
>>> cmp(1, 2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    cmp(1, 2)
NameError: name 'cmp' is not defined
>>> lt(1, 3)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    lt(1, 3)
NameError: name 'lt' is not defined
>>> numbers.sort(-1)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    numbers.sort(-1)
NameError: name 'numbers' is not defined
>>> number.sort(-1)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    number.sort(-1)
TypeError: must use keyword argument for key function
>>> number.sort((2>1)-(2<1))
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    number.sort((2>1)-(2<1))
TypeError: must use keyword argument for key function
>>> import operator
>>> operator.lt(1, 2)
True
>>> number.sort(true)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    number.sort(true)
NameError: name 'true' is not defined
>>> number.sort(operator.lt(1, 2))
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    number.sort(operator.lt(1, 2))
TypeError: must use keyword argument for key function
>>> number.sort(lt)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    number.sort(lt)
NameError: name 'lt' is not defined
>>> number.sort()
>>> number
[1, 2, 3, 4, 6]
>>> number = [4, 2, 5]
>>> number
[4, 2, 5]
>>> operator.lt(1, 2)
True
>>> number.sort(operator.lt)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    number.sort(operator.lt)
TypeError: must use keyword argument for key function
>>> number.sort(key=operator.lt)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    number.sort(key=operator.lt)
TypeError: op_lt expected 2 arguments, got 1
>>> number.sort(key=operator.lt(1, 2))
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    number.sort(key=operator.lt(1, 2))
TypeError: 'bool' object is not callable
>>> number.sort(key=-1)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    number.sort(key=-1)
TypeError: 'int' object is not callable
>>> number.sort(key=operator.lt(a,b))
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    number.sort(key=operator.lt(a,b))
NameError: name 'a' is not defined
>>> number.sort(key=len)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    number.sort(key=len)
TypeError: object of type 'int' has no len()
>>> a=1
>>> b=2
>>> number.sort(key=operator.lt(a, b))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    number.sort(key=operator.lt(a, b))
TypeError: 'bool' object is not callable
>>> number.sort(key=operator.lt)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    number.sort(key=operator.lt)
TypeError: op_lt expected 2 arguments, got 1
>>> number.sort(key-operator.__lt__)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    number.sort(key-operator.__lt__)
NameError: name 'key' is not defined
>>> number.sort(key=operator.__lt__)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    number.sort(key=operator.__lt__)
TypeError: op_lt expected 2 arguments, got 1
>>> number.sort(key=operator.lt,a,b)
SyntaxError: non-keyword arg after keyword arg
>>> def com(x, y):
	if x < y :
		return 1
	elif x > y:
		return -1
	else:
		return 0
number.sort(com)
SyntaxError: invalid syntax
>>> number.srot(com)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    number.srot(com)
AttributeError: 'list' object has no attribute 'srot'
>>> number.sort(com)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    number.sort(com)
NameError: name 'com' is not defined
>>> def com(x, y):
	if x < y :
		return 1
	elif x > y:
		return -1
	else:
		return 0

>>> com(1, 2)
1
>>> number.sort(com)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    number.sort(com)
TypeError: must use keyword argument for key function
>>> number.sort(key=com)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    number.sort(key=com)
TypeError: com() missing 1 required positional argument: 'y'
>>> ================================ RESTART ================================
>>> 1, 2, 3
(1, 2, 3)
>>> 32,
(32,)
>>> [5, 5]*2
[5, 5, 5, 5]
>>> 50, * 2
SyntaxError: can use starred expression only as assignment target
>>> 50,*2
SyntaxError: can use starred expression only as assignment target
>>> (50,)*3
(50, 50, 50)
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple([2, 3, 5])
(2, 3, 5)
>>> a = [1, 3 5, 6]
SyntaxError: invalid syntax
>>> a = [1, 4, 5, 76]
>>> a.reverse()
>>> a
[76, 5, 4, 1]
>>> b = a.reversed()
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    b = a.reversed()
AttributeError: 'list' object has no attribute 'reversed'
>>> reversed(a)
<list_reverseiterator object at 0x10577f668>
>>> a
[76, 5, 4, 1]
>>> list(reversed(a))
[1, 4, 5, 76]
>>> format = 'hello, %s, %s enough for ya?'
>>> values = ('world', 'Hot')
>>> print(format % values)
hello, world, Hot enough for ya?
>>> format = 'Pi width three decimals: %.3f'
>>> form math import pi
SyntaxError: invalid syntax
>>> from math import pi
>>> print(format % pi)
Pi width three decimals: 3.142
>>> ================================ RESTART ================================
>>> 
<string.Template object at 0x10577f668>
<string.Template object at 0x10577f2e8>
<string.Template object at 0x10577f5f8>
Traceback (most recent call last):
  File "/Users/jtun02/Desktop/Python/L/template.py", line 18, in <module>
    d.substitute(d)
AttributeError: 'dict' object has no attribute 'substitute'
>>> ================================ RESTART ================================
>>> 
<string.Template object at 0x105802668>
<string.Template object at 0x1058022e8>
<string.Template object at 0x1058025f8>
Traceback (most recent call last):
  File "/Users/jtun02/Desktop/Python/L/template.py", line 18, in <module>
    d.substitute(d)
AttributeError: 'dict' object has no attribute 'substitute'
>>> ================================ RESTART ================================
>>> 
<string.Template object at 0x10527c668>
<string.Template object at 0x10527c2e8>
<string.Template object at 0x10527c5f8>
Traceback (most recent call last):
  File "/Users/jtun02/Desktop/Python/L/template.py", line 18, in <module>
    d.safe_substitute(d)
AttributeError: 'dict' object has no attribute 'safe_substitute'
>>> ================================ RESTART ================================
>>> 
<string.Template object at 0x105382668>
<string.Template object at 0x1053822e8>
<string.Template object at 0x1053825f8>
Traceback (most recent call last):
  File "/Users/jtun02/Desktop/Python/L/template.py", line 18, in <module>
    d.substitute(d)
AttributeError: 'dict' object has no attribute 'substitute'
>>> from string import Template
s = Template('$x, glorious $x!')
s.substitute(x = 'slurm')
print(s)
SyntaxError: multiple statements found while compiling a single statement
>>> form string import Template
SyntaxError: invalid syntax
>>> from string import Template
>>> s = Template('$x, glorious $x!')
>>> s.substitute(x = 'slurm')
'slurm, glorious slurm!'
>>> z = Template('It\'s ${x}tastic!')
>>> z.substitute(x = 'slurm')
"It's slurmtastic!"
>>> d = Te
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    d = Te
NameError: name 'Te' is not defined
>>> d = Template('A $string must never $active')
>>> o = {}
>>> o['string'] = 'grent leman'
>>> o['active'] = 'show his socks'
>>> d.substitute(o)
'A grent leman must never show his socks'
>>> width = 40
>>> price_width = 10
>>> item_width = width - price_width
>>> header_format = '%-*s%*s'
>>> print(header_format % (item_width, 'Item', price_width, 'Price'))
Item                               Price
>>> print('=' * width)
========================================
>>> print('%-*s%-*s' % (item_width, 'Item', price_width, 'Price'))
Item                          Price     
>>> ================================ RESTART ================================
>>> 
========================================
Item                               Price
----------------------------------------
Apples                              0.40
Pears                               0.50
Cantaloupers                        1.92
Dried Apricots (16 oz.)             9.00
Prunts (4 lbs.)                    12.00
========================================
>>> seq = [1, 3, 4, 6,6 ]
>>> seq.jpin(',')
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    seq.jpin(',')
AttributeError: 'list' object has no attribute 'jpin'
>>> seq.join(',')
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    seq.join(',')
AttributeError: 'list' object has no attribute 'join'
>>> seq = ['1'] * 5
>>> seq
['1', '1', '1', '1', '1']
>>> seq.join(',')
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    seq.join(',')
AttributeError: 'list' object has no attribute 'join'
>>> '12345'.join(',')
','
>>> abc = '12345'
>>> abc.join(',')
','
>>> abc
'12345'
>>> seq
['1', '1', '1', '1', '1']
>>> ','.join(seq)
'1,1,1,1,1'
>>> seq
['1', '1', '1', '1', '1']
>>> ','.join(['a','b','c'])
'a,b,c'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> dirs = '','usr','bin','env'
>>> dirs
('', 'usr', 'bin', 'env')
>>> '/'.join(dirs)
'/usr/bin/env'
>>> dirs
('', 'usr', 'bin', 'env')
>>> _dirs = '/'.join(dirs)
>>> _dirs
'/usr/bin/env'
>>> '/'.split(_dirs)
['/']
>>> _dirs.split('/')
['', 'usr', 'bin', 'env']
>>> 'that\'s all folks'.title()
"That'S All Folks"
>>> import string
>>> string.capwords('that\'s all. folks')
"That's All. Folks"
>>> testStr = 'that\'s all. folks'
>>> string.swapcase
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    string.swapcase
AttributeError: 'module' object has no attribute 'swapcase'
>>> string.swapcase(testStr)
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    string.swapcase(testStr)
AttributeError: 'module' object has no attribute 'swapcase'
>>> testStr.swapcase()
"THAT'S ALL. FOLKS"
>>> testStr.istitle
<built-in method istitle of str object at 0x1058af270>
>>> testStr.istitle()
False
>>> testStr.upper()
"THAT'S ALL. FOLKS"
>>> 'abc'.split('')
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    'abc'.split('')
ValueError: empty separator
>>> 'a b c'.split()
['a', 'b', 'c']
>>> 'a b c'.split(' ')
['a', 'b', 'c']
>>> ' this is '.strip()
'this is'
>>> ' this is jack '.strip().split(' ')
['this', 'is', 'jack']
>>> ' this is jack '.split(' ')
['', 'this', 'is', 'jack', '']
>>> '*** SPAM * for * everyone!!! ***'.strip(' *!')
'SPAM * for * everyone'
>>> from string import maketrans
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    from string import maketrans
ImportError: cannot import name 'maketrans'
>>> table = maketrans('cs', 'kz')
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    table = maketrans('cs', 'kz')
NameError: name 'maketrans' is not defined
>>> table = string.maketrans('cs', 'kz')
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    table = string.maketrans('cs', 'kz')
AttributeError: 'module' object has no attribute 'maketrans'
>>> ================================ RESTART ================================
>>> test = 'this is an inkrediable test'
>>> m = test.maketrans('cs', 'kz')
>>> test.translate(t)
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    test.translate(t)
NameError: name 't' is not defined
>>> test.translate(m)
'thiz iz an inkrediable tezt'
>>> test.translate(m, ' ')
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    test.translate(m, ' ')
TypeError: translate() takes exactly one argument (2 given)
>>> test.translate(m)
'thiz iz an inkrediable tezt'
>>> m2 = test.maketrans('abc', 'xyz')
>>> test.translate(m2)
'this is xn inkredixyle test'
>>> ================================ RESTART ================================
>>> items = [('name', 'Gumby'), ('age', 43)]
>>> d = dict(items)
>>> d
{'age': 43, 'name': 'Gumby'}
>>> d2 = dict(name='Gumby', age=43)
>>> d2
{'age': 43, 'name': 'Gumby'}
>>> list('abc')
['a', 'b', 'c']
>>> tuple('ablc')
('a', 'b', 'l', 'c')
>>> d['age']
43
>>> d['gender'] = '1'
>>> d
{'age': 43, 'gender': '1', 'name': 'Gumby'}
>>> 'age' in d
True
>>> 
