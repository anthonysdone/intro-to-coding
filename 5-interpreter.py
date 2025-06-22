# ==========================================
# 5: Building a Simple Lisp Interpreter Lab
# ==========================================

"""
In this lab, you will build a simple Lisp interpreter from scratch in Python. Lisp is a simple
programming language where everything is in parentheses. You'll learn how to break text into pieces,
understand structure, and calculate results. We'll start with just basic math like (+ 1 2), then add
variables, conditionals, and more features. This is a hands-on coding lab - you'll write most of the code!
"""

# --------------------------------------------------
# Step 1: Breaking Text into Pieces (Tokenizing)
# --------------------------------------------------

"""
First, we need to break text like "(+ 1 2)" into separate pieces: ['(', '+', '1', '2', ')'].
This is called "tokenizing" - we split the text wherever we see spaces, but we need to be
careful with parentheses. The key trick is to add spaces around parentheses first.
"""

def tokenize(text):
    """Break text into a list of tokens (pieces)."""
    # TODO: Replace '(' with ' ( ' in the text using .replace()
    # Hint: text = text.replace('(', ' ( ')
    
    # TODO: Replace ')' with ' ) ' in the text using .replace()
    # Hint: text = text.replace(')', ' ) ')
    
    # TODO: Split the text into a list using .split()
    # Hint: tokens = text.split()
    
    # TODO: Return the tokens list
    pass

# Test your tokenize function:
# tokenize("(+ 1 2)") should return ['(', '+', '1', '2', ')']

# --------------------------------------------------
# Step 2: Understanding Structure (Parsing)
# --------------------------------------------------

"""
Next, we convert tokens into a tree structure. In Lisp, parentheses show us the structure.
"(+ 1 2)" means "call the + function with arguments 1 and 2". We'll convert our list of tokens
into nested lists where each list represents a function call. Numbers become actual numbers.
"""

def parse(tokens):
    """Convert tokens into a structure we can work with."""
    # TODO: Check if tokens is empty, return None if so
    # Hint: if not tokens: return None
    
    # TODO: Remove and get the first token using tokens.pop(0)
    # Hint: token = tokens.pop(0)
    token = None  # Replace this line with your pop(0) call
    
    # TODO: Check if token is '('
    if token == '(':
        # TODO: Create an empty list called result
        # TODO: Use a while loop: while tokens and tokens[0] != ')':
        # TODO: Inside the loop, append parse(tokens) to result
        # TODO: After the loop, remove the ')' with tokens.pop(0)
        # TODO: Return result
        pass
    elif token == ')':
        # TODO: Raise a SyntaxError with message "Unexpected )"
        pass
    else:
        # TODO: Try to convert token to int with int(token), return it if successful
        # TODO: If that fails, try float(token), return it if successful  
        # TODO: If both fail, return token as a string
        # Hint: Use try/except blocks with ValueError
        pass

# Test your parse function:
# parse(tokenize("(+ 1 2)")) should return ['+', 1, 2]

# --------------------------------------------------
# Step 3: Setting Up Variables and Functions
# --------------------------------------------------

"""
We need a place to store variables like x = 5 and built-in functions like +, -, *, /.
We'll use a simple Python dictionary. This is much simpler than real programming languages!
"""

# TODO: Create a global dictionary called 'variables'
# TODO: Add basic math functions using lambda:
# Hint: '+': lambda a, b: a + b
# TODO: Add these operators: +, -, *, /, >, <, >=, <=, =
# TODO: For = use lambda a, b: a == b (since = is assignment in Python)
variables = {
    # TODO: Fill this in!
}

# Test your variables:
# variables['+'](3, 4) should return 7

# --------------------------------------------------
# Step 4: Running the Code (Evaluation)
# --------------------------------------------------

"""
This is where the magic happens! We take our parsed structure and actually calculate the result.
Numbers just return themselves. Symbols (like '+') look up their values. Lists mean "call a function"
- the first item is the function, the rest are arguments. So ['+', 1, 2] means "call + with 1 and 2".
"""

def evaluate(expression):
    """Calculate the result of an expression."""
    # TODO: Check if expression is a number (int or float) using isinstance
    # Hint: isinstance(expression, (int, float))
    # TODO: If it's a number, return it unchanged
    
    # TODO: Check if expression is a string using isinstance(expression, str)
    # TODO: If it's a string, look it up in variables dictionary
    # TODO: If not found, raise NameError with a helpful message
    # Hint: Use 'in' operator to check if key exists
    
    # TODO: Check if expression is a list using isinstance(expression, list)
    # TODO: If empty list, return empty list
    # TODO: Get the first element (that's the function name)
    
    # TODO: Handle special case 'set' for storing variables
    # If expression[0] == 'set':
    #   - Get symbol name from expression[1] 
    #   - Get value by calling evaluate(expression[2])
    #   - Store in variables dictionary
    #   - Return the value
    
    # TODO: Handle special case 'if' for conditionals  
    # If expression[0] == 'if':
    #   - Evaluate the condition (expression[1])
    #   - If true, evaluate and return expression[2]
    #   - If false, evaluate and return expression[3] (or None if missing)
    
    # TODO: Handle regular function calls
    # - Evaluate the function (first element)
    # - Evaluate all arguments (remaining elements) using list comprehension
    # - Call the function with *args
    # Hint: args = [evaluate(arg) for arg in expression[1:]]
    #       return func(*args)
    
    # TODO: If none of the above, raise TypeError
    pass

