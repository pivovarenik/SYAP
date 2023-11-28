count_1 = 0
with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        count_1+=1
        if not line:
            break
        f1.write(line + '\n')
choice=True
while choice:
    try:
        N = int(input("Введите значение N: "))
        K = int(input("Введите значение K: "))
    except Exception as e:
        print("Ошибка:", e)
    if (N>0) and (N<K) and (K>N) and (K<count_1):
        choice = False
    print("Повторите ввод значений N и K!\n")



# копируем строки из F1 в F2 с позиции N до K
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
    if N < 1:
        N = 1
    if K > len(lines):
        K = len(lines)
    for i in range(N - 1, K):
        f2.write(lines[i])
with open('F2.txt', 'r') as f2:
    text = f2.read()
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyzБбВвГгДдЖжЙйЗзКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ"
    count = sum(1 for char in text if char in consonants)
    print(f"Количество согласных букв в файле F2: {count}")
