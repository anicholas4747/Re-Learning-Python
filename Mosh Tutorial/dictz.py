# dictionaries = hash maps

person = {"name": "Joe Doe", "age": 27, "is_weeb": False, "fave_ppg": "Bubbles"}

#person["undefined_key"] # throws error
person.get("undefined_key")  # returns None
print(person["name"]) # retrieve existing key
person["is_weeb"] = True # re-assign existing key
person["fave_anime"] = "Death Note" # assign new key-value pair
print(person)
print(person.keys())  # returns list of hash keys
print(person.values()) # returns list of hash values

for val in person.values():
  print(val)

freq = {}
sent = "here is a sentence, now build the char frequency"
for char in sent:
  freq[char] = freq.get(char,0) + 1 # using get, you can say (curr value or 0) + 1
print(freq)