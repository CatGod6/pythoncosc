phrase= "Hello, World"
print(phrase)
""" Alright so this is my first official script in python

Gotta say this coding language is dope as hell!"""

phrase = "GAAAAY"

print(phrase)

""" The line above this prints out GAAAY :))))) """

phrase = "Hello, World"

my_string = "We're #1"

string_number = "1234"

conversation = 'I said, "Put it over by the llama."'

long_string = ''' This is a strig that spans accross multiple lines '''


print(long_string)
my_long_string = "Here's a string that I want \
write accorss multiple lines since it is too long."


print(my_long_string)


# CONCATENATION & FORMATING

string_length = len(my_long_string)

print(string_length)

string1 = "abra"
string2 = "cadabra"

magic_string = string1 + string2

print(magic_string)

print(magic_string[3])

print(magic_string[0])

print(magic_string[0:4])

print(magic_string[4:])

print(magic_string[:4])

loud_voice = "Can you hear me yet?"
print(loud_voice.upper())

response = input("Hey, what's up?")
response = response.upper()
print("Your response's first letter is:" , response[0])

my_number = "12"
print(int(my_number))

num_arms = 2
num_heads = 1
num_feet = 2

print("{0} has {1} heads and {2} arms".format(loud_voice, num_heads, num_arms))

print("Hey man back off of my girl you gay boy".replace("gay" , "funny"))

# ARETHMATIC

print("1+1=", 1+1)
print("2*(2+3) =", 2 * (2+3))

base = input("Enter a base: ")
exponent = input("Enter the exponent")

base = float(base)
exponent = float(exponent)
product = base**exponent

print("{0} to the power of {1} = {2}".format(base, exponent, product))

def square(number) :
    sqr_num = number**2
    return sqr_num


print(square(10))

def cube(num1) :
    cube_num = num1*num1*num1
    return cube_num


return_value = cube(20)

print(return_value)

