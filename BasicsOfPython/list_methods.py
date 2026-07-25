list = [2,1,3,4,6]

# List - Append

list.append(5)

print(list)

# List - Sort

list.sort() # Directly Not print(list.sort()) = it throws None

print(list) 

# String Sorting 

fruit = ["banana", "apple", "lichi", "chickoo"]

fruit.sort() # Alphabettical Sorting in String 

print(fruit)

# List - Reverse - Sort

list.sort(reverse = True)

print(list)

fruit.sort(reverse = True) # Alphabetical Reverse Sorting for String

print(fruit)

# List - Reverse

list2 = [4,5,6] # [6,5,4]

list2.reverse()

print(list2)

# List - Inserting

list2.insert(0,9)

print(list2) 

# List - Remove

list.remove(6) # First 6 Occurence = Dekhayelo Remove Thay

print(list)

# List - Pop - Removes element at Index

last = [11, 22, 45, 55]

last.pop(2) # 2 idx = 45 Element Remove

print(last)