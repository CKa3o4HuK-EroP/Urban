students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
# list(map(str, input("Введите имена учеников через пробел: ").split(' ')))
students.sort()
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# [[] for _ in students]
avg = dict()
for i in range(len(students)):
    # grades[i] = list(map(int, input(f"Введите оценки студента {students[i]} через пробел: ").split(' ')))
    avg[students[i]] = round(sum(grades[i]) / len(grades[i]), 2)
print(avg)
