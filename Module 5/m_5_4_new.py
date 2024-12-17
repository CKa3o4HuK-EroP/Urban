class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')

    def go_to(self, floor):
        if 1 <= floor <= self.floors:
            for i in range(1, floor + 1):
                print(i)
        else:
            print("Такого этажа не существует.")

    def __str__(self):
        return f'Название: {self.name}; Кол-во этажей: {self.floors}'

    def __len__(self):
        return self.floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else:
            return self.floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else:
            return self.floors < other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            return self.floors > other

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        elif isinstance(value, House):
            self.floors += value.floors
        else: print('Impossible addition.')
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
