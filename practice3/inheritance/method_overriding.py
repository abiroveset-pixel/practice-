class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

animal = Animal()
cat = Cat()

animal.speak()
cat.speak()