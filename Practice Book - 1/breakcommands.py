print("To quit enter 'q' or 'Q'")

while True :
    phrase_input = input("Enter a word")
    if phrase_input == "q" or phrase_input == "Q" :
        break

for i in range(1,51) :
    if i % 3 == 0 :
        continue
    print(i)
    
        
