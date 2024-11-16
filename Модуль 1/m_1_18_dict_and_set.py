my_dict = {
    'Vasya': 1975,
    'Masha': 2002,
    'Egor': 2004
}

print(my_dict)
print(f'Existing value: {my_dict["Egor"]}')

print(f'Non-existing value: {my_dict.get("Maksim")}')
my_dict['Viktor'] = 1985
my_dict['Stas'] = 2015
print(f'Deleted value: {my_dict.pop("Vasya")}')
print(f'Modified dictionary: {my_dict}')

print('\n')

my_set = {1, "Яблоко", 42.314, 1, 1, 42.314, 69, (70-1), 'a', 'aaa', 'a'}
print(f'Set: {my_set}')
my_set.add(42)
my_set.add(241)
my_set.discard(1)
print(f'Modified set: {my_set}')
