number = int(input("Введите целое число: "))
chet = 0
nechet = 0
while number != 0:
    if ((number % 10) % 2) == 0:
        chet += 1
    else:
        nechet += 1
    number = number // 10
print("Количество четных цифр - ", chet, "\nКоличество нечетных цифр - ", nechet)
