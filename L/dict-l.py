Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> phonebook = {'Beth':'9103', 'Alice':'2345}
	     
SyntaxError: EOL while scanning string literal
>>> phonebook = {'Beth':'9103', 'Alice':'2345'}
>>> phonebook
{'Beth': '9103', 'Alice': '2345'}
>>> 'Beth\'s phone number is %(Beth)s.' % phonebook
"Beth's phone number is 9103."
>>> template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
>>> data = {'title':'My Home Page', 'text':'Welcome to my home page'}
>>> print (template % data}
SyntaxError: invalid syntax
>>> print (template % data)
<html>
<head><title>My Home Page</title></head>
<body>
<h1>My Home Page</h1>
<p>Welcome to my home page</p>
</body>
>>> s = Template('$x, glorious $x!')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s = Template('$x, glorious $x!')
NameError: name 'Template' is not defined
>>> from string import Template
>>> s = Template('$x, glorious $x!')
>>> z.substitute(x = 'slurm')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    z.substitute(x = 'slurm')
NameError: name 'z' is not defined
>>> s.substitute(x = 'slurm')
'slurm, glorious slurm!'
>>> d = '''<html>
<head><title>$title</title></head>
<body>
<h1>$title</h1>
<p>$text</p>
</body>'''
>>> d.subsittide(data)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.subsittide(data)
AttributeError: 'str' object has no attribute 'subsittide'
>>> d.substitute(data)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.substitute(data)
AttributeError: 'str' object has no attribute 'substitute'
>>> d = Template('''<html>
<head><title>$title</title></head>
<body>
<h1>$title</h1>
<p>$text</p>
</body>''')
>>> d.substitute(data)
'<html>\n<head><title>My Home Page</title></head>\n<body>\n<h1>My Home Page</h1>\n<p>Welcome to my home page</p>\n</body>'
>>> data
{'title': 'My Home Page', 'text': 'Welcome to my home page'}
>>> data.clear()
>>> data
{}
>>> x = {'attr':'value'}
>>> y = x
>>> y
{'attr': 'value'}
>>> x = {}
>>> y
{'attr': 'value'}
>>> 
=============================== RESTART: Shell ===============================
>>> x = {'key':'value'}
>>> y = x
>>> y
{'key': 'value'}
>>> x.clear()
>>> y
{}
>>> 
=============================== RESTART: Shell ===============================
>>> x = {'key':'value'}
>>> y = deepcopy(x)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    y = deepcopy(x)
NameError: name 'deepcopy' is not defined
>>> from copy import deepcopy
>>> y = deepcopy(x)
>>> y
{'key': 'value'}
>>> y['key'] = 'new value'
>>> x
{'key': 'value'}
>>> y
{'key': 'new value'}
>>> 
=============================== RESTART: Shell ===============================
>>> from copy import deepcopy
>>> x = {}
>>> x['key'] = ['a','b']
>>> y = x.copy()
>>> yd = deepcopy(x)
>>> y
{'key': ['a', 'b']}
>>> yd
{'key': ['a', 'b']}
>>> d['key'].append('c')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d['key'].append('c')
NameError: name 'd' is not defined
>>> x['key'].append('c')
>>> x
{'key': ['a', 'b', 'c']}
>>> y
{'key': ['a', 'b', 'c']}
>>> yd
{'key': ['a', 'b']}
>>> 
=============================== RESTART: Shell ===============================
>>> from copy import deepcopy
>>> x = {'key':'value'}
>>> y = x.copy()
>>> yd = deepcopy(x)
>>> y
{'key': 'value'}
>>> yd
{'key': 'value'}
>>> x['key'] = 'new value'
>>> y
{'key': 'value'}
>>> yd
{'key': 'value'}
>>> ax = ['a', 'b']
>>> ay = ax
>>> ay
['a', 'b']
>>> ax[0:1] = 'c'
>>> ax
['c', 'b']
>>> ay
['c', 'b']
>>> az = ax[:]
>>> az
['c', 'b']
>>> ax[0:0] = 'x'
>>> ax
['x', 'c', 'b']
>>> zy
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    zy
NameError: name 'zy' is not defined
>>> ay
['x', 'c', 'b']
>>> az
['c', 'b']
>>> dict.fromkeys(['name', 'age'])
{'name': None, 'age': None}
>>> 
=============================== RESTART: Shell ===============================
>>> d = {}
>>> d.get('name')
>>> print(d.get('name'))
None
>>> print(d.get('name', 'there is no name'))
there is no name
>>> 'name' in d
False
>>> d.has_key('name')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d.has_key('name')
AttributeError: 'dict' object has no attribute 'has_key'
>>> 
=============================== RESTART: Shell ===============================
>>> d = {'title':'Python Web site', 'url':'http://www.python.org', 'spm':0}
>>> d.items()
dict_items([('url', 'http://www.python.org'), ('title', 'Python Web site'), ('spm', 0)])
>>> list(d.iteritems())
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    list(d.iteritems())
AttributeError: 'dict' object has no attribute 'iteritems'
>>> d.keys()
dict_keys(['url', 'title', 'spm'])
>>> d.keys()[0]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d.keys()[0]
TypeError: 'dict_keys' object does not support indexing
>>> d
{'url': 'http://www.python.org', 'title': 'Python Web site', 'spm': 0}
>>> d.pop('spm')
0
>>> d
{'url': 'http://www.python.org', 'title': 'Python Web site'}
>>> d['pop'] = 'pop'
>>> d
{'url': 'http://www.python.org', 'title': 'Python Web site', 'pop': 'pop'}
>>> d.popitem()
('url', 'http://www.python.org')
>>> d
{'title': 'Python Web site', 'pop': 'pop'}
>>> d.setdefault('url', 'http://www.python.org')
'http://www.python.org'
>>> d
{'url': 'http://www.python.org', 'title': 'Python Web site', 'pop': 'pop'}
>>> x = {'title':'Python Language Website'}
>>> d.update(x)
>>> d
{'title': 'Python Language Website', 'pop': 'pop', 'url': 'http://www.python.org'}
>>> x
{'title': 'Python Language Website'}
>>> x.update(d)
>>> x
{'url': 'http://www.python.org', 'title': 'Python Language Website', 'pop': 'pop'}
>>> d
{'title': 'Python Language Website', 'pop': 'pop', 'url': 'http://www.python.org'}
>>> d == x
True
>>> d === x
SyntaxError: invalid syntax
>>> d
{'title': 'Python Language Website', 'pop': 'pop', 'url': 'http://www.python.org'}
>>> d.values()
dict_values(['Python Language Website', 'pop', 'http://www.python.org'])
>>> dict([('name':'zhin'),('age':'25')])
SyntaxError: invalid syntax
>>> dict([('name','zhin'),('age',25)])
{'name': 'zhin', 'age': 25}
>>> dict('name'='zhin','age'=25)
SyntaxError: keyword can't be an expression
>>> dict(name='zhin',age=25)
{'name': 'zhin', 'age': 25}
>>> d
{'title': 'Python Language Website', 'pop': 'pop', 'url': 'http://www.python.org'}
>>> d.title
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d.title
AttributeError: 'dict' object has no attribute 'title'
>>> print ('age:', 15)
age: 15
>>> print(1, 2, 3)
1 2 3
>>> 1,2,3
(1, 2, 3)
>>> name = 'Gummy'
>>> salutation = 'Mr.'
>>> greeting = 'Hello'
>>> print(greeting, salutation, name)
Hello Mr. Gummy
>>> print(greeting,salutation,name)
Hello Mr. Gummy
>>> 
=============================== RESTART: Shell ===============================
>>> x, y, z = 1, 2, 3
>>> x
1
>>> y
2
>>> z
3
>>> 
=============================== RESTART: Shell ===============================
>>> x = {'name':'zhin', 'age':25}
>>> x
{'name': 'zhin', 'age': 25}
>>> key, value = x.popitem()
>>> key
'name'
>>> value
'zhin'
>>> x
{'age': 25}
>>> a, b, reset* = 1, 2, 3, 4
SyntaxError: invalid syntax
>>> a, b, reset* = [1, 2, 3, 4]
SyntaxError: invalid syntax
>>> z
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a, b, c* = (1, 2, 3, 4)
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> x = 2
>>> x += 1
>>> x
3
>>> x *= 2
>>> x
6
>>> x += 1
>>> x *= 2
>>> x
14
>>> 
