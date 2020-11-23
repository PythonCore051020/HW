# task 10.2 Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# В програмі необхідно передбачити можливість введення від’ємного числа, і в цьому випадку згенерувати виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.

class AgeError(ValueError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_age(p_age):
    if p_age < 0:
        raise AgeError('Age is negative')

    if p_age % 2 > 0:
        return 'Odd age'

    return 'Even age'


if __name__ == "__main__":
    try:
        age = int(input('Please enter your age:'))
        print(check_age(age))
    except AgeError as e:
        print('Negative age is not allowed. ', e)
    except Exception:
        print("Seems like something else went wrong")
    finally:
        print("Program finished")