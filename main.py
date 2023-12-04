# SNAKE WATER GUN GAME   OR     ROCK PAPER SCISSORS

import random       

def gamewin(comp,you):
    
    if comp == you:
        return None
        
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
        
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
        
    elif comp == 'g':
        if you =='w':
            return True
        elif you == 's':
            return False
    
print("comp turn : Snake(s) Water(w) or Gun(g) ? ")
randomnumber = random.randint(1,3)   
if randomnumber == 1:
    comp ='s'
elif randomnumber == 2:
    comp = 'w'
elif randomnumber ==3:
    comp = 'g'

you = input("your turn : Snake(s) Water(w) or Gun(g) ?")
a = gamewin(comp,you)

print(f"Computer chose {comp}")  
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You win !")
else:
    print("You lose!")
