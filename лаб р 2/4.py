def divide_numbers(a, b):
    try:
        result = a / b
        print("Результат деления: ", result)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    finally:
        print("Этот блок выполнится всегда, независимо от того, было исключение или нет.")


try:
    divide_numbers(10, 2)
except Exception as e:
    print("Ошибка: ", e)

try:
    divide_numbers(5, 0)
except Exception as e:
    print("Ошибка: ", e)
