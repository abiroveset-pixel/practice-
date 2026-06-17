import json

# JSON string
json_string = '''
{
    "name": "Eset",
    "age": 19,
    "city": "Almaty"
}
'''

# Parse JSON
data = json.loads(json_string)

print(data["name"])
print(data["city"])

# Python to JSON
student = {
    "name": "Eset",
    "course": "Python",
    "passed": True
}

json_data = json.dumps(student, indent=4)

print(json_data)

# Write JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON file
with open("student.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)