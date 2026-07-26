info = {
    "key": "value",
    "name": "Maharshi",
    "lerning": "python",
    "cgpa": 8.89,
    "marks": [98, 78, 85], # List in Dictionary
    "is_adult": True,
    "t_or_f": False,
    "subject": ("maths", "gujarati", "samanyagyan"),
    "topics": ["Dict", "Set", "Java"],
}

print(type(info))

print(info["topics"])

print(info["subject"]) # Access dict values through it Key

print(info["key"])

print(info["cgpa"])

# Changing keys 

info["name"] = "Komal" # OverWrite old name is Gayab & newName aa jayega

info["surname"] = "Dabgar" # Add new Key : Value Pair

print(info) 

# Null Dictionary

null_dict = {}

null_dict["naam"] = "Nidhi"

null_dict["surnaam"] = "Patel"

print(null_dict)