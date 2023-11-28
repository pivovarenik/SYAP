class Pistol:

    def __init__(self, name, caliber):
        self.__name = name
        self.__caliber = caliber
        self.__bullets_count = 5
        self.__is_charged = True

    def reload(self):
        self.__bullets_count = 5
        self.__is_charged = True

    def shoot(self):
        if self.__is_charged:
            print("Выстрел\n")
            self.__bullets_count -= 1
            if self.__bullets_count == 0:
                self.__is_charged = False
        else:
            print("Пистолет разряжен")

    def display_info(self):
        return f"Название пистолета: {self.__name}\nКалибр: {self.__caliber}\nКоличество патрон: {self.__bullets_count}"


pistol = Pistol("Пистолет Макарова(ПМ)", "9 мм")

while True:
    print("\n==========Меню==========")
    print("1. Информация о пистолете")
    print("2. Перезарядить пистолет")
    print("3. Выстрелить из пистолета")
    print("4. Выход")

    choice = input("Сделайте выбор: ")

    if choice == "1":
        info = pistol.display_info()
        print(info);
    elif choice == "2":
        pistol.reload()
        print("Пистолет перезаряжен.")
    elif choice == "3":
        pistol.shoot()
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Попробуйте снова")


