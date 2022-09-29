def menu():
    print("[1]chocolate")
    print("[2]strawberry")
    print("[3]vanilla")
    print("[0]exit the program")
 
menu()
fv = int(input("pls enter your favorite icecream flavor"))
while fv !=0:
    if fv == 1:
        print("chocolate")
    elif fv == 2:
        print("strawberry")
    elif fv == 3:
        print("vanilla")
    else:
        print("pls enter a valid icecream flavor")
    
menu()
fv = int(input("pls enter your favorite icecream flavor"))

print("thank you for doing the survey")
        

