
f = open("demo.txt", "r") # Open a File

data = f.read(4)      # Read the entire file

print(data)

print(type(data)) # Type of demo.txt data

f.close()       # Close the file


fo = open("demo.txt","r+") 

line1 = fo.readline() # Read full Line

print(line1)

line2 = fo.readline() 

print(line2)

line3 = fo.readline()

print(line3)

f.close()

# 

