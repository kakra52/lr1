a, b = map(int, input().split())
if a > 0 and b > 0:
    print('в першій чверті')
elif a < 0 and b > 0:
    print('в другій чверті')
elif a < 0 and b < 0:
    print('в третій чверті')
else:
    print('в четвертій чверті')