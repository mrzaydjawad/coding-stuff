import random
yeslist = ("y","Y")
nolist = ("n","N")
def question():
    st = input("would like to take a a stupidity test?(y/n)")
    if st in yeslist:
        rn = random.randint(1,100)
        print(f"you are {rn}% stupid")
    elif st in nolist:
        print("ok bye")
    else:
        print("pls enter either (y/n)")
question()
input()