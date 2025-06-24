# ==========================================
# 3: Data Structures
# ==========================================

"""
In this module, you will learn about Python's built-in data structures for storing and organizing data.
You will first learn about lists for storing ordered collections, then dictionaries and tuples for key-value
pairs and immutable sequences, then iteration and list comprehension for processing data efficiently, and
finally searching, sorting, and time complexity. 
"""

# --------------------------------------------------
# Lists II
# --------------------------------------------------

"""
Building on basic list operations from Module 2, this section covers advanced list techniques including
slicing, list methods, nested lists, and list manipulation with loops and conditionals. List slicing uses
the syntax list[start:end:step] to extract portions of lists. Methods like insert(), pop(), index(), 
count(), and reverse() provide powerful ways to manipulate lists. Nested lists (lists within lists) 
allow you to create 2D structures like matrices or tables. You can combine lists with conditional 
statements and loops to filter, transform, and analyze data efficiently.
"""

# Worked Example 1 - Advanced List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])     # prints [2, 3, 4, 5] (elements 2 through 5)
print(numbers[:4])      # prints [0, 1, 2, 3] (first 4 elements)
print(numbers[6:])      # prints [6, 7, 8, 9] (from index 6 to end)
print(numbers[::2])     # prints [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])    # prints [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)

# Worked Example 2 - Advanced List Methods
fruits = ["apple", "banana", "cherry", "date"]
fruits.insert(1, "apricot")          # insert at specific position
print(fruits)                        # prints ['apple', 'apricot', 'banana', 'cherry', 'date']
last_fruit = fruits.pop()            # remove and return last item
print("Removed:", last_fruit)        # prints "Removed: date"
print("Apple appears", fruits.count("apple"), "times")  # count occurrences
fruits.reverse()                     # reverse the list in place
print("Reversed:", fruits)

# Worked Example 3 - Nested Lists and Data Processing
grades = [
    ["Alice", 85, 92, 78],
    ["Bob", 90, 88, 95],
    ["Charlie", 78, 85, 90]
]
# Calculate average grade for each student
for student in grades:
    name = student[0]
    scores = student[1:4]           # slice to get just the scores
    average = sum(scores) / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"{name}: {average:.1f} - Grade {grade}")

# Practice Problems:
# 1. Create a list of 10 numbers and print every 3rd element using slicing.
# 2. Use insert() to add an item at the beginning and middle of a list.
# 3. Create a nested list representing a 3x3 tic-tac-toe board.
# 4. Find and print the index of the maximum value in a list of numbers.
# 5. Create a list of words and use loops to find all words longer than 5 characters.

# --------------------------------------------------
# Dictionaries and Tuples
# --------------------------------------------------

"""
Dictionaries store data as key-value pairs using curly braces: {key1: value1, key2: value2}. You access
values using their keys instead of positions: dict[key]. Dictionaries are mutable and very useful for
storing related information. Tuples are ordered collections like lists but immutable (cannot be changed)
and use parentheses: (item1, item2, item3). Tuples are good for storing data that shouldn't change, like
coordinates or dates. Both dictionaries and tuples can store any data types and are fundamental for
organizing data in more complex ways than simple lists.
"""

# Worked Example 1
student = {"name": "Alice", "age": 20, "major": "Computer Science"}  # create dictionary
print(student["name"])      # prints "Alice"
print(student["age"])       # prints 20
student["gpa"] = 3.8        # add new key-value pair
print(student)              # prints entire dictionary with new gpa

# Worked Example 2
point = (3, 4)              # create tuple with coordinates
x = point[0]                # get x coordinate (3)
y = point[1]                # get y coordinate (4)
print("Point is at", x, y)  # prints "Point is at 3 4"
# point[0] = 5              # this would cause an error - tuples are immutable

# Worked Example 3
inventory = {"apples": 50, "bananas": 30, "oranges": 25}  # store fruit quantities
fruit = input("Which fruit? ")  # ask user for fruit name
if fruit in inventory:          # check if fruit exists in dictionary
    print("We have", inventory[fruit], fruit)  # print quantity
else:
    print("Sorry, we don't have", fruit)       # fruit not in inventory

# Practice Problems:
# 1. Create a dictionary with 3 countries and their capitals.
# 2. Make a tuple storing your birth year, month, and day.
# 3. Add a new item to an existing dictionary and print it.
# 4. Create a dictionary of friends' names and phone numbers.
# 5. Use a tuple to store RGB color values (red, green, blue).

# --------------------------------------------------
# Iteration and Comprehension
# --------------------------------------------------

"""
Iteration means going through each item in a data structure one by one. You can iterate through lists,
dictionaries, tuples, and strings using for loops. For dictionaries, you can loop through keys, values,
or both using .keys(), .values(), or .items(). List comprehension is a compact way to create new lists
by applying an operation to each item in an existing sequence. The syntax is [expression for item in sequence],
and you can add conditions with "if". Comprehensions make code more readable and often faster than regular
loops when creating new lists.
"""

# Worked Example 1
names = ["Alice", "Bob", "Charlie"]  # list of names
for name in names:                   # iterate through each name
    print("Hello,", name)            # greet each person
