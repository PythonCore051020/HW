def check_user_input(age):
    try:
        age_to_int = int(age)
        if age_to_int <= 1:
            raise ValueError('Age is not valid')
    except ValueError:
        print('Age is not valid')
        age_to_int = False
    return age_to_int


def continue_work(answer):
    if answer.lower() == 'y':
        return True
    else:
        return False


while True:
    user_age = check_user_input(input('Please enter your age:'))
    if user_age:

        try:
            if (user_age % 2) > 0:
                print('This is odd number')
            else:
                print('This is even number')
        except ValueError:
            print('Age is not valid')
        finally:
            user_answer = continue_work(input('Do you want try again?'))
            if user_answer:
                continue
            else:
                break








