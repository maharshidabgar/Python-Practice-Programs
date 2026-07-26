tup = (87, 45, 33, 26, 76, 45)

print(type(tup)) 

print(tup[0])
print(tup[1]) # Access of Tuple is Allowed

# but

# tup[0] = 92 # This not Allowed bcz Tuple Operator 

# is not Allowed Item Assignmet

tuple = (1,) # Its ok but tuple = (1) ... it gives int 

# tuple = (1.0) ... it gives Float Value

print(type(tuple))

# Slicing in Tuple

print(tup[1:3]) # all same as List 

# Methods

# Index Method

print(tup.index(33))

# Count Element Occurence

print(tup.count(45)) # Returns 2 BCZ 45 is 2 times in Tup ok