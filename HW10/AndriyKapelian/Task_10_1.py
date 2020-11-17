while True:
    user_numbers = (input('Please enter two numbers:'))
    list_users_numbers = user_numbers.strip().split(",")
    try:
        x = int(list_users_numbers[0])
        y = int(list_users_numbers[1])
    except ValueError:
        print('Number is not valid')
    else:
        try:
            result = x/y
            print(result)
        except ZeroDivisionError:
            print("Division by zero!")
    finally:
        answer = input('Do you want try again?')
        if answer.lower() == 'y':
            continue
        else:
            break




