str1 = "Sara's Shell Shop"
print(str1)
print("-" * 50)

str2 = 'Sara and her "Shell" Shop'
print(str2)
print("-" * 50)

str3 = 'Sara\'s "Shell" Shop'
print(str3)
print("-" * 50)

str4 = 'Sara\'s\t"Shell"\tShop'
print(str4)
print("-" * 50)

str5 = 'Sara\'s\n"Shell"\nShop'
print(str5)
print("-" * 50)

str6 = '''
  Sara's "Shell" Shop
  P. Sherman
  42 Wallaby Way
  Sydney, Australia
'''
print(str6)
print("-" * 50)

alphabet = "abcdefghijklmnopqrstuvqxyz"
print(alphabet[0])
print(alphabet[5])
print(alphabet[-1])
print(alphabet[-2])
print(alphabet[1:4])
print(alphabet[:5])
print(alphabet[15:])
print(alphabet[-5:])
print(alphabet[:])
print("-" * 50)

# string interpolation
name = "Jaxson"
age = 47
msg = f'{name} is {age} years old'
print(msg)