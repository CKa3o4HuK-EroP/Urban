import random


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __str__(self):
        return f'Цветок, {self.name}'


class Fruit(Plant):
    edible = True

    def __str__(self):
        return f'Фрукт, {self.name}'


class Mammal(Animal):
    def __str__(self):
        return f'Травоядное, {self.name}'

    def eat(self, other):
        if isinstance(other, Plant):
            if other.edible:
                print(f'{self.name} съел {other.name}.')
                self.fed = True
        else:
            print(f'{self.name} не стал есть {other.name}.')
            self.alive = False


class Predator(Animal):
    def __str__(self):
        return f'Хищник, {self.name}'

    def eat(self, other):
        if isinstance(other, Mammal):
            print(f'{self.name} съел {other.name}.')
            self.fed = True
        elif isinstance(other, Predator):
            if random.randint(0, 1):
                print(f'{self.name} съел {other.name}.')
                self.fed = True
                other.alive = False
            else:
                print(f'{other.name} съел {self.name}.')
                other.fed = True
                self.alive = False
        elif other.edible:
            print(f'{self.name} съел {other.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {other.name}.')
            self.alive = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
