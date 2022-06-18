import math


class Animal:
    def __init__(self):
        print("UBUNGA!")

    def eat(self):
        print("I am eating!")


class Dog:

    species = "mammal"

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots

    def bark(self, number=1):
        print(f"Woof! My name is {self.name}")
        for _ in range(number):
            print("Woof!")

    def speak(self):
        return "woof!"


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def speak(self):
        return "meow!"


def pet_speak(pet):
    print("From pet_speak function: " + pet.speak() * 3)


dog = Dog(name="Black", breed="Lab", spots=True)
cat = Cat()

print(dog.species)
dog.bark(2)  # method
cat

for pet in [dog, cat]:
    print(type(pet))
    print(pet.speak())

pet_speak(dog)

############################################################################################################################################################


class Circle:
    pi = math.pi

    def __init__(self, radius=1):
        self.radius = radius
        self.area = self.pi * radius ** 2

    def get_circumference(self):
        return self.radius * Circle.pi * 2  # Or self.pi


circle = Circle(30)  # Provide radius of 2
print(f"Circle circumference: {circle.get_circumference():.5f}")
print(f"Circle area: {circle.area:.5f}")

############################################################################################################################################################


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'The book "{self.title}" has been burned!')


book1 = Book("Lamb", "Butcher", 1_203)
print(book1)
print(len(book1))
del book1


############################################################################################################################################################


class Line:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        return math.dist(self.coordinate1, self.coordinate2)

    def slope(self):
        return (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])


class Cylinder:
    pi = math.pi

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * (self.radius + self.height)


coordinate1 = [3, 2]
coordinate2 = [8, 10]
line = Line(coordinate1, coordinate2)

print(line.distance())
print(line.slope())

cylinder = Cylinder(2, 3)
print(f"{cylinder.volume():.5f}")
print(f"{cylinder.surface_area():.5f}")


############################################################################################################################################################


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance:,.2f}"

    def deposit(self, amount):
        self.balance += amount
        return (
            f"${amount:,.2f} has been deposited. Account Balance: ${self.balance:,.2f}."
        )

    def withdraw(self, amount):
        if self.balance < amount:
            return f"Insufficient account balance. Account Balance has ${self.balance:,.2f} only."
        else:
            self.balance -= amount
            return f"${amount:,.2f} has been withdrawn. Account Balance: ${self.balance:,.2f}."


account = Account("Jose", 100)
print(account)
print(account.owner, account.balance)
print(account.deposit(1000))
print(account.withdraw(50))
print(account.withdraw(1200))
