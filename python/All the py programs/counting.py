num = 0
special_num = int(input("pls enter a number:"))
while num < special_num:
    print(num)
    if (special_num>0):
        num += 1
while num > special_num:
    print(num)
    if (special_num<0):
        num -= 1