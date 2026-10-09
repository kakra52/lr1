def average(grades):
    return sum(grades) / len(grades)


def minimum(grades):
    return min(grades)


def maximum(grades):
    return max(grades)


def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count


def main():
    grades = [10, 8, 12, 9, 11]
    value = int(input("Поріг: "))

    print("Оцінки:", grades)
    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print(f"Вище {value}:", count_above(grades, value))


main()