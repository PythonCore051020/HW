week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

user_number = input('Please enter number from 1 to 7:')

try:
    day = int(user_number)
    if day <= 1 or day >= 7:
        raise ValueError('Number is not valid')
except ValueError:
    print('Number is not valid')
else:
    print(week_list[day-1])
