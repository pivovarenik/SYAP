shop_inventory = {
    "Масло моторное": ["Масло моторное для автомобилей", 25.0, 50],
    "Фильтр масляный": ["Фильтр масляный для автомобилей", 5.0, 100],
    "Тормозные колодки": ["Тормозные колодки для автомобилей", 15.0, 30],
    "Аккумулятор": ["Аккумулятор для автомобилей", 50.0, 20],
    "Шины": ["Шины для автомобилей", 100.0, 40],
    "Свечи зажигания": ["Свечи зажигания для автомобилей", 3.0, 200],
}

def display_description():
    print("Описание товаров:")
    for product, details in shop_inventory.items():
        print(f"{product}: {details[0]}")

def display_price():
    print("Цены на товары:")
    for product, details in shop_inventory.items():
        print(f"{product}: {details[1]} рублей")

def display_quantity():
    print("Количество товаров:")
    for product, details in shop_inventory.items():
        print(f"{product}: {details[2]} штук")

def display_all_info():
    print("Информация о товарах:")
    for product, details in shop_inventory.items():
        print(f"{product}:")
        print(f"  Описание: {details[0]}")
        print(f"  Цена: {details[1]} рублей")
        print(f"  Количество: {details[2]} штук")

def make_purchase():
    total_cost = 0
    while True:
        product_name = input("Введите название товара (или 'n' для выхода): ")
        if product_name.lower() == 'n':
            break
        if product_name in shop_inventory:
            quantity_to_buy = int(input(f"Сколько {product_name} вы хотите купить: "))
            if quantity_to_buy <= shop_inventory[product_name][2]:
                cost = shop_inventory[product_name][1] * quantity_to_buy
                total_cost += cost
                shop_inventory[product_name][2] -= quantity_to_buy
                print(f"Вы добавили {quantity_to_buy} {product_name} в корзину.")
            else:
                print(f"Извините, недостаточно {product_name} в наличии.")
        else:
            print("Извините, такого товара нет в магазине.")
    print(f"Общая стоимость покупок: {total_cost} рублей")

while True:
    print("\nМеню магазина автозапчастей:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        display_description()
    elif choice == '2':
        display_price()
    elif choice == '3':
        display_quantity()
    elif choice == '4':
        display_all_info()
    elif choice == '5':
        make_purchase()
    elif choice == '6':
        print("До свидания! Спасибо за покупки.")
        break
    else:
        print("Неправильный ввод. Пожалуйста, выберите пункт из меню.")
