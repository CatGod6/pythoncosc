from random import random

cA = 0
cB = 0

for trials in range(0,10000) :
    if (random() < .87) + (random() <.65) + (random()<.13) >= 2:
        cA +=1
    else :
            cB +=1
print (" A wins {}, B wins {} out of {} elections. Chance that A wins is : {} ".format(cA, cB, cA + cB, cA / (cA + cB)))
