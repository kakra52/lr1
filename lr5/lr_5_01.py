def circle_area(radius):
    return 3.14159 * radius ** 2


def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return base * height / 2


def main():
    figure = input("Фігура: ").lower()

    if figure == "круг":
        radius = float(input("Радіус: "))
        print("Площа круга:", circle_area(radius))
    elif figure == "прямокутник":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        print("Площа прямокутника:", rectangle_area(width, height))
    elif figure == "трикутник":
        base = float(input("Основа: "))
        height = float(input("Висота: "))
        print("Площа трикутника:", triangle_area(base, height))
    else:
        print("Невідома фігура")


main()