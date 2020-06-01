import random

class Die():
    def __init__(self, sides=6):
        self.sides =  sides
    def roll_die(self):
        print("Dice roll is", random.randint(1, self.sides))

die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

for i in range(0, 10):
    ten_die.roll_die()

for i in range(0, 10):
    twenty_die.roll_die()
