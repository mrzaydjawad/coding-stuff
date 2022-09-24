length = input("pls enter the length")
length = float(length)
width = input("pls enter the breadth")
width = float(width)
depth = input("pls enter the height")
depth = float(depth)
x = length*width
y = length*depth
z = depth*width
xx = x+y+z
total_surface_area = xx*2
volume = length*width*depth
print("the total surface area is",total_surface_area)
print("the total volume is",volume)

