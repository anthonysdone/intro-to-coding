# ==========================================
# 4: Object-Oriented Programming
# ==========================================

"""
In this module, you will learn about object-oriented programming (OOP) in Python, which allows you to
create reusable and organized code using classes and objects. You will first learn about classes, attributes,
and methods, then inheritance and polymorphism for code reuse, then encapsulation and composition for better
design, and finally design patterns and best practices. Each topic will have explanations, worked examples,
and practice problems, along with ten exercises and a project at the end of the module.
"""

# --------------------------------------------------
# Classes, Attributes, and Methods
# --------------------------------------------------

"""
Classes are blueprints for creating objects that contain both data (attributes) and functions (methods).
You define a class using "class ClassName:" followed by an __init__ method that sets up the object when
it's created. Attributes are variables that belong to the object, accessed using "self.attribute_name".
Methods are functions that belong to the class and can access the object's attributes using "self".
To create an object (instance) from a class, you call the class name like a function. Objects allow you
to organize related data and behavior together, making code more modular and reusable.
"""

# Worked Example 1
class Dog:
    def __init__(self, name, breed):    # constructor method, runs when object is created
        self.name = name                # set the dog's name attribute
        self.breed = breed              # set the dog's breed attribute
    
    def bark(self):                     # method that makes the dog bark
        print(self.name, "says woof!")  # access the dog's name using self

my_dog = Dog("Buddy", "Golden Retriever")  # create a Dog object
print("Dog's name:", my_dog.name)           # access attribute
print("Dog's breed:", my_dog.breed)         # access another attribute
my_dog.bark()                               # call method

# Worked Example 2
class Circle:
    def __init__(self, radius):         # constructor takes radius parameter
        self.radius = radius            # store radius as attribute
    
    def area(self):                     # method to calculate area
        return 3.14159 * self.radius ** 2  # use the radius attribute
    
    def circumference(self):            # method to calculate circumference
        return 2 * 3.14159 * self.radius   # another calculation using radius

circle1 = Circle(5)                     # create circle with radius 5
print("Area:", circle1.area())          # call area method
print("Circumference:", circle1.circumference())  # call circumference method

# Worked Example 3
class BankAccount:
    def __init__(self, owner, balance): # constructor with two parameters
        self.owner = owner              # set account owner
        self.balance = balance          # set initial balance
    
    def deposit(self, amount):          # method to add money
        self.balance += amount          # increase balance
        print("Deposited $" + str(amount) + ". New balance: $" + str(self.balance))
    
    def withdraw(self, amount):         # method to take money
        if amount <= self.balance:      # check if enough money
            self.balance -= amount      # decrease balance
            print("Withdrew $" + str(amount) + ". New balance: $" + str(self.balance))
        else:
            print("Insufficient funds") # not enough money

account = BankAccount("Alice", 1000)    # create account
account.deposit(500)                    # add money
account.withdraw(200)                   # take money

# Practice Problems:
# 1. Create a Car class with make, model, and year attributes.
# 2. Add a start_engine() method that prints "Engine started".
# 3. Create a Student class with name, grade, and GPA attributes.
# 4. Add a study() method that increases GPA by 0.1.
# 5. Create a Rectangle class with width and height, add area() method.

# --------------------------------------------------
# Inheritance and Polymorphism
# --------------------------------------------------

"""
Inheritance allows you to create new classes based on existing classes. The new class (child/subclass)
inherits all attributes and methods from the parent class (superclass) and can add new ones or override
existing ones. You create inheritance using "class Child(Parent):". Polymorphism means different classes
can have methods with the same name that behave differently. This allows you to treat different objects
the same way if they share common methods. Inheritance promotes code reuse and polymorphism makes code
more flexible by allowing different objects to respond to the same method calls in their own way.
"""

# Worked Example 1
class Animal:                           # parent class
    def __init__(self, name):
        self.name = name
    
    def speak(self):                    # method that child classes can override
        print(self.name, "makes a sound")

class Cat(Animal):                      # Cat inherits from Animal
    def speak(self):                    # override the speak method
        print(self.name, "says meow")

class Dog(Animal):                      # Dog also inherits from Animal
    def speak(self):                    # override with different behavior
        print(self.name, "says woof")

pet1 = Cat("Whiskers")                  # create Cat object
pet2 = Dog("Rex")                       # create Dog object
pet1.speak()                            # calls Cat's version of speak
pet2.speak()                            # calls Dog's version of speak

