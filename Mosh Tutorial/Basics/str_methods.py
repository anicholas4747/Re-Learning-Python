sent = "I wonder if you can guess how many characters are in this string"
print(sent)
print(f'There are {len(sent)} chars in that string')
print("-"*50)

print("I'm gonna scream the sentence:")
print(sent.upper())
print("-"*50)

print(f'Is the sentence all numbers? {sent.isnumeric()}')
print("-"*50)

print(f'The first "c" is at index {sent.find("c")}')
print("-"*50)

print(f'Now you\'re coding with {"Python".replace("P","J").replace("on","on, boi!")}')
print("-"*50)

print(f'Is there an ass is the classroom? {"ass" in "the classroom"}')
print("-"*50)

print(f'Are there COVID patients in JFK airport? {"COVID patients" in "JFK airport"}')
print("-"*50)