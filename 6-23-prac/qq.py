import json, os, shutil

# Working with strings - dumps()

student_dict = {
    "name": "James",
    "age": 18,
    "city": "Paris"
}

json_str1 = json.dumps(student_dict) # Converts dict to json string
print(json_str1)

# loads() - Convert a JSON string to a python dictionary

text = '{"genre": "grunge", "instrument": "guitar"}'
data = json.loads(text)
print(data)


# Working with files: dump(), load()

# Writing to a json file - dump()

student_dict = {
    "name": "James",
    "age": 18,
    "city": "Paris",
    "grades": [90, 82, 75],
    "languages": ["English", "French"]
}

with open("6-23-prac/whatever.json", "w") as file:
    json.dump(student_dict, file, indent=4)
    print("JSON file written successfully!")


# Reading a json file - load()

with open("6-23-prac/whatever.json", "r") as file:
    output = json.load(file)
    print(output)