import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
           return False
        elif you=='s':
            return True
    elif comp == 'p':
        if you == 's':
           return False
        elif you=='r':
            return True 
    elif comp == 's':
        if you == 'r':
           return False
        elif you=='p':
            return True               

print("comp turn : rock(r) paper(p) scissors(s)")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo ==2:
    comp='p'
elif randNo == 3:
    comp = 's'
    you = input("your turn: rock(r) paper(p) or scissors(s)?")
    a = gamewin(comp,you)
    print(f"computer choose{comp}")
    print(f"you choose{you}")
    if a == None:
        print("the game is a tai")
    elif a :
        print(" you win")
    else:
        print("you lose")