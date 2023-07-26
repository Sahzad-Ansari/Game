import random

def gameWin(computer,you):
    if computer== you:
        return None
    elif computer == "s":
        if you =="w":
            return False
        elif computer == "g":
            return True
    elif computer == "w":
        if you =="g":
            return False
        elif you == "s":
            return True
    elif computer == "g":
        if you =="s":
            return False
        elif you == "w":
            return True
print("computer turn : sanke(s) water(w) gun(g)?")
randNO=random.randint(1,3)
if randNO ==1:
            computer="s"
elif randNO == 2:
            computer ="w"    
elif randNO == 3 :
            computer= "g"    

you = input("your turn: sanke(s) water(w) gun(g)?")
a=gameWin(computer,you)    
print(f"computer chose {computer}")
print(f"you chose {you}")

if a== None:
    print("the game is tie!")
elif a:
    print( "you win")    
else :
    print("you lose")    