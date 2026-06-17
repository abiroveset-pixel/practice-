class Student:
    # Class variable
    school = "KBTU"

    def __init__(self, name):
        # Instance variable
        self.name = name

student1 = Student("Eset")
student2 = Student("Aruzhan")

print(student1.name)
print(student2.name)

print(student1.school)
print(student2.school)

# Modify instance variable
student1.name = "Dias"
print(student1.name)

# Delete instance variable
del student2.name
# print(student2.name)  # This would cause an error