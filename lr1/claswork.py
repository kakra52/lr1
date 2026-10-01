# a = 12       # int
# b = 12.43    # float
# c = "12"     # str
# d = True     # bool

# Арифметичні оператори:
# +  додавання
# -  віднімання
# *  множення
# /  ділення
# // цілочисельне ділення
# %  остача від ділення
# ** піднесення до степеня

# print(a)
# n = int(input("Введи число: "))
# m = int(input("Введи число: "))
# print(n + m)#Конкатинація- додавання двох або більше стрінгових частин

# a = int(input())
# b = int(input())
# a, b =map(int, input().split(", "))
# print(a + b)
# < > <= >= !=
# or and not
a = int(input())
b = int(input())
c = int(input())

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("a == b")
print(max(a, b , c))
print(min(a, b , c))
