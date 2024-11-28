def print_params(a=1, b='string', c=True):
    print(a, b, c, sep='')


values_list_2 = [54.32, 'Строка']

print_params()
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])
