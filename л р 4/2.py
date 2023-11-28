class Country:
    capital = ""
    square = 0
    population = 0
    count = 0
    def __init__(self):
        self.capital = "Пружаны"
        self.square = 206900
        self.population = 9300
        self.count+=1
    def new_country(self, capital, square, population):
        print("Создано государство со столицей - ", capital)
        self.capital = capital
        self.square = square
        self.population = population
        self.count += 1
    def show_counter(self):
        return self.count
    def output(self):
        print("\n==========Страны==========")
        print(f'''    {self.capital}    
    {self.square} кв. км  
    {self.population} тыс. чел.''')
        print("==========================")
        return 0

country1 = Country()
country2 = Country()
country3 = Country()
country4 = Country()
country5 = Country()
country2.new_country("Пекин", 1000000, 1300000)
country3.new_country("Москва", 2000000, 150000)
country4.new_country("Минск", 206900, 9300)
capital = input("Введите столицу: ")
square = int(input("Введите площадь: "))
population = int(input("Введите население: "))
country5.new_country(capital, square, population)

s=int(input("Введите площадь для поиска(в кв.км): "))
p=int(input("Введите численность населения для поиска(в тыс. человек): "))

if(country1.square==s):
    print("Страна с заданной площадью:")
    country1.output()
else:
    if(country2.square==s):
        print("Страна с заданной площадью:")
        country2.output()
    else:
        if (country3.square == s):
            print("Страна с заданной площадью:")
            country3.output()
        else:
            if (country4.square == s):
                print("Страна с заданной площадью:")
                country4.output()
            else:
                if (country5.square == s):
                    print("Страна с заданной площадью:")
                    country5.output()
                else:
                    print("Страны с заданной площадью не существует!")


if(country1.population==p):
    print("Страна с заданным населением:")
    country1.output()
else:
    if(country2.population==p):
        print("Страна с заданным населением:")
        country2.output()
    else:
        if (country3.population==p):
            print("Страна с заданным населением:")
            country3.output()
        else:
            if (country4.population==p):
                print("Страна с заданным населением:")
                country4.output()
            else:
                if (country5.population==p):
                    print("Страна с заданным населением:")
                    country5.output()
                else:
                    print("Страны с заданным населением не существует!")