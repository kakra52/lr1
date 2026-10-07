# колекція структури данних які дозволяють зберігати данні
#list список-впорядкована змінна колекція
# grades = [12,6,4,5,6]
# numders = []
# # numders2 = list()
# # print(grades[2])
# # # print(grades[5])
# # print(grades[len(grades)-1])
# # grades[2] = 6
# # print(grades)
# numders.append(5)
# numders.append(6)
# numders.append("6")
# numders.insert(1,2)
# numders.insert(10,2)
# numders.extend([5,6,5,"4"])
# numders.remove(5)
# if "6" in numders:
#     numders.remove("6")#за значенням
# #tuple кортеж
# rgb = (255,0,0)
#
# numders.pop(-1)#видалення за індексом
#
# del numders[2]
# #print(numders)
# #numders.clear() очистка
# print(numders.count(5))
# print(numders.index(6))
#
# print(2 in numders)
# len()#кількість
# min()
# max()
# sum()

# if len(numders) > 0:
#     average = sum(numders) / len(numders)


# numders.sort()#упорядку зростання
# print(numders)
# numders.sort(reverse= True)
# print(numders)
# print(sorted(numders))

# numders.reverse()
#
# print(numders[1:3])
# print(numders[::-1])
# print(numders[::2])

# for numder in numders:
#     print(numder)
# print(numders)

# digits = [-1,0,4,-5,3,-6]
# dodatni = []
# parni = []
# for digit in digits:
#     if digit >0:
#         dodatni.append(digit)
#     if digit % 2 ==0:
#         parni.append(digit)
# print(parni)
# print(dodatni)







#tuple кортежі - впорядкована незмінна колекція
# rgb = (255,0,0)
# r ,g ,b =rgb
# print(r,g,b)
#
# data = ()
# a = (1,)

# point = (4,-6)
# point = point + (4,)
# print(point)
# a = (30,40)
# b = (50,60)
# c = a + b
# c = a[:1] +b[::]
# print(c)
# c.count()
# c.index()
# len(c)


# set множина послідовність унікальних елементів нема послідовності

# subjects = {"Python","Html","CSS","JavaSkript"}
#
# data = {}
# data2 = set()
# data2.add("Python")
# data2.update(["Html","CSS"])
# print(data2)
# data2.remove("Html")
# data2.discard("C++")
# deleted = data2.pop()
# # clear()
#
# if "Python" in data2:
#     print("Python")
#
#
#
# print(data2)


# names = ["Ivan","Olha","Vadym","Ivan","Irina"]
# new_names = set(names)
# print(new_names)

# name1 = {"Ivan","Olha","Vadym"}
# name2 ={"Ivan","Irina"}
# name3 = name1 | name2#обєднання
# name4 = name1 & name2#перетин
# name5 = name1 - name2#віднімання
# name6 = name2 - name1
# print(name3)



#dict словник певна полідовність з пари значенн ключ і значення

# student = {
#     "name":"yaroslav",
#     "age": 18
# }

# products = ["bread", "cheese", "milk", "apple", "banana"]
# price = [30,50,50,80]
price = {
    "apple":50,
    "banana":70,
    "orange":50,
    "mango":100
}
student1 = {}
student2 = dict()
print(price["apple"])
price["tea"] =75
price.update(
    {
        "juce":560,
        "coffy":23442
    }
)
print(price)