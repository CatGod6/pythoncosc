from random import randint

def altside() :
    flip1 = randint(0,1)
    flips = 1
    while True :
        flips +=1
        if randint(0,1) != flip1 :
            break
        return flips

totalflips = 0

for i in range(10000) :
    totalflips = altside()
print( "To get Average sides of the coin it requires on average {} flips".format(totalflips/10000))
    
