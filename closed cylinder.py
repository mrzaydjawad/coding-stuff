height = input("pls enter the height")
height = float(height)
radius = input("pls enter the radius")
radius = float(radius)
from fractions import Fraction
pie = Fraction(22,7)
radius_squared = radius*radius
volume = pie*radius_squared*height
surface_area = 2*pie*radius_squared+2*pie*radius*height
print(volume)
print(surface_area)
