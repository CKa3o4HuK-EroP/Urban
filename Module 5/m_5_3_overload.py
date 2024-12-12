class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
