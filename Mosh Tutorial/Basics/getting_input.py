print("Hello, what's your name? ")
name = input("> ")
print("Cool, it's nice to meet you, " + name + "!")
print("-" * 50)
print("Guess what, " + name)
print("I can print a bunch of numbers!")
s = int(input("Where should I start? "))
e = int(input("Where should I stop? "))

print("Okay, here goes!")
# range is exclusive of the end
for i in range(s,e+1):
  print(i)