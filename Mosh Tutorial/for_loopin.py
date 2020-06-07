for c in "string":
  print(c)

prices = [10,20,30]
amount = [6,3,4]
total = 0
for i in range(len(prices)):
  total += (prices[i] * amount[i])
print(f"The total is {total}")

nums = [5,2,4,2,2]
for num in nums:
  str = ""
  for i in range(num):
    str += "x"
  print(str)