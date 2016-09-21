my_input_file = open("hello.txt" , "r")
print(my_input_file.readlines())
my_input_file.close()

my_input_file = open("hello.txt" , "r")

for line in my_input_file.readlines() :
    print(line, end="")

my_input_file.close()

my_input_file = open("hello.txt" , "r")
line = my_input_file.readline()
while line != "" :
    print(line) ,
    line = my_input_file.readline()

my_input_file.close()

with open("hello.txt" , "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line),
