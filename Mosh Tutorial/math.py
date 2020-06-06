print(10+3)     # returns 13
print("10"+"3") # returns "103"
print(10-3)     # returns 7
print(10*3)     # returns 30
print("10"*3)   # returna "101010"
print(10**3)    # returns 1000
print(10/3)     # returns 3.333333
print(10//3)    # returns 3
print(10%3)     # returns 1
print(10.1%3)   # returns 1.1

x = 10
x += 3
print(x) # 13

y = 1.49
print(round(y)) # rounds down
y = 1.5
print(round(y))  # rounds up

print(abs(-123456789))

num = 255
print(bin(num)) # "0b11111111" aka a bunch of zeros until first 1, then binary rep of num
num <<= 1 # left shift 1 is the same as multiplying by 2^1
print(num) # 510
num >>= 2 # right shift 2 is the same as dividing by 2^2
print(num) # 127