# Test your evaluate function:
# evaluate(5) should return 5
# evaluate(['+', 1, 2]) should return 3

# --------------------------------------------------
# Step 5: Putting It All Together
# --------------------------------------------------

"""
Now we can build a simple calculator that understands Lisp! We'll create a function that takes
text like "(+ 1 2)", breaks it into pieces, understands the structure, and calculates the result.
"""

def lisp_calc(text):
    """Calculate the result of a Lisp expression from text."""
    # TODO: Use try/except to handle errors gracefully
    # TODO: Inside try block:
    #   - Call tokenize(text) to get tokens
    #   - Check if tokens is empty, return None if so
    #   - Call parse(tokens) to get parsed expression
    #   - Call evaluate(parsed) to get result
    #   - Return the result
    # TODO: In except block, return f"Error: {e}" where e is the exception
    pass

def calculator():
    """Interactive Lisp calculator."""
    # TODO: Print welcome message and instructions
    # TODO: Print example commands like "(+ 1 2)", "(set x 5)", etc.
    
    # TODO: Create infinite loop with while True:
    # TODO: Use try/except to handle KeyboardInterrupt and EOFError
    # TODO: Get user input with input("lisp> ")
    # TODO: Check if user typed 'quit', break if so
    # TODO: Call lisp_calc(text) and print result if not None
    pass

# --------------------------------------------------
# Step 6: Adding More Features
# --------------------------------------------------

"""
Let's add more cool features to our Lisp interpreter! We'll add mathematical functions,
better conditionals, and list operations while keeping everything simple.
"""

def add_advanced_features():
    """Add more functions to our interpreter."""
    # TODO: Import the math module
    
    # TODO: Add these math functions to the variables dictionary:
    # 'abs': abs (absolute value)
    # 'max': max (maximum of numbers)
    # 'min': min (minimum of numbers)  
    # 'sqrt': math.sqrt (square root)
    # 'pow': lambda a, b: a ** b (power)
    # 'mod': lambda a, b: a % b (modulo/remainder)
    
    # TODO: Add string functions:
    # 'len': len (length of string/list)
    # 'upper': lambda s: s.upper() (uppercase string)
    # 'lower': lambda s: s.lower() (lowercase string)
    
    # TODO: Add list functions:
    # 'list': lambda *args: list(args) (create list)
    # 'first': lambda lst: lst[0] if lst else None (first element)
    # 'rest': lambda lst: lst[1:] if lst else [] (all but first)
    # 'append': lambda lst, item: lst + [item] (add to end)
    
    pass

# TODO: Call add_advanced_features() to enable the new functions

# --------------------------------------------------
# Enhanced Evaluation for New Features
# --------------------------------------------------

def evaluate_enhanced(expression):
    """Enhanced evaluate function with more special forms."""
    # TODO: Copy your basic evaluate function here
    
    # TODO: Add more special cases in the list handling:
    
    # TODO: Handle 'cond' for multiple conditions
    # (cond (condition1 result1) (condition2 result2) (else default))
    # Loop through pairs, evaluate conditions, return first true result
    
    # TODO: Handle 'let' for local variables
    # (let ((var1 value1) (var2 value2)) body)
    # Create temporary variables, evaluate body, restore old variables
    
    # TODO: Handle 'print' for output
    # (print expression) - evaluate expression and print it
    
    # TODO: Handle 'quote' to prevent evaluation
    # (quote (+ 1 2)) returns ['+', 1, 2] instead of 3
    
    pass

# --------------------------------------------------
# Test Your Interpreter!
# --------------------------------------------------

"""
Test these expressions when your interpreter is complete:

Basic math:
(+ 1 2)                    # Should return 3
(* 3 4)                    # Should return 12
(/ 10 2)                   # Should return 5.0

Variables:
(set x 10)                 # Should return 10 and store x
(+ x 5)                    # Should return 15

Conditionals:
(if (> 5 3) "yes" "no")    # Should return "yes"
(if (< 1 0) "true" "false") # Should return "false"

Advanced math:
(sqrt 16)                  # Should return 4.0
(pow 2 3)                  # Should return 8
(abs -5)                   # Should return 5

Lists:
(list 1 2 3)              # Should return [1, 2, 3]
(first (list 1 2 3))      # Should return 1
(len "hello")             # Should return 5

Try building nested expressions:
(+ 1 (* 2 (- 5 2)))       # Should return 7
(if (> (+ 1 2) 2) (pow 2 3) 0) # Should return 8
"""

print("Lisp Interpreter Lab")
print("Complete the TODOs to build your interpreter!")
print("Test with: lisp_calc('(+ 1 2)')")
print("Or run: calculator() for interactive mode")
