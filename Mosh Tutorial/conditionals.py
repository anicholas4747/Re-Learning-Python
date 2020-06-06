import random

temp_f = random.randint(25,95)

print(f'It is {temp_f} degrees (F) outside')

if temp_f > 75:
  print("It's pretty warm today, remember to drink lots of water!")
elif temp_f < 60:
  print("It's pretty chilly today, remember to wear layers!")
else:
  print("It's a lovely day!")

print("Enjoy your day :)")
print("-"*50)

has_high_income = True
has_good_credit = False
has_a_cosigner = True

if (has_high_income and has_good_credit):
  print("Eligible for a business loan!")
elif (has_high_income and has_a_cosigner) or (has_good_credit and has_a_cosigner):
  print("Eligible for a personal loan!")
else:
  print("GTFO OF MY OFFICE")
print("-"*50)

print("Scope is crazy in Python")

if True:
  print("Variables defined in here")
  can_be = "can be accessed out here"

print(can_be)
print("-"*50)

# Falsey values in Python:
#   False, 0, None, Empty lists[], Empty tuples(), Empty dictionaries {}, 
#   Empty sets set(), Empty strings "", Empty ranges range(0)

money = 1000
broke = not(bool(money))
if not broke:
  print("You got shmoney!")