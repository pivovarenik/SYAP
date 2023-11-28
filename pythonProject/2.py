#file=open('Клиент.txt', 'w')
#file.close()

try:
    with open("Клиент.txt", "r", encoding='utf-8') as file_of_subjects:
        clients = file_of_subjects.readlines()
except Exception as e:
    print("Ошибка:", e)
print("\nСодержимое файла:\n", " ".join(clients))

list=[]
list_max=[]
max=0
count=0
for i in clients:
    money=i.split(" ")
    if int(money[1])>1000:
        list.append(money)
        count+=1
        if int(money[1])>=max:
            list_max.append(money)
            max=int(money[1])

if count>0:
    print("Клиенты с суммой на счету более 1000 рублей:\n")
    for i in range(count):
        print(list[i])
    print("\nКлиент с максимальной суммой на счету:\n", list_max[0])
else:
    print("Клиентов с суммой на счету более 1000 рублей нет\n")