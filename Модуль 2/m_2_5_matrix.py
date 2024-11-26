def getmatrix(n, m, value):
    M = [[value] * m for _ in range(n)]
    return M


n, m, value = map(int, input("Введите через пробел количество строк, столбцов и значение для заполнения: ").split())
M = getmatrix(n, m, value)
print(*M, sep='\n')