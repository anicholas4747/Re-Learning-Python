print("I bet I can guess any integer you're thinking about")
low = int(input("What's the smallest num it can be? "))
high = int(input("What's the largest num it can be? "))

while (low > high):
  print("Come on, that's not a valid range")
  high = int(input("What's the real largest num it can be? "))
else:
  print("All right, all set\n")

num_guesses = 0
got_it = False

while (not got_it) and (low < high):
  guess = (high + low) // 2
  num_guesses += 1
  res = input(f"Is it {guess}? (Y)es, Too (H)igh, or Too (L)ow: ").lower()
  if res == "y":
    got_it = True
  elif res == "h":
    high = guess
  elif res == "l":
    low = guess + 1
  else:
    print("\nCome on, tell me how I did")
    num_guesses -= 1

if got_it:
  print(f"\nAha! Knew I could do it, and it only took me {num_guesses} tries!")
else:
  print("\nYou must've changed the number or something, I give up")
