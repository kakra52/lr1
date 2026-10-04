full_name = input("Введіть прізвище, ім'я та по батькові: ")

parts = full_name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name = parts[1].capitalize()
    patronymic = parts[2].capitalize()

    result = surname + " " + name[0] + "." + patronymic[0] + "."
    print(result)
else:
    print("Помилка: потрібно ввести прізвище, ім'я та по батькові.")
