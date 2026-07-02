import json


json_string = '''
{
    "name": "Eset",
    "age": 19,
    "city": "Almaty"
}
'''


data = json.loads(json_string)

print(data["name"])
print(data["city"])


student = {
    "name": "Eset",
    "course": "Python",
    "passed": True
}

json_data = json.dumps(student, indent=4)

print(json_data)


with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


with open("student.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
