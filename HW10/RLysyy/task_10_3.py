# task 10.3 Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

WEEKS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
try:
    day_number = int(input('Please enter day number:'))

    if (day_number >= 1) and (day_number <= 7):
        print(WEEKS[day_number - 1])
    else:
        raise ValueError('Number is not valid')
except ValueError:
    print('Number is not valid')
