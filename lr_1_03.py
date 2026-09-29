a = int(input("введіть вік"))
if a > 120:
    print("вік не вірний")
else:
    if a % 10 == 1 and a != 11 :
        print("рік",a)
    elif a % 10 == 2 and a % 10 == 3 and a % 10 == 4 and a != 12 and a != 13 and a != 14:
        print("роки", a)
    else:
        print("років", a)