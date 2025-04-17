import random

def rolldice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f'total of dice {total}')
 



def simulation_roll():
    dice1: int= 10
    print("die1 in main() starts as: " + str(dice1))
    for i in range (3):
        print(f"Roll # {i}")
        total =rolldice()



simulation_roll()