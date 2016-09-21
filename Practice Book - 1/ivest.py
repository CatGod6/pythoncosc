def invest(amount, rate, time) :
         total= 0;
         for i in range(time) :
             total= amount+(amount * rate)
             amount = total
             print("Year  " , str(i) , ":" , total)


amount_i = input("principal amount?:")
rate_i = input("annual rate?:")
time_i= input("How many years?:")

print(invest(float(amount_i),float(rate_i),int(time_i)))
print(invest(float(amount_i),float(rate_i),int(time_i)))
