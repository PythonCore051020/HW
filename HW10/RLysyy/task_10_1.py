# task 10.1 Напишіть програму для обчислення частки двох чисел ....

def task10_1():
    numbers_str = input('Please enter two numbers:')
    numbers_list = numbers_str.strip().split(',')

    try:
        x = int(numbers_list[0])
        y = int(numbers_list[1])
        x_div_y = x / y
    except IndexError:
        print('Seems no two numbers')
    except ValueError:
        print('Number is not valid')
    except ZeroDivisionError:
        print("Division by zero")
    except Exception:
        print("Seems like something else went wrong")
    else:
        print(x_div_y)
    finally:
        print("Program finished")


task10_1()
