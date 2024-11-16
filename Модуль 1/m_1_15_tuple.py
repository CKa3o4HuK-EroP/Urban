immutable = tuple(range(1, 11, 2))
print('Immutable tuple:', immutable)
# immutable[0] = 5
# Ошибка. Элементы кортежа нельзя изменять напрямую,
# поскольку кортеж является неизменяемым типом данных.
mutable = [str(i) for i in range(2, 24, 4)]
mutable.append('Modified')
print("Mutable list: ", mutable)