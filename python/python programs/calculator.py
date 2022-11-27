def calculation_menu():
    print("[1]addition:")
    print("[2]subtraction:")
    print("[3]multiplication:")
    print("[4]devision:")
print("CALCULATOR")
print("----------")
print()
no_1 = float(input("pls enter a number:"))
print()
calculation_menu()
print()
calculation_selection = int(input("pls elect 1 / 2 / 3 / 4:"))
print()
no_2 = float(input("pls enter the other number:"))
if calculation_selection == 1:
    add_ans = no_1 + no_2
    print("the answer is ",add_ans)
if calculation_selection == 2:
    minus_ans = no_1 - no_2
    print("the answer is ",minus_ans)
if calculation_selection == 3:
    multiply_ans = no_1 * no_2
    print("the answer is ",multiply_ans)
if calculation_selection == 4:
    divide_ans = no_1 / no_2
    print("the answer is ",divide_ans)
else:
    print("pls enter either 1/2/3/4")
input()