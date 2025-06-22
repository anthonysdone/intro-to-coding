# ==========================================
# 2: Control Flow
# ==========================================

"""
In this module, you will learn about control flow in Python, which allows your programs to make decisions
and repeat actions. You will learn about conditional statements (if, elif, else), loops (for and while), 
and functions. 
"""

# --------------------------------------------------
# Conditional Statements
# --------------------------------------------------

"""
Conditional statements allow your program to make decisions based on certain conditions. The basic structure
is "if condition:", followed by indented code that runs if the condition is true. You can also use "elif condition:"
for additional conditions and "else:" for code that runs if no conditions are met. Conditions are usually
comparisons using ==, !=, <, >, <=, >= or boolean values True/False. Python also has "truthiness" - values like
0, empty strings "", and None are considered False, while most other values are True.
"""

# Worked Example 1
age = 18
if age >= 18:
    print("You are an adult")  # runs if age is 18 or older
else:
    print("You are a minor")   # runs if age is less than 18

# Worked Example 2
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Worked Example 3
password = input("Enter password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# Practice Problems:
# 1. Check if a number is positive, negative, or zero.
# 2. Ask for age and determine if someone can vote (18+).
# 3. Check if a number is even or odd using modulo (%).
# 4. Compare two numbers and print which is larger.
# 5. Check if a string is empty and print appropriate message.

# --------------------------------------------------
# Loops
# --------------------------------------------------

"""
Loops allow you to repeat code multiple times. There are two main types: "for" loops and "while" loops.
For loops are used when you know how many times to repeat or want to iterate through a sequence. The basic
syntax is "for variable in range(number):" or "for variable in sequence:". While loops continue as long
as a condition is true, using "while condition:". Be careful with while loops to avoid infinite loops by
ensuring the condition eventually becomes false.
"""

# Worked Example 1
for i in range(5):  # runs 5 times, i goes from 0 to 4
    print("Count:", i)

# Worked Example 2
countdown = 5
while countdown > 0:  # runs while countdown is greater than 0
    print(countdown)
    countdown -= 1    # decrease countdown by 1 each time
print("Blast off!")

# Worked Example 3
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:   # iterate through each number in the list
    total += num      # add each number to total
print("Sum:", total)

# Practice Problems:
# 1. Print numbers from 1 to 10 using a for loop.
# 2. Calculate the factorial of a number using a loop.
# 3. Ask user for numbers until they enter 0, then print the sum.
# 4. Print all even numbers from 2 to 20.
# 5. Count how many times letter 'a' appears in a word.

# --------------------------------------------------
# Functions
# --------------------------------------------------

"""
Functions are reusable blocks of code that perform specific tasks. They help organize code and avoid repetition.
Functions are defined using "def function_name(parameters):" followed by indented code. Functions can take
inputs (parameters/arguments) and return outputs using "return value". Variables created inside functions
have local scope - they only exist within that function. To use a function, you "call" it by writing
the function name followed by parentheses containing any required arguments.
"""

# Worked Example 1
def greet(name):              # function that takes one parameter
    print("Hello,", name)     # code that runs when function is called

greet("Alice")                # calling the function with "Alice" as argument

# Worked Example 2
def add_numbers(a, b):        # function that takes two parameters
    result = a + b            # calculate sum
    return result             # return the result

sum_result = add_numbers(5, 3)  # call function and store result
print("5 + 3 =", sum_result)   # prints "5 + 3 = 8"

# Worked Example 3
def is_even(number):          # function that checks if number is even
    if number % 2 == 0:       # if remainder when divided by 2 is 0
        return True           # return True (it's even)
    else:
        return False          # return False (it's odd)

print(is_even(4))             # prints True
print(is_even(7))             # prints False

# Practice Problems:
# 1. Write a function that squares a number and returns the result.
# 2. Create a function that takes two numbers and returns the larger one.
# 3. Write a function that converts Celsius to Fahrenheit.
# 4. Create a function that checks if a string is a palindrome.
# 5. Write a function that calculates the area of a circle given radius.

# --------------------------------------------------
# Exercises
# --------------------------------------------------

# 1. Write a program that asks for a number and prints if it's positive, negative, or zero.
# 2. Create a guessing game where user tries to guess a number between 1-10.
# 3. Print the multiplication table for a number entered by the user.
# 4. Write a function that returns the maximum of three numbers.
# 5. Create a program that counts vowels in a sentence.
# 6. Write a function that checks if a year is a leap year.
# 7. Create a simple menu system using if/elif statements.
# 8. Write a program that finds the sum of all numbers from 1 to N.
# 9. Create a function that reverses a string.
# 10. Write a program that asks for passwords until correct one is entered.

# --------------------------------------------------
# Project: Simple Calculator with Functions
# --------------------------------------------------

"""
Create a calculator program that can perform basic arithmetic operations (addition, subtraction, 
multiplication, division) using functions. The program should continuously ask the user for operations
until they choose to quit. Each arithmetic operation should be implemented as a separate function.

The execution of the program in the terminal MUST match the following:

Simple Calculator
1. Addition
2. Subtraction  
3. Multiplication
4. Division
5. Quit
Choose operation (1-5): [user input]
Enter first number: [user input]
Enter second number: [user input]
Result: [calculated result]

[repeat until user chooses 5 to quit]
"""
