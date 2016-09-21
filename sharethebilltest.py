bill = float(input("Enter the total check amount: "))
tiprate = float(input("Enter tip percentage: "))
tip = bill *(tiprate/100)
guests = int(input("Enter guests: "))
total_pay = (bill + tip)/guests

print("Our total for each of us on the bill is %.2f" % (total_pay))

print(_1337)