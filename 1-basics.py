# ==========================================
# 1: Python Basics
# ==========================================

"""
In this module, you will be introduced to the basics of coding through Python (a programming language), 
you will first learn about python syntax basics, then about storing data in variables, then about doing
arithmetic with data. In general, each module will consist of 2-4 topics, each with an explanation, a
few worked examples, and five practice problems, along with ten exercises and a projects at the end of the module. 
"""

# --------------------------------------------------
# Printing and Input
# --------------------------------------------------

"""
Using a programming language, such as Python, you can give a computer instructions. For the computer to
understand them, the instructions must be formatted in a particular way. In python, each instruction takes
up a line, and instructions are run in order. For instance "print("text")" prints out "text", or "data = 123"
stores 123 in data. We can also take input from the terminal using "data = input("prompt")", which will print 
"prompt" to the terminal and store the user response in data. 
"""

# Example 1
print("Hello, World!")  # prints "Hello, World!" to the terminal

# Example 2
a = 5 # stores 5 in a
b = 3 # stores 3 in b 
print(a + b)  # adds a and b and prints the result (8)

# Example 3
name = input("What's your name? ") # prompts user, and stores result in name
print("Nice to meet you,", name) # prints out "Nice to meet you, [data stored in name]"

# Practice Problems:
# 1. Print your favorite quote.
# 2. Print your age.
# 3. Store your name in a variable and print it.
# 4. Ask the user for their hometown and print it.
# 5. Ask the user for two numbers and print their sum.

# --------------------------------------------------
# Variables and Types
# --------------------------------------------------

"""
Variables can be thought of as pointers to or storing some data. When you assign data to a variable using 
"variable = data", any time you reference "variable", imagine that Python replaces "variable" with "data".
Variables can have several types: ints (integers), float (rationals), char (single characters), string 
(any text), and bool (True or False). For char and string, we put quotes around the data. In many other languages, 
we have to declare type when creating a variable, but in Python this is done automatically. To convert a variable's
type, simply write "converted = type(variable)", which stores the variable converted to type in converted. Note
that input() always provides strings, and print() will try to convert everything to a string. 
"""

# Worked Example 1
age = 20  # stores data 20 in variable age with type int
height = 5.9  # stores data 5.9 in variable height with type float
name = "Alice"  # stores data "Alice" in variable name with type string
girl = True # stores data True in variable girl with type bool

# Worked Example 2
print("Name: ", name) # prints out "Name: [data in name]"
print("Age in 5 years:", age + 5) #prints out "Age in 5 years: [data in age + 5]"

# Worked Example 3
pi = 3.14 # stores 3.14 in pi (float)
radius = 2 # stores 2 in radius (int)
area = pi * radius ** 2 # computes area of a circle (** is power)
area_s = str(area) # converts area to a string and stores it in area_s
print("Area: ", area) # prints "Area: [area_s]"

# Practice Problems:
# 1. Ask the user for their name, then age, and print both. 
# 2. Ask the user for their GPA, and 
# 3. Create an float storing height and convert it to a string. 
# 4. Multiply two integers and print the result.
# 5. Add a float and int, convert the sum to a string, and print the result.

# --------------------------------------------------
# Arithmetic
# --------------------------------------------------

"""
Python supports various arithmetical operations, which you can use in programming just as you would in
a calculator like desmos. The operations are + (addition), - (subtraction), * (multiplication), / (division),
% (modulo, or remainder), and ** (power). These operations take the form "result = num_1 [operation] num_2". An 
operation can also update a variable by adding = to it, for instance to increase "count" by 1, you would write
"count += 1". These operations generally work on ints and floats, but + also works on strings by concatinating them,
which means joining two strings together. For examples if we have "hi" and "bye", if we do "greet = "hi" + "bye"", 
then greet will store "hibye". You cannot add a non-string to a string, for this you need to first convert it to
a string then you can add it. 
"""

# Worked Example 1
a = 5 # a starts as 5
b = a * 3 # we put a * 3 = 15 into b
a = b / 5 # we put b / 5 = 3 into a (overwriting it)
a += 1 # we add 1 to a, giving us a = 4


# Worked Example 2
dividend = int(input("Dividend? ")) # Asks user to provide dividend (number to divide) and converts to int
divisor = int(input("Divisor? ")) # Asks user to provide divisor (number we divide by) and converts to int
quotient = dividend / divisor # divides dividend by divisor (result is float)
remainder = dividend % divisor # takes remainder of dividend and divisor (result is int)
quotient = int(quotient) # truncates quotient by converting it to an int
print("Quotient: " + str(quotient) + ", Remainder: " + str(remainder)) # prints out result using concatination
# note that when we use "+" with a string and a number we must convert the number to be a string

# Practice Problems:
# 1. Ask user for two numbers, then multiply them, print the result. 
# 2. Compute the average of three numbers. 
# 3. Ask user for temperature in C, convert and print temperature in F
# 4. Ask for radius and compute and print the circumference.
# 5. Compute remainder and quotient (as an int) of 512 / 33

# --------------------------------------------------
# Exercises
# --------------------------------------------------

# 1. Print "Coding is fun!"
# 2. Create variables for your name, age, and favorite color, and print them.
# 3. Ask the user for their height in cm, convert to meters, and print.
# 4. Compute and print the area of a rectangle from input width and height.
# 5. Ask the user for a number, square it, and print.
# 6. Ask for two integers and print their sum, difference, and product.
# 7. Take input for base and height of a triangle and compute area.
# 8. Convert minutes to hours and minutes.
# 9. Write a Celsius to Kelvin converter.
# 10. Create a simple tip calculator (bill + tip percentage).

# --------------------------------------------------
# Project: Quadratic Roots
# --------------------------------------------------

"""
Here you will build a program that computes the roots of a quadratic of the form ax**2 + bx + c using the 
quadratic calculator. The program will ask the user for a, b, and c, and then return the two roots x = r1, r2. 
For the purposes of this project, you can assume both roots are real. 

The execution of the program in the terminal MUST match the following: 

Please provide coefficients for ax**2 + bx + c
a? [input for a]
b? [input for b]
c? [input for c]
Roots: 
x = [root 1]
x = [root 2]
"""