# Worked Example 2
class Vehicle:                          # base class for all vehicles
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def start(self):                    # common method for all vehicles
        print("Vehicle is starting...")

class Car(Vehicle):                     # Car inherits from Vehicle
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)   # call parent constructor
        self.doors = doors              # add new attribute specific to cars
    
    def honk(self):                     # new method specific to cars
        print("Car honks: Beep beep!")

my_car = Car("Toyota", 2020, 4)         # create Car object
print("Brand:", my_car.brand)           # inherited attribute
print("Doors:", my_car.doors)           # new attribute
my_car.start()                          # inherited method
my_car.honk()                           # new method

# Worked Example 3
# Polymorphism example - same method name, different behavior
animals = [Cat("Fluffy"), Dog("Buddy"), Animal("Generic")]  # list of different animals
for animal in animals:                  # loop through all animals
    animal.speak()                      # each animal speaks differently

# Practice Problems:
# 1. Create a Shape class and inherit Circle and Square from it.
# 2. Override a method in the child classes to calculate area differently.
# 3. Create a Person class and inherit Student and Teacher from it.
# 4. Add unique methods to each child class.
# 5. Demonstrate polymorphism with a list of different objects.

# --------------------------------------------------
# Encapsulation and Composition
# --------------------------------------------------

"""
Encapsulation means hiding internal details of a class and controlling access to data through methods.
In Python, attributes starting with underscore (_) are considered "protected" and those with double
underscore (__) are "private". You should use getter and setter methods to access private data safely.
Composition means building complex objects by combining simpler objects, rather than inheriting from them.
This follows the principle "has-a" relationship instead of "is-a". Composition is often preferred over
inheritance because it's more flexible and doesn't create tight coupling between classes.
"""

# Worked Example 1
class Student:
    def __init__(self, name, student_id):
        self.name = name                # public attribute
        self._grade = 0                 # protected attribute (use with caution)
        self.__student_id = student_id  # private attribute
    
    def get_student_id(self):           # getter method for private attribute
        return self.__student_id
    
    def set_grade(self, grade):         # setter method with validation
        if 0 <= grade <= 100:           # validate grade is reasonable
            self._grade = grade
        else:
            print("Invalid grade. Must be 0-100")
    
    def get_grade(self):                # getter method for grade
        return self._grade

student = Student("John", "S123")       # create student
student.set_grade(85)                   # set grade using method
print("Grade:", student.get_grade())    # get grade using method
print("ID:", student.get_student_id())  # get ID using method

# Worked Example 2
class Engine:                           # simple component class
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine with", self.horsepower, "HP is running")

class Wheels:                           # another component class
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        print("Wheels of size", self.size, "are spinning")

class Car:                              # Car is composed of Engine and Wheels
    def __init__(self, brand, engine, wheels):
        self.brand = brand
        self.engine = engine            # composition - Car "has-a" Engine
        self.wheels = wheels            # composition - Car "has-a" Wheels
    
    def drive(self):                    # Car uses its components
        print("Driving", self.brand)
        self.engine.start()             # delegate to engine
        self.wheels.rotate()            # delegate to wheels

my_engine = Engine(200)                 # create engine component
my_wheels = Wheels(18)                  # create wheels component
my_car = Car("Honda", my_engine, my_wheels)  # compose car from components
my_car.drive()                          # car coordinates its components

# Worked Example 3
class Address:                          # component class for address
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode
    
    def full_address(self):             # method to format address
        return self.street + ", " + self.city + " " + self.zipcode

class Person:                           # Person contains an Address
    def __init__(self, name, address):
        self.name = name
        self.address = address          # composition relationship
    
    def introduce(self):                # Person uses Address methods
        print("Hi, I'm", self.name)
        print("I live at", self.address.full_address())

home = Address("123 Main St", "Springfield", "12345")  # create address
person = Person("Alice", home)          # create person with address
person.introduce()                      # person introduces using address info

# Practice Problems:
# 1. Create a class with a private attribute and getter/setter methods.
# 2. Build a Computer class composed of CPU and Memory objects.
# 3. Create a School class that contains multiple Student objects.
# 4. Use encapsulation to validate data before setting attributes.
# 5. Design a House class composed of multiple Room objects.

# --------------------------------------------------
# Design Patterns and Best Practices
# --------------------------------------------------

