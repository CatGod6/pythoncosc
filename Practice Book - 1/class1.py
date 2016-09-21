class Dog(object):

    #Class Attribute , What is it?
    species = 'mammal'

    #Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog Object
phil = Dog("Phil",5)
mikey = Dog("Mikey",6)
leslie = Dog("Leslie",7)
catrell = Dog("Catrell",9)
rohaun = Dog("Rohaun",3)

def oldest_number() :
    highest = [phil,mikey,leslie,catrell,rohaun]
    old = sorted(highest)
    print(max(old))
    

# Access the instance attributes , In this case NAME , AGE
print("{} is {} and {} is {}.".format(
    phil.name, phil.age, mikey.name, mikey.age))

# Is phil a mammal?
if phil.species == "mammal":
    print("{} is a {}!".format(phil.name, phil.species))

oldest_number()
