
yeslist = ("yes","y","Y")
print("size of the pond")
print("----------------")
width = input("pls enter the width:")
width = float(width)
length = input("pls enter the length:")
length = float(length)
depth = input("pls enter the depth:")
depth = float(depth)
surface_area = width*length
size = surface_area*depth
print("the volume of the pond is ",size)
print()
print("filling the pond")
print("----------------")
second = input("pls enter the liters per second:")
second = float(second)
hour = second*3600
hours = hour/1000
htftp = size/hours
htftp = round(htftp,2)
days = htftp/24
days = int(days)
dais = days*24
hl = htftp-dais
hl = round(hl,2)
print("the liters per hour is:",hour)
print("the cubic meters per hour is:",hours)
print("it will take ",days," days and ",hl," hours to fill the pond")
print()
print("evaporation")
print("-----------")
evaporation = float(surface_area * 75/1000)
evaporation = round(evaporation,2)
print("cubic meters of water lost per month:",evaporation)
print()
print("rainfall")
print("--------")
rainfall = float(input("pls enter the rainfall (in milimeters):"))
rain = surface_area * rainfall/1000
rain = round(rain,2)
print("cubic meters of rain added:",rain)
print()
print("change to the pond")
print("------------------")
seapage = 20*surface_area
seepage = seapage/1000
lof = evaporation+seepage
change = rain-lof
change = round(change,2)
new_volume = size+change
print("the change to the pond is:",change)
print("the new volume of water in the pond is ",new_volume)
Q = input("do you want the monthly?: ")
if Q in yeslist:
    pass
else:
    print("bye")