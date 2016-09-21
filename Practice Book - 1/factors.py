number = int(input("Enter a number a positive number:"))

for i in range(1,number+1) :
    if number % i == 0 :
        print(" {0} is a divisor of {1} ".format(i, number))



