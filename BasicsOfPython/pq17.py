# 1Q. Print numbers from 1 to 100.

n = 1

while n <= 100:
    print(n)
    n += 1

# 2Q. Print numbers from 100 to 1.

r = 100

while r >= 1:
    print(r)
    r -= 1

# 3Q. Print the Multiplication table of number n.

n = int(input("Enter N num : "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


''' 4Q. Print the elements of the following list using a Loop :
  [1,4,9,16,25,36,49,64,81,100]'''

nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["ironman", "thor", "superman", "batman", "spiderman"]

idx = 0

while idx < len(nums):
    print(nums[idx])

    idx += 1

 
idxx = 0

while idxx < len(heroes):
    print(heroes[idxx])
    idxx += 1

# 5Q. Search for a number x In this tuple using loop:

tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter Tup's Any Num : "))

i = 0 # Initialization

while i < len(tup):

    if (tup[i] == x):

        print("Found At Index ...",i)

    i += 1
