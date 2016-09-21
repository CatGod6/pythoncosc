from random import randint

heads = 0
tails = 0

for trials in range(0, 10000) :
    while randint(0,1) == 0:
        tails += 1
    heads += 1

print("heads / tails = ", heads/tails)    

for dice in range(0,5) :
     output = randint(1,6)
     print(output)

average = 0

for i in range(0,10000) :
    average += randint(1,6)
print(average/10000)

        
