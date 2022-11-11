import fractions
pie = (22/7)
def mainMenu():
    print("1. cylinder")
    print("2. cone")
    print("3. sphere")
    print("0. exit")
def functions():
    selection = int(input("Enter choice: "))
    if selection==1:
        print("Size of cylinder")
        print("-------------")
        radius=float(input("Enter the base radius of the cylinder: "))
        cheight=float(input("Enter the height of the cylinder: "))
        volume = pie * radius * radius * cheight
        ccurvedarea = 2 * pie * radius * cheight
        ctotalarea = 2 * pie * radius * radius + 2 * pie * radius * cheight
        print("\n")
        print("Volume of cylinder")
        print("--------")
        print("The volume of the cylinder is : ",volume)
        print("--------")
        print("The total surface area of the cylinder is: ",ctotalarea)
    elif selection==2:
        print("Size of cone")
        print("------------")
        base = float(input("Enter the base radius of the cone: "))
        vheight = float(input("Enter the vertical height of the cone: "))
        sheight = float(input("Enter the slant height of the cone: "))
        volume = 1/3 * pie * base * base * vheight
        tsa = pie * base * base + pie * base * sheight
        print("\n")
        print("The volume of the cone is: ",volume)
        print("--------------~")
        print("The total surface area of the cone is: ",tsa) 
    elif selection==3:
            print("Size of sphere")
            print("----------")
            radius = float(input("Enter the radius of the sphere: "))
            volume = 4/3 * pie * radius * radius * radius
            tsa = 4 * pie * radius * radius
            print("\n")
            print("The volume of the sphere is: ",volume)
            print("----------------------------------~")
            print("The total surface area of the sphere is: ",tsa)
    elif selection == 0:
        exit
    else:
        print("invalid choice")
mainMenu()
functions()
input()