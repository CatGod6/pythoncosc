"""
Catrell Rashad Washington
CSCE 1306
Sharing the bill
Fall 2016
This script computes the total price of a bill with a tip
"""

#def main():
check = float(input("Enter the check amount (* No commas *) : "))
tip = float(input("Enter the tip percentage: "))
guests = int(input("Enter the amount of guests: "))
pay = float((check + check*tip/100)/guests)
print("You must each pay $%.2f" % (pay))

#if __name__ == "__main__":
#	main()