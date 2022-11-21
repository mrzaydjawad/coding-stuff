import matplotlib.pyplot as plt
x = [31,28,31,30,31,30,31,31,30,31,30,31]
y = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,y,c="black",linewidth=4,label="days in months")
plt.xlabel("days in months")
plt.ylabel("months")
plt.title("days in each month")
plt.legend()
plt.show()