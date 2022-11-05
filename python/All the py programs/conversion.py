from decimal import Decimal
no = float(input("pls enter a number:"))
no_litre = no/1000
no_cubic_metre = no/1000000
print()
print("the cubic meters is ",Decimal(no_cubic_metre))
print()
print("the liters is ",Decimal(no_litre))
