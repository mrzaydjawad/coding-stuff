def menu():
    print("[1] cube")
    print("[2] cuboid")
    print("[3] sphere")
    print("[4] closed cylinder")
    print("[0] exit the program")


menu()
option = int(input("enter the shape you wanna find the area and total surface area of:"))

while option != 0:
    if option == 1:
        length = input("pls enter the length:")
        length = float(length)
        area = length*length*length
        surface_area = length*length*6
        print("the area of the cube is ",area)
        print("the total surface area of a cube is ",surface_area)
    elif option == 2:
        length = input("pls enter the length:")
        length = float(length)
        width = input("pls enter the breadth:")
        width = float(width)
        depth = input("pls enter the height:")
        depth = float(depth)
        x = length*width
        y = length*depth
        z = depth*width
        xx = x+y+z
        total_surface_area = xx*2
        volume = length*width*depth
        print("the total surface area is",total_surface_area)
        print("the total volume is ",volume)
    elif option == 3:
        radius = input("pls enter the radius:")
        radius = float(radius)
        from fractions import Fraction
        fr1 = Fraction(4,3)
        pie = Fraction(22,7)
        radius_squared = radius*radius
        radius_cubed = radius*radius*radius
        surface_area = 4*pie*radius_squared
        volume = fr1*pie*radius_cubed
        print("the area for the sphere is ",volume)
        print("the surface area for the sphere is ",surface_area)
    elif option == 4:
        height = input("pls enter the height:")
        height = float(height)
        radius = input("pls enter the radius:")
        radius = float(radius)
        from fractions import Fraction
        pie = Fraction(22,7)
        radius_squared = radius*radius
        volume = pie*radius_squared*height
        surface_area = 2*pie*radius_squared+2*pie*radius*height
        print("the total volume of the closed cylinder is ",volume)
        print("the total surface area of the closed cylinder is ",surface_area)
    else:
        print("invalid option.")

print()
menu()
option = int(input("enter the shape you wanna find the area and total surface area of:"))

print("bye and have a wondefull day")
