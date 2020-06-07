mapping = {
  "0": "zero",
  "1": "ichi",
  "2": "ni",
  "3": "san",
  "4": "yon",
  "5": "go",
  "6": "roku",
  "7": "nana",
  "8": "hachi",
  "9": "kyuu"
}

phone_num = input("Ay girl, konnichi wa, what's yo number: ")
phone_arr = []
for num in phone_num:
  phone_arr.append(mapping.get(num,"NaN"))
print(" ".join(phone_arr))
print("Aight, Imma call you later")
