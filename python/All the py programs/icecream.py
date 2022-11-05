nolist = ["no","nein","neyet","nah","no thank you","na","n","N"]
yeslist = ["yes","y","sure","Y"]
def main():
    def menu():
        print("[1]chocolate")
        print("[2]strawberry")
        print("[3]vanilla")
        print("[0]exit the program")
    menu()
    fv = int(input("pls enter your favorite icecream flavor"))
    while fv != 0:
        if fv == 1:
            print("chocolate")
            start()
            break
        elif fv == 2:
            print("strawberry")
            start()
            break
        elif  fv == 3:
            print("vanilla")
            start()
            break
        else:
            print("pls enter a valid icecream flavor")
            start()
            break
def start():
        restart = input("do you want to do it again?(Y/N)").lower()
        if restart in yeslist:
            main()
        elif restart in nolist:
            print("bye have a good day.")
        else:
            print("pls enter yes or no")
            print()
            start()
main()