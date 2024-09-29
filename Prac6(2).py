import math
spisok = []
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
h = int(input("Введіть h: "))
while a <= b:
    x = 7 - a * math.e**(2 * a - 1) + math.sqrt(abs(a))
    a = a + h
    spisok.append(x)
print(spisok)