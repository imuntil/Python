database = [
	['albert', '1234'],
	['dilbert', '4242'],
	['smith', '4567'],
	['jones', '7683']
]
username = input('User name: ')
pin = input('PIN code: ')

if [username, pin] in database: print ('Access granted')