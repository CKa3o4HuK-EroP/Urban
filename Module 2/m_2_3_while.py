my_list = list(map(int, input("Введите список чисел через пробел: ").split()))
i = 0
while i < len(my_list):
    if my_list[i] > 0: print(my_list[i]); i += 1
    elif my_list[i] == 0: i += 1; continue
    else: break
