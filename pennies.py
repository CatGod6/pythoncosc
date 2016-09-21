#Let's make an exponential function named Penny Counter!
#This function counts pennies exponentially to the end of the range!

print("Welcome to penny counter!")
raw_input = int(input("How many days do you want us to count for?: "))

pennies = 0
for i in range(1,raw_input+1):
	pennies = pennies + i

print("After {} days, you will have {} pennies!".format(raw_input, pennies))