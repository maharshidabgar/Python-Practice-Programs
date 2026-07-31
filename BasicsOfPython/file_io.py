# # Open a File

# f = open("demo.txt", "r") 

# # Read the entire file

# data = f.read(4)      

# print(data)

# # Type of demo.txt data

# print(type(data)) 

# # Close the file

# f.close()       

# fo = open("demo.txt","r+") 

# # Read full Line

# line1 = fo.readline() 

# print(line1)

# line2 = fo.readline() 

# print(line2)

# line3 = fo.readline()

# print(line3)

# f.close()

# # Wriring(overWrite in file)

# f = open("demo.txt","w")

# f.write("Jay Mataji Bapu Kem che...")

# f.close()

# Adding a Line

f = open("demo.txt","a")

f.write("This is a NewLine...") # Adds to the File

f.close()

