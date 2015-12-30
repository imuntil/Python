people = {
	'Alice': {
		'phone':'1234',
		'addr':'Foo drive 23'
		},
	'Beth': {
		'phone':'4356',
		'addr':'Bar street 56'
		},
	'Cecil':{
		'phone':'3308',
		'addr':'Baz avenune 90'
		}
}
labels = {
	'phone': 'phone number',
	'addr':'address'
}
name = input('Name: ')
request = input('Phone number (p) or address (a)?')
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people : 
	print('%s\'s %s is %s.' % (name, labels[key], people[name][key]))
