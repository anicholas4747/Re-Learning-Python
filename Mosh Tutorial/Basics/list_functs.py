nums = [1,2,3]
nums.append(7) # O(1)
print(nums)
nums.insert(0,42)  # O(n)
print(nums)
print(nums.pop()) # O(1)
print(nums)
print(len(nums)) # O(1)
nums.sort() # O(nlogn) [default is least to greatest]
print(nums)
print(7 in nums) # O(n)

freq = [
  [3, "a"],
  [7, "b"],
  [1, "c"],
]
freq.sort(key=lambda el: el[1])  # O(nlogn) [use lambda to specify how to sort]
print(freq)
freq.sort(key=lambda el: el[0], reverse=True)  # O(nlogn)[use reverse=True to get greatest to least]
print(freq)

