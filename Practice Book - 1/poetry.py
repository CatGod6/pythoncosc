import random

noun = ["fossil" , "horse" , "aardvark" , "chef" , "judge"]
verb= [ "kicks", "jingles", "bounces", "slurps", "meows"]
adjs= ["fury" , "balding" , "incredulous" , "fragant"]
prep= ["against" , "after" , "into" , "beneath" , "for", "in"]
ads= ["curiously" , "extravagantly" , "furiously" , "sensuously"]
 
def selectn(list, n) :
    selection = []
    while (len(selection) != n) : 
        w = random.choice(list)
        if w not in selection :
            selection.append(w)
    return selection
# ERROR FIXED WOOO!
def makePoem() :
    my_nouns = selectn(noun,3)
    my_verbs = selectn(verb,3)
    my_adj = selectn(adjs,3)
    my_adverb = selectn(ads,1)
    my_prepo = selectn(prep,2)
    
    print ("A {} {}".format(my_adj[0], my_nouns[0]))
    print("")
    print("A {} {} {} {} the {} {}".format(my_adj[0], my_nouns[0], my_verbs[0], my_prepo[0], my_adj[1], my_nouns[1]))
    print("{}, the {} {}".format(my_adverb[0], my_nouns[0], my_verbs[1]))
    print("the {} {} {} a {} {}".format(my_nouns[1], my_verbs[2], my_prepo[1], my_adj[2], my_nouns[2]))
makePoem()    
