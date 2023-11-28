def check(S):
    lst = S.split()
    number = len(lst)
    maximum = max(lst)
    print("\nКоличество слов в строке - ", number, "\nСамое длинное слово - ", maximum)

try:
    s = input("Введите строку: ")
    check(s)
except Exception as e:
    print("Ошибка: ", e)
finally:
    print("Finally")

