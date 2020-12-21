
hour = int(input('Enter hour:'))
minute = int(input('Enter minute:'))
ampm = raw_input('Am or PM:')

if ampm == 'am' and hour != 12:
    print(hour, minute)

if ampm == 'pm' and hour != 12:
    print(hour + 12, minute)

if hour == 12 and ampm == 'am':
    print('00', minute)

if hour == 12 and ampm == 'pm':
    print('12', minute)