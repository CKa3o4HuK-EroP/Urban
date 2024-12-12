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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))