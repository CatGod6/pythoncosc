"This is the famous cats with hats question. It's a pretty simple code!" 
cats = 100
laps = 100
catsH = []

def count() :
    for lap in range(1,laps+1) :
        for cat in range(1,cats+1) :
            if cat % lap == 0 :
                if cat  in catsH :
                    catsH.remove(cat)
                else :
                    catsH.append(cat)
    print(catsH)

count()