# prints: Hello, Alice, Hello, Bob, Hello, Charlie

# Worked Example 2
ages = {"Alice": 20, "Bob": 25, "Charlie": 30}  # dictionary of ages
for name, age in ages.items():                   # iterate through key-value pairs
    print(name, "is", age, "years old")          # print each person's age

# Worked Example 3
numbers = [1, 2, 3, 4, 5]                       # original list
squares = [x ** 2 for x in numbers]             # create new list using comprehension
print(squares)                                   # prints [1, 4, 9, 16, 25]
evens = [x for x in numbers if x % 2 == 0]      # comprehension with condition
print(evens)                                     # prints [2, 4]

# Practice Problems:
# 1. Loop through a string and print each character on a new line.
# 2. Create a list of cubes (x^3) for numbers 1-10 using comprehension.
# 3. Iterate through a dictionary and print only the keys.
# 4. Use comprehension to create a list of even numbers from 0-20.
# 5. Loop through a list and count how many items are greater than 10.

# --------------------------------------------------
# Searching, Sorting, and Time Complexity
# --------------------------------------------------

"""
Searching means finding specific items in data structures. Python provides the "in" operator for simple
searching, or you can write functions to find item positions. Sorting arranges items in order - Python
has built-in sort() method for lists and sorted() function for any sequence. Time complexity describes
how long operations take as data size grows. O(1) is constant time (instant), O(n) is linear time (grows
with size), and O(n²) is quadratic time (nested loops). Understanding these concepts helps you write
efficient programs. Generally, simpler operations are faster, and nested loops should be avoided when possible.
"""

# Worked Example 1
numbers = [64, 34, 25, 12, 22, 11, 90]  # unsorted list
print("Original:", numbers)
numbers.sort()                           # sort the list in place
print("Sorted:", numbers)                # prints [11, 12, 22, 25, 34, 64, 90]
print("22 found at index:", numbers.index(22))  # find position of 22

# Worked Example 2
def linear_search(lst, target):          # function to search for target
    for i in range(len(lst)):            # loop through each index
        if lst[i] == target:             # if item matches target
            return i                     # return the index
    return -1                            # return -1 if not found

fruits = ["apple", "banana", "cherry"]
result = linear_search(fruits, "banana")
print("banana found at index:", result)  # prints index of banana

# Worked Example 3
# Time complexity examples:
data = [1, 2, 3, 4, 5]
print(data[2])                           # O(1) - constant time, instant access

for item in data:                        # O(n) - linear time, grows with list size
    print(item)

for i in data:                           # O(n²) - quadratic time, nested loops
    for j in data:
        print(i, j)                      # prints all pairs

# Practice Problems:
# 1. Sort a list of strings alphabetically and print the result.
# 2. Write a function to find the maximum value in a list.
# 3. Search for a specific word in a list of words.
# 4. Identify the time complexity of a function with 3 nested loops.
# 5. Use sorted() to create a new sorted list without changing the original.

# --------------------------------------------------
# Exercises
# --------------------------------------------------

# 1. Create a shopping list with 5 items and print each item with its position.
# 2. Make a dictionary of 4 students and their grades, then print the average.
# 3. Create a tuple with your full name (first, middle, last) and print each part.
# 4. Use list comprehension to create a list of squares for even numbers 2-20.
# 5. Write a function that searches for a value in a list and returns True/False.
# 6. Sort a list of mixed numbers and strings (convert all to strings first).
# 7. Create a dictionary of movies and ratings, then find the highest rated.
# 8. Use a loop to count how many vowels are in a sentence.
# 9. Write a function that removes duplicates from a list using a set.
# 10. Create a gradebook dictionary and calculate letter grades for each student.

# --------------------------------------------------
# Project: Sort Visualizer with Histogram Display
# --------------------------------------------------

"""
Create a sorting algorithm visualizer that displays data as horizontal histograms using asterisks and shows each swap operation step-by-step.

To do this: 
1. Create a visualizer function that displays arrays as horizontal histograms
2. Implement several sorting algorithm functions that show each swap
3. Create a main function with user interaction for array size and algorithm choice

Required imports: import random, import time

The execution of the program in the terminal MUST match the following:

Sort Visualizer
===============
Enter array size: 6

Generated random array: [7, 3, 8, 2, 9, 1]

Starting Array:
7: *******
3: ***
8: ********
2: **
9: *********
1: *

Choose sorting algorithm:
1. Bubble Sort
2. Insertion Sort  
3. Merge Sort
4. Stalin Sort
Enter choice: 1

Starting Bubble Sort...

Step 1 - Comparing positions 0 and 1:
7: *******
3: ***
8: ********
2: **
9: *********
1: *

Swapping 7 and 3...

After swap:
3: ***
7: *******
8: ********
2: **
9: *********
1: *

[Continue showing each swap until sorted]

Final sorted array:
1: *
2: **
3: ***
7: *******
8: ********
9: *********

Bubble Sort completed!

Try again? (y/n): [user input]
"""
