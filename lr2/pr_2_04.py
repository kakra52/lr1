width = int(input("Введіть ширину: "))
height = int(input("Введіть висоту: "))
border = input("Введіть символ контуру: ")
inside = input("Введіть символ всередині: ")

if width < 3 or height < 3:
    print("Помилка: мінімальний розмір рамки 3 x 3")
else:
    for row in range(height):
        for column in range(width):
            if (
                row == 0
                or row == height - 1
                or column == 0
                or column == width - 1
            ):
                print(border, end="")
            else:
                print(inside, end="")

        print()