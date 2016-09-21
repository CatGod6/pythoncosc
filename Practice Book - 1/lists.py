desserts_list = ["ice cream" , "cookies"]
print(desserts_list)
desserts_list.sort()
print(desserts_list)
print(desserts_list.index("ice cream"))
food = []
food.extend(desserts_list)
print(food)
food.extend(["brocoli" , "turnips"])
print(food,desserts_list)
food.remove("cookies")
print(food)
print(food[0:2])
string = "cookies, cookies, cookies"
breakfast = string.split(",")
print(breakfast)

def numbers() :
    list_num = [2,4,20,19,30,94]
    for i in range(len(list_num)) :
        if list_num[i] <= 20 :
            print(list_num[i])
print(numbers())
