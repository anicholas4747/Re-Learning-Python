arr = [1,8,1,2,3,4,1,1,4,2,5,6,7,9,2,8]

# uniqs = set()

# for num in arr:
#   if num in uniqs: # O(1) check if set has value
#     continue
#   uniqs.add(num) # O(1) operation to add value to set

# uniqs.remove(6) # O(1) operation to delete value from set
# print(uniqs)

print(set([num for num in arr])) # you can initialize a set w values by passing them in as an array to constructor