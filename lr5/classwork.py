# def say_hello():
#     print("Hello World")
#
# say_hello()
#
#
# def say_hello(name):
#     print(f'Hello {name}!!!')
#
# say_hello("Ivan")
# say_hello("Oleg")
#
#
# def rectangle_area(width, height):
#     return width * height
#
# width = int(input("Введіть ширину прямокутника: "))
# height = int(input("Введіть висоту прямокутника: "))
#
# S = rectangle_area(width, height)
#
# print(f"Площа дорівнює {S} см2")
#
#
# def hello_world(name, message='Hello World!'):
#     print(f'Hello {name}, your message is {message}!!!')
#
# hello_world('Ivan', "Python")
#
#
# def price_with_discount(price, discount=0):
#     return price - price * discount / 100
#
# print(price_with_discount(1000))
#
#
# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_, max_ = min_max(numbers)
#
#
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(3))
# print(is_even.__doc__)
#
#
# def rectangle_area(width, height):
#     return width * height
#
# def main():
#     width = float(input("width: "))
#     height = float(input("height: "))
#
#     print(f'Ширина, {width}')
#     print(f'Висота, {height}')
#     result = rectangle_area(width, height)
#     print(f'Площа прямокутника: {result}')
#
# main()