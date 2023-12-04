# SNAKE WATER GUN GAME   OR     ROCK PAPER SCISSORS

import random       # it print random what u show this----NEW impp😀

def gamewin(comp,you):
    #If two values are equal , declare a tie!
    if comp == you:
        return None
    
    #check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
        
    #check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
        
    #check for all possibilities when computer chose g
    elif comp == 'g':
        if you =='w':
            return True
        elif you == 's':
            return False
    
print("comp turn : Snake(s) Water(w) or Gun(g) ?")
randomnumber = random.randint(1,3)    # random show 1,2 or 3------- NEW impp😀
if randomnumber == 1:
    comp ='s'
elif randomnumber == 2:
    comp = 'w'
elif randomnumber ==3:
    comp = 'g'

you = input("your turn : Snake(s) Water(w) or Gun(g) ?")
a = gamewin(comp,you)

print(f"Computer chose {comp}")  # it tell what comp chosen and you
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You win !")
else:
    print("You lose!")
