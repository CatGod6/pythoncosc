def my_first_kata(a,b):
    #if type(a) or type(b) == str: 
    #    return False
    if type(a) == int and type(b) == int:
        c = (a % b) + (b % a)
        return c
    else:
    	return False l
print(my_first_kata(5,3))