import random

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose rock
    elif comp == 'rock':
        if you=='scissor':
            return False
        elif you=='paper':
            return True
    
    # Check for all possibilities when computer chose paper
    elif comp == 'paper':
        if you=='rock':
            return False
        elif you=='scissor':
            return True
    
    # Check for all possibilities when computer chose scissor
    elif comp == 'scissor':
        if you=='paper':
            return False
        elif you=='rock':
            return True

print("Comp Turn: rock paper or scissor!")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'rock'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

you = input("Your Turn: rock paper scissor!")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")