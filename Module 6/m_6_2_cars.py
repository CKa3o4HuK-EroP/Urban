class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'cyan']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power
        pass
    def get_model(self):
        return f'Модель: {self.__model}'
        pass
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
        pass
    def get_color(self):
        return f'Цвет: {self.__color}'
        pass
    def print_info(self):
        print('___________________________')
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
        print('___________________________')
        pass
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            print(f'{self.__color} {self.__model} был перекрашен в {new_color}')
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
