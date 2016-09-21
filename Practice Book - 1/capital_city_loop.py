from capitals import capitals_dict
import random

print("Guess write or say 'exit' to escape\n")

def find() :
    while True :
        c = random.choice(list(capitals_dict.keys()))
        user_input = str(input("What is the capital of : {} ".format(c)))
        if user_input.lower() == "Exit".lower():
            print("Goodbye")
            break
        elif user_input.lower() == capitals_dict[c].lower():
            print ("Correct ! {}'s capital is : {} \nGoodbye".format(c, user_input))
            break
        elif user_input.lower() != capitals_dict[c].lower() :
            print("Wrong ! {}'s capital is : {} ".format(c, capitals_dict[c]))
            continue
find()
