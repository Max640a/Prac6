spisok = []
word = input("Введіть слова розділені комами або пробілами: ")
spl = word.replace(",", " ").split()
spisok.append(word)
print(spl)