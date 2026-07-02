numbers = [10, 20, 30]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))



fruits = ["apple", "banana", "orange"]

fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)



class CountUp:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 5:
            current = self.number
            self.number += 1
            return current
        raise StopIteration

counter = CountUp()

for value in counter:
    print(value)



def countdown(start):
    while start > 0:
        yield start
        start -= 1

for number in countdown(5):
    print(number)



squares = (x * x for x in range(5))

for square in squares:
    print(square)
