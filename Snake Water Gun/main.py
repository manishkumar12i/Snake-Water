import random
# Snake water gun or Rock Paper Scissor

def gameWin(comp,you):
    # if two values are equal declare a tie
    if comp == you:
        return None

    # Check for all posiblity when computer choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # Check for all posiblity when computer choose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # Check for all posiblity when computer choose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print('Comp Turn: Snake(s) Water(w) or Gun(g)?')
randNo = random.randint(1,3)
# print(randNo)
if randNo ==1:
    comp = 's'
elif randNo == 2 :
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Player's Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("You loose!")
