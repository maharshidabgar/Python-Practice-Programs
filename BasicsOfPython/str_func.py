str = "i am from studying Python from ApnaCollege."

print(str.endswith("ege.")) # Returns True if string ends with substr.

print(str.capitalize()) # Capitalizes string 1st Char & its work only 1 time

# for capitAlize permenentaly 1st char uses

str = str.capitalize()

print(str)

# str.replace() - old value with New o -old , a - new 

print(str.replace("o","a"))

print(str.replace("studying", "bhanu chu"))

# str.find(word) - char / string index given

print(str.find("from"))

print(str.find("W")) # gives -1 bcz this char not exist in the string

# str.count()

print(str.count("from"))

