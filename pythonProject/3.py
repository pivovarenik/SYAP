#file=open('Предметы.txt', 'w')
#file.close()

try:
    with open("предметы.txt", "r", encoding='utf-8') as file_of_subjects:
        subjects = file_of_subjects.readlines()
except Exception as e:
    print("Ошибка:", e)

print("\nСодержимое файла:\n", " ".join(subjects))
dictionary = {}
for i in subjects:
    subject, lessons = i.split(": ")
    count_of_lessons = 0
    lecture = practice = lab = 0
    number_of_lessons = lessons.split()
    lecture = int(lessons.split(" ")[0].split("(")[0])
    if len(number_of_lessons) > 1:
        practice = int(lessons.split(" ")[1].split("(")[0])
        if len(number_of_lessons) > 2:
            lab = int(lessons.split(" ")[2].split("(")[0])
    count_of_lessons = lecture + practice + lab
    dictionary[subject] = count_of_lessons

print("\n", dictionary)