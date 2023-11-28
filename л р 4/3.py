class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("Вы уже едете.")
            return
        print("Начало движения...")
        try:
            while self.speed < 1 or self.speed > 120:
                self.speed = int(input("Укажите скорость:"))
        except Exception as e:
            self.speed = 0
            print("Ошибка!", e)

    def stop(self):
        if self.speed == 0:
            print("Вы уже стоите.")
            return
        print("Остановка...")
        self.speed = 0

    def turn(self, direction):
        if self.speed == 0:
            print("Сначала начните движение.")
            return
        print("Выполняется поворот в направлении:", direction)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)

    def print_car(self):
        print(f"Автомобиль: {self.name}\n Цвет: {self.color}")
        if self.is_police:
            print("Тип машины: полицейская.")


class TownCar(Car):
    def __init__(self):
        super().__init__(0, "Жёлтый", "Городской автомобиль.", False)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        if self.speed > 60:
            print("Вы превышаете максимально допустимую скорость.")


class SportCar(Car):
    def __init__(self):
        super().__init__(0, "Красный", "Спортивный автомобиль.", False)

    def go(self):
        if self.speed > 0:
            print("Вы уже едете.")
            return
        print("Начало движения...")
        try:
            while self.speed < 1 or self.speed > 350:
                self.speed = int(input("Укажите скорость:"))
        except Exception as e:
            self.speed = 0
            print("Ошибка!", e)

    def edit_speed(self):
        try:
            while self.speed < 1 or self.speed > 350:
                self.speed = int(input("Укажите новую скорость:"))
        except Exception as e:
            print("Ошибка!", e)


class WorkCar(Car):
    def __init__(self):
        super().__init__(0, "Белый", "Рабочий автомобиль.", False)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        if self.speed > 40:
            print("Вы превышаете максимально допустимую скорость.")


class PoliceCar(Car):
    def __init__(self):
        self.lights = False
        super().__init__(0, "Белый", "Рабочий автомобиль.", True)

    def go(self):
        if self.speed > 0:
            print("Вы уже едете.")
            return
        print("Начало движения...")
        try:
            while self.speed < 1 or (self.speed > 120 and self.lights == False):
                self.speed = int(input("Укажите скорость:"))
        except Exception as e:
            self.speed = 0
            print("Ошибка!", e)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        if self.lights == True:
            print("Мигалки включены.Вы можете ехать с любой скоростью(до 350 км/ч).")

    def edit_speed(self):
        if self.lights == False:
            print("Нельзя изменить скорость с выключенными мигалками.")
            return
        try:
            while self.speed < 1 or self.speed > 350:
                self.speed = int(input("Укажите новую скорость:"))
        except Exception as e:
            print("Ошибка!", e)

    def on_lights(self):
        if self.lights == True:
            print("Мигалки уже включены")
            return
        self.lights = True
        print("Вы включили мигалки!")

    def off_lights(self):
        if self.lights == False:
            print("Мигалки уже выключены")
            return
        self.lights = False
        print("Вы выключили мигалки.")


def drive_town():
    town_car = TownCar()
    counter = 0
    print("Вы сели за руль городского автомобиля...")
    while True:
        print('''\n1. Посмотреть информацию о машине.
2. Поехать.
3. Повернуть.
4. Посмотреть скорость.
5. Остановиться.
6. Выйти.''')
        while True:
            try:
                choice = int(input("Ваш выбор:"))
                if choice < 1 or choice > 6:
                    print("Неправильный ввод.")
                    continue
                print("\n")
            except ValueError:
                print("Некорректный ввод, повторите попытку")
            except Exception as e:
                print("Ошибка! Повторите попытку")
            else:
                break
        if choice == 6 and counter == 0:
            break
        elif choice == 6:
            print("Перед выходом надо остановиться!")
        if choice == 1:
            town_car.print_car()
        if choice == 2:
            town_car.go()
            counter = 1
        if choice == 3:
            turn = input("Куда хотите повернуть?\n")
            town_car.turn(turn)
        if choice == 4:
            town_car.show_speed()
        if choice == 5:
            town_car.stop()
            counter = 0


