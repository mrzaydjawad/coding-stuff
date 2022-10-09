radius = input("pls enter the radius")
radius = float(radius)
from fractions import Fraction
fr1 = Fraction(4,3)
pie = Fraction(22,7)
radius_squared = radius*radius
radius_cubed = radius*radius*radius
surface_area = 4*pie*radius_squared
volume = fr1*pie*radius_cubed
print("the area for the sphere is", volume)
print("the surface area for the sphere is", surface_area)
