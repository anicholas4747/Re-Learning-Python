import random

class Dice:
  def __init__(self):
    pass

  def roll(self):
    die1 = random.randint(1,6)
    die2 = random.randint(1, 6)
    return (die1,die2)

newDice = Dice()
print(newDice.roll())