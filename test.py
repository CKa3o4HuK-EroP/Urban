class Example:

    def __new__(cls, *args, **kwargs):
        print('new start')
        print(args)
        print(kwargs)
        print('new end\n')
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print('init start')
        print(first)
        print(second)
        print(third)
        print('init end')


ex = Example('data', 25, 3.14)
print(ex)
