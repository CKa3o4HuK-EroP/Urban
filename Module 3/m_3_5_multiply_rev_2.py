def get_multiplied_digits(number):
    str_num = str(number).replace('0', '')
    first = int(str_num[0])
    if len(str_num) > 1:
        return first * get_multiplied_digits(int(str_num[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
