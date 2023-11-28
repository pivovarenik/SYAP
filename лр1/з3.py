list = []
sum = 0
nul = 0
index = -1
sum_nul = 0

print("Введите список из 10 элементов: ")
for i in range(10):
    l = int(input())
    list.append(l)
    if l > 0:
        sum += l
        index = 1
    if l == 0:
        nul += 1
if nul < 2:
    if index == 1:
        print("Сумма положительных элементов - ", sum, "\n", 0)
    else:
        print("Положительные элементы отсутствуют\n", 0)
else:
    n1 = -1
    n2 = -1
    for i in range(10):
        if list[i] == 0 and n1 == -1:
            n1 = i
        if list[i] == 0 and i > n1:
            n2 = i
            break
    for i in range(n1 + 1, n2):
        sum_nul += list[i]
    print("Сумма положительных элементов - ", sum, "\nСумма между первыми нулями - ", sum_nul)
