def process_input(data):
    if isinstance(data, dict):
        sorted_1 = dict(sorted(data.items(), key=lambda x: x[1]))
        sorted_2 = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        return sorted_1, sorted_2
    elif isinstance(data, list):
        letters_count = sum(c.isalpha() for item in data for c in str(item))
        numbers_count = sum(c.isdigit() for item in data for c in str(item))
        return letters_count, numbers_count
    elif isinstance(data, int):
        number = data
        # if data < 2:
        # return "<2"
        # else:
        for i in range(2, number + 1):  # 2, int(data ** 0.5) + 1):
            if number % i != 0 and number != i:
                return number
            else:
                return ("not prime")
    elif isinstance(data, str):
        words = data.split()
        palindromes = [word for word in words if word.lower() == word.lower()[::-1]]
        return palindromes
    else:
        raise ValueError("\tНеподдерживаемый тип данных")


try:
    input_data = {"b": 2, "a": 1, "c": 3}
    result_asc, result_desc = process_input(input_data)
    print(input_data)
    print("Сортировка по возрастанию:", result_asc)
    print("Сортировка по убыванию:", result_desc)
except Exception as e:
    print("\tОшибка: ", e)

try:
    input_data = [123, "abc", 456, "def"]
    letters, numbers = process_input(input_data)
    print("\n", input_data)
    print("Количество букв:", letters)
    print("Количество чисел:", numbers)
except Exception as e:
    print("\tОшибка: ", e)

try:
    input_data = 11
    prime = process_input(input_data)
    print("\n", input_data)
    print("Простое число:", prime)
except Exception as e:
    print("\tОшибка: ", e)

try:
    input_data = "шалаш человек мем"
    palindromes = process_input(input_data)
    print("\n", input_data)
    print("Слова-палиндромы:", palindromes)
except Exception as e:
    print("\tОшибка: ", e)
