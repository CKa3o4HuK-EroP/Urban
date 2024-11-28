def resolve(args):
    total_sum = 0

    if isinstance(args, int):
        total_sum += args
    elif isinstance(args, str):
        total_sum += len(args)
    elif isinstance(args, (list, tuple, set)):
        for item in args:
            total_sum += resolve(item)
    elif isinstance(args, dict):
        for key, value in args.items():
            if isinstance(key, str):
                total_sum += resolve(key)
            total_sum += resolve(value)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = resolve(data_structure)
print(result)
