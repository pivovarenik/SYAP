word = input("Введите слово: ")
verh = 0
niz = 0
kolvo = 0

for letter in word:
    if letter != " ":
        if letter.isupper():
            if word.index(letter) < len(word) - 1 and word[word.index(letter) + 1].isupper():
                verh += 1
        elif letter.islower():
            if word.index(letter) < len(word) - 1 and word[word.index(letter) + 1].islower():
                niz += 1
        kolvo += 1

print("Количество букв - ", kolvo, "\nКоличество пар верхнего регистра - ", verh,
      "\nКоличество пар нижнего регистра - ", niz)

print("Егор Кучер живет в 1121!!!")
