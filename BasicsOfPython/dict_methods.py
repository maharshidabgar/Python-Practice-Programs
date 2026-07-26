# Dictionary Methods 

student = {
    "name": "Rahul Shah",

    # Nested Dictionary

    "Subjects": {
        "Physics": 79,
        "Biology": 58,
        "Chemistry": 76,
        "English": 82,
        "Sanskrit": 56,
        "Computer": 92,
    }
}

# All Keys Print

print(student.keys())

# All Values Print

print(student.values())

# Key - Values All Pair Print

print(student.items())

# Returns the Key According to Value

print(student.get("name"))

# extra
 
print(len(student))

print(list(student.keys()))

# Insert new Items = key:value pair

student.update({"city": "Bhavnagar"})

print(student)