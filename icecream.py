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
            break
        elif fv == 2:
            print("strawberry")
            break
        elif fv == 3:
            print("vanilla")
            break
        else:
            print("pls enter a valid icecream flavor")
            break
    restart = input("do you want to do it again?").lower()
    if restart == ("yes"):
        main()
    else:
        print("bye have a good day")

main()