def drive_sport():
    sprot_car = SportCar()
    counter = 0
    print("Вы сели за руль спортивного автомобиля...")
    while True:
        print('''\n1. Посмотреть информацию о машине.
2. Поехать.
3. Изменить скорость.
4. Повернуть.
5. Посмотреть скорость.
6. Остановиться.
7. Выйти.''')
        while True:
            try:
                choice = int(input("Ваш выбор:"))
                if choice < 1 or choice > 6:
                    print("Неправильный ввод.")
                    continue
                print("\n")
            except ValueError:
                print("Некорректный ввод, повторите попытку")
            except Exception as e:
                print("Ошибка! Повторите попытку")
            else:
                break
        if choice == 7 and counter == 0:
            break
        elif choice == 7:
            print("Перед выходом надо остановиться!")
        if choice == 1:
            sprot_car.print_car()
        if choice == 2:
            sprot_car.go()
            counter = 1
        if choice == 3:
            sprot_car.edit_speed()
        if choice == 4:
            turn = input("Куда хотите повернуть?\n")
            sprot_car.turn(turn)
        if choice == 5:
            sprot_car.show_speed()
        if choice == 6:
            sprot_car.stop()
            counter = 0


def drive_work():
    work_car = WorkCar()
    counter = 0
    print("Вы сели за руль рабочего автомобиля...")
    while True:
        print('''\n1. Посмотреть информацию о машине.
2. Поехать.
3. Повернуть.
4. Посмотреть скорость.
5. Остановиться.
6. Выйти.''')
        while True:
            try:
                choice = int(input("Ваш выбор:"))
                if choice < 1 or choice > 6:
                    print("Неправильный ввод.")
                    continue
                print("\n")
            except ValueError:
                print("Некорректный ввод, повторите попытку")
            except Exception as e:
                print("Ошибка! Повторите попытку")
            else:
                break
        if choice == 6 and counter == 0:
            break
        elif choice == 6:
            print("Перед выходом надо остановиться!")
        if choice == 1:
            work_car.print_car()
        if choice == 2:
            work_car.go()
            counter = 1
        if choice == 3:
            turn = input("Куда хотите повернуть?\n")
            work_car.turn(turn)
        if choice == 4:
            work_car.show_speed()
        if choice == 5:
            work_car.stop()
            counter = 0


def drive_police():
    police_car = PoliceCar()
    counter = 0
    print("Вы сели за руль спортивного автомобиля...")
    while True:
        print('''\n1. Посмотреть информацию о машине.
2. Поехать.
3. Включить мигалки.
4. Выключить мигалки.
5. Изменить скорость.
6. Повернуть.
7. Посмотреть скорость.
8. Остановиться.
9. Выйти.''')
        while True:
            try:
                choice = int(input("Ваш выбор:"))
                if choice < 1 or choice > 9:
                    print("Неправильный ввод.")
                    continue
                print("\n")
            except ValueError:
                print("Некорректный ввод, повторите попытку")
            except Exception as e:
                print("Ошибка! Повторите попытку")
            else:
                break
        if choice == 9 and counter == 0:
            break
        elif choice == 9:
            print("Перед выходом надо остановиться!")
        if choice == 1:
            police_car.print_car()
        if choice == 2:
            police_car.go()
            counter = 1
        if choice == 3:
            police_car.on_lights()
        if choice == 4:
            police_car.off_lights()
        if choice == 5:
            police_car.edit_speed()
        if choice == 6:
            turn = input("Куда хотите повернуть?\n")
            police_car.turn(turn)
        if choice == 7:
            police_car.show_speed()
        if choice == 8:
            police_car.stop()
            counter = 0


while True:
    print("====================Автомобили======================")
    print('''             1.Городской автомобиль.
             2.Спортивный автомобиль.
             3.Рабочий автомобиль.
             4.Полицейский автомобиль.
             5.Выход.''')
    print("====================================================")
    while True:
        try:
            choice = int(input("Ваш выбор:"))
            if choice < 1 or choice > 5:
                print("Неправильный ввод.")
                continue
            print("\n")
        except ValueError:
            print("Некорректный ввод, повторите попытку")
        except Exception as e:
            print("Ошибка! Повторите попытку")
        else:
            break
    if choice == 5:
        break
    elif choice == 1:
        drive_town()
    elif choice == 2:
        drive_sport()
    elif choice == 3:
        drive_work()
    elif choice == 4:
        drive_police()

