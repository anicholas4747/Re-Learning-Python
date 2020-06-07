# try except blocks to catch certain errors

while True:
  try:
    age = int(input("Enter your age: "))
  except ValueError:
    print("Invalid Input")
  else:
    break

print(f"Coool, I'm {age} years old too!")