"""
Design patterns are proven solutions to common programming problems. Some important patterns include
the Factory pattern (creates objects without specifying exact classes), Observer pattern (notifies
multiple objects of changes), and Singleton pattern (ensures only one instance exists). Best practices
for OOP include keeping classes focused on single responsibilities, preferring composition over inheritance,
using meaningful names, and writing methods that do one thing well. Following these patterns and practices
makes code more maintainable, testable, and understandable by other programmers.
"""

# Worked Example 1 - Factory Pattern
class AnimalFactory:                    # factory creates different animals
    @staticmethod                       # static method doesn't need instance
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name, "Mixed")
        elif animal_type == "cat":
            return Cat(name)
        else:
            return Animal(name)

# Using the factory
dog = AnimalFactory.create_animal("dog", "Buddy")
cat = AnimalFactory.create_animal("cat", "Whiskers")
dog.speak()                             # factory created appropriate type
cat.speak()

# Worked Example 2 - Single Responsibility Principle
class FileReader:                       # only responsible for reading files
    def read_file(self, filename):
        print("Reading file:", filename)
        return "file contents"

class DataProcessor:                    # only responsible for processing data
    def process(self, data):
        print("Processing:", data)
        return "processed " + data

class FileManager:                      # coordinates file operations
    def __init__(self):
        self.reader = FileReader()      # composition for flexibility
        self.processor = DataProcessor()
    
    def handle_file(self, filename):    # orchestrates the workflow
        data = self.reader.read_file(filename)
        result = self.processor.process(data)
        return result

manager = FileManager()                 # create coordinating object
result = manager.handle_file("data.txt")  # handle complete workflow

# Worked Example 3 - Proper Method Design
class Calculator:
    def __init__(self):
        self.history = []               # keep track of operations
    
    def add(self, a, b):                # method does one thing: addition
        result = a + b
        self._record_operation("add", a, b, result)
        return result
    
    def multiply(self, a, b):           # method does one thing: multiplication
        result = a * b
        self._record_operation("multiply", a, b, result)
        return result
    
    def _record_operation(self, op, a, b, result):  # private helper method
        operation = f"{a} {op} {b} = {result}"
        self.history.append(operation)
    
    def get_history(self):              # getter method for history
        return self.history

calc = Calculator()                     # create calculator
print(calc.add(5, 3))                  # use calculator
print(calc.multiply(4, 7))             # use calculator again
print("History:", calc.get_history())  # view operation history

# Practice Problems:
# 1. Create a factory that makes different types of vehicles.
# 2. Design a class that follows single responsibility principle.
# 3. Use composition to build a flexible drawing system.
# 4. Create a simple observer pattern with multiple listeners.
# 5. Design a class hierarchy that avoids deep inheritance.

# --------------------------------------------------
# Exercises
# --------------------------------------------------

# 1. Create an Animal class with name and species attributes.
# 2. Add a make_sound() method that prints a generic animal sound.
# 3. Create Dog and Cat subclasses that override make_sound().
# 4. Add a private attribute _age to Animal with getter/setter methods.
# 5. Create a Zoo class that contains multiple Animal objects.
# 6. Implement a Vehicle class with Engine and Transmission components.
# 7. Create a factory that produces different types of shapes.
# 8. Design a Student class with an Address component.
# 9. Use polymorphism to make different animals respond to same method.
# 10. Create a game character hierarchy with at least 3 levels of inheritance.

# --------------------------------------------------
# Project: Text-Based Card Game (Blackjack)
# --------------------------------------------------

"""
Create a text-based Blackjack card game using object-oriented programming principles. The system should
include classes for Card, Deck, Hand, Player, and Game. Use inheritance, composition, and encapsulation
appropriately. The game should allow dealing cards, calculating hand values, and determining winners.
Players should be able to hit (take another card) or stand (keep current hand).

The execution of the program in the terminal MUST match the following:

Welcome to Blackjack!
1. Start New Game
2. View Rules
3. Exit
Choose option (1-3): [user input]

For Start New Game:
Dealer's hand: [Hidden Card] [visible card]
Your hand: [card1] [card2] (Total: [value])

Your turn:
1. Hit (take another card)
2. Stand (keep current hand)
Choose action (1-2): [user input]

If Hit:
You drew: [card]
Your hand: [card1] [card2] [card3] (Total: [value])

Game Results:
Dealer's hand: [all cards] (Total: [value])
Your hand: [all cards] (Total: [value])
[You win! / Dealer wins! / It's a tie!]

Play again? (y/n): [user input]
"""
