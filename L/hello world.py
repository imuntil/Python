#!usr/bin/python
print ('hello world!')

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'Jue',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]
endings = ['st', 'nd', 'rd'] + 17*['th'] \
         + ['st', 'nd', 'rd'] + 7 * ['th'] \
         + ['st']
year = input('Year:')
month = input('Month(1-12):')
day = input('Day(1-31):')
month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
day_name = day + endings[day_number - 1]
print(month_name + ' ' + day_name + '. ' + year)