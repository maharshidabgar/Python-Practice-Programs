# 'r' usage in FileIO for read a full file

f = open("samp.txt", "r")

data = f.read()

print(data)

f.close()

# 'w' using for write = overwrite and also create new file in folder

f = open("samp.txt", "w")

f.write("Add in Samp text file...")

f.close()

# 'a' Append / Add some new String, Char in File

f = open("samp.txt", "a")

f.write("\nTano aje gyo Surat..")

f.close()

# 'r+' use with FileIO first read after write

f = open("samp.txt", "r+")

data = f.read(4)

f.write("cgdg")

# 'w+' use with FileIO first Write after Read 1st write after Read 

f = open("samp.txt", "w+")

f.write("\nDibo ekli ghare che..")

data = f.read(4)

print(data)

# 'x' Create a 
 
f = open("newfile.txt", "x")

f.write("Hello, Maharshi!")

f.close()

print("File created successfully.")