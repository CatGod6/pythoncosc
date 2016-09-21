from matplotlib import pyplot as plt
from numpy import random

plt.hist(random.randn(10000),20)

plt.annotate("expected mean", xy=(0, 0), xytext=(0, 300), ha="center",
             arrowprops=dict(facecolor='white'), fontsize=20)

path = "C:/Python35/"
plt.savefig(path + "histogram.png")
plt.savefig(path + "histogram.pdf")

plt.show()
