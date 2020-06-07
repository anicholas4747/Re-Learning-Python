def convert(num,units):
  if units == "k":
    print(f"You are {num*2.2} lbs")
  else:
    print(f"You are {num/2.2} kg")

amt = float(input("How much do you weigh? "))
sys = input("Is that in (L)bs or (K)g? ").lower()
convert(amt,sys)