import random
yeslist = ("yes","yeah","sure","y","Y")
nolist = ("no","nah","n","N")
def question():
    st = input("would like to take a a stupidity test?(y/n)")
    if st in yeslist:
        rn = random.randint(1,100)
        print("you are ",rn,"%","stupid")
    elif st in nolist:
        print("ok bye")
    else:
        print("pls enter either (y/n)")
        print()
        start = input("would you like to take the program again?:")
        print()
        if start in yeslist:
            question()
        else:
            print("ok bye")
question()