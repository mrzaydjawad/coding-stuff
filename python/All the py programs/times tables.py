print("in this program you will enter a number and the tables of the number will be shown")
print()
number = float(input("pls enter a number:"))
multi = 1
a = 1
while multi != 12:
    multi += 1
    x = number*multi
    a += 1
    x = round(x,2)
    print(f"{a}~~ {x} ~~")