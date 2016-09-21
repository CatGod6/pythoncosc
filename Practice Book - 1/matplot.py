from matplotlib import pyplot as plt
from numpy import arange


x_points = arange(1,21) # arranges 20 x points
baseline = arange(0,20) # arranges 20 points

plt.plot(x_points, baseline**2, "b-x", x_points, baseline, "r-^") #our line segments that we need
plt.axis([0,21,0,400]) #Our restrictions for the graph (MIN X, MAX X, MIN Y, MAX Y)

plt.title("Amount of Python learned over time")
plt.xlabel("Days")
plt.ylabel("Standerdized knowledge index score")
plt.legend(("Real Python" , "Other course"), loc=2)
plt.show()
