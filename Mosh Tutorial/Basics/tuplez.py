# immutable lists
# once defined, you can only get informatino about them

tup = (1,2,3,1,1,1)
print(tup[:4])
print(tup.count(1))
print(tup.index(3))

# unpacking / object deconstruction
coord = (1,2,3)
x,y,z = coord
print(f"x:{x}, y:{y}, z:{z}")

# unpacking works for lists too
arr = ["hello", "world"]
str1, str2 = arr
print(str1 + " " + str2)

# swapping is similar to js without outer brackets
nums = [1,2,3]
print(nums)
nums[0], nums[2] = nums[2], nums[0]
print(nums)