group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

both = group1 & group2
only_group1 = group1 - group2
only_group2 = group2 - group1
all_people = group1 | group2

print("Спільні:", both)
print("Тільки group1:", only_group1)
print("Тільки group2:", only_group2)
print("Усі:", all_people)