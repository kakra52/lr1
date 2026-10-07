group_info = ("10-IT", "2026/2027")

students = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9],
    "Olha": [12, 11, 10, 12, 11]
}

correct = True

for name, grades in students.items():
    if len(grades) != 5:
        correct = False

    for grade in grades:
        if grade < 1 or grade > 12:
            correct = False

if correct:
    print("Усі дані правильні")
else:
    print("Помилка в оцінках")

print("\nСередні бали:")

for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, "—", round(average, 1))

rating = []

for name, grades in students.items():
    average = sum(grades) / len(grades)
    rating.append((average, name))

rating.sort(reverse=True)

print("\nРейтинг:")

for average, name in rating:
    print(name, "—", round(average, 1))

best_average, best_student = rating[0]

print("\nНайкращий учень:", best_student)
print("Середній бал:", round(best_average, 1))

print("\nГрупа:", group_info[0])
print("Навчальний рік:", group_info[1])