def menu():
    print("[1]Pythagoras theorem")
    print("[2]converse Pythagoras theorem")
    print("[3]sides Pythagoras theorem")
    print()
menu()
selection_list = [1,2,3]
selection = int(input("enter a number[1,2,3]:"))
print()
if selection in selection_list:
    if selection == 1:
        a = int(input("enter 'a':"))
        b = int(input("enter 'b':"))
        a_squared = a*a
        b_squared = b*b
        c = a_squared + b_squared
        c_under_root = c**0.5
        print(f"the hypotenus is {c_under_root}")
        input()
    if selection == 2:
        d = int(input("enter 'a':"))
        e = int(input("enter 'b':"))
        f = int(input("enter 'c'"))
        d_squared = d*d
        e_squared = e*e
        f_squared = f*f
        if f_squared == (d_squared + e_squared):
            print("True,right angle at angle b")
        else:
            print("false,not a right angle")
        input()
    if selection == 3:
        g = int(input("enter 'a':"))
        i = int(input("enter 'c':"))
        g_squared = g*g
        i_squared = i*i
        h = i_squared-g_squared
        h_under_root = h**0.5
        print(f"side is {h_under_root}")
        input()
else:
    print("error:please enter on of the mentioned numbers")
    input()