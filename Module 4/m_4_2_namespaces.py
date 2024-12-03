def test_function():
    def inner_function():
        print("Я в области видимости функции test_function!")
    inner_function()


print('Вызов тестовой функции.')
test_function()
print('Вывод внутренней функции.')
try:
    inner_function()
except:
    print('Ошибка области видимости.')
