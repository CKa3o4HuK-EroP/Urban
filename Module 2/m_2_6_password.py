#from random import randint
#key = randint(3, 20)
key = int(input("Введите число на левой вставке: "))
password = ''
for i in range(1, key - 1):
    for j in range(i + 1, key):
        if key % (i + j) == 0:
            password += str(i)
            password += str(j)

print(f'Ключ: {key}\nОтвет: {password}')
