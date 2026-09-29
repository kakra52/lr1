a = int(input("введіть ціле число"))
if a % 2 == 0 :
    print("Ділиться націло")
else :
    print("Не ділиться націло")
b = int(input("введіть свій вік"))
if b >= 18 :
    print("Ви повнолітні!")
else :
    print("Ви неповнолітній!")
c = float(input("введіть радіус кола"))
r = c*3.14*2
s = c*c*3.14

print("довжина кола", r )
print("площа кола", s )

d = float(input("введіть число а"))
f = float(input("введіть число б"))

if d > f:
    print(d)
elif f > d:
    print(f)
else:
    print("d == f")