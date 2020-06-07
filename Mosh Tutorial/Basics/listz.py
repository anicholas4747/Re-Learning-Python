# find the largest num in a list

def find_max(arr):
  max = None
  for n in arr:
    if (max == None) or (max < n):
      max = n
  return max

arr = [1,2,3,4,5]
print(find_max(arr))

arr = [6, 2, 3, 4, 5]
print(find_max(arr))

arr = [1, 2, 7, 4, 5]
print(find_max(arr))