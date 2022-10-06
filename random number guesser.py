import random
print("guess the number program")
print("you should have a 10 percent chance of a guessing a number")
numlist = random.sample(range(1,100), 10)
numlist = int
urn = input("pls enter the random number you chose:")
if urn in numlist:
    print("wow you geussed a number correctly,congratulations!")
else:
    print("unfortunately your ans was wrong")
#a work in progress don't know how to fix this?
