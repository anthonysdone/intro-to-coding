// ==========================================
// 8: C Basics
// ==========================================

/*
In this module, you will be introduced to the basics of coding through C (a programming language), 
you will first learn about binary and hexadecimal numbers, then about storing data in variables, then about 
input and output.
*/

#include <stdio.h>

// --------------------------------------------------
// Binary and Hexadecimal
// --------------------------------------------------

/*
In programming, numbers can be represented in different bases. The decimal system (base 10) uses digits 0-9.
Binary (base 2) uses only 0 and 1, and hexadecimal (base 16) uses 0-9 and A-F. In C, you can write binary
numbers with 0b prefix (like 0b1010), hex numbers with 0x prefix (like 0xFF), and decimal normally.
Binary is useful for understanding how computers store data, and hex is commonly used for memory addresses
and colors. To convert between them: each hex digit represents 4 binary digits, and you can use printf
with different format specifiers to display numbers in different bases.
*/

// Example 1: Representing the same number in different bases
void example1() {
    int decimal = 15;           // stores 15 in decimal
    int binary = 0b1111;        // stores binary 1111 (which is 15) 
    int hex = 0xF;              // stores hex F (which is 15)
    
    printf("Decimal: %d\n", decimal);      // prints 15
    printf("Binary: %d\n", binary);        // prints 15 (converted to decimal)
    printf("Hex: %d\n", hex);              // prints 15 (converted to decimal)
}

// Example 2: Displaying numbers in different formats
void example2() {
    int num = 42;
    printf("Decimal: %d\n", num);          // prints in decimal: 42
    printf("Hex: %x\n", num);              // prints in hex: 2a
    printf("Hex (uppercase): %X\n", num);  // prints in hex: 2A
}

// Example 3: Converting between bases
void example3() {
    printf("Binary 1010 = %d in decimal\n", 0b1010);  // prints: Binary 1010 = 10 in decimal
    printf("Hex A = %d in decimal\n", 0xA);           // prints: Hex A = 10 in decimal
    printf("Decimal 255 = %x in hex\n", 255);         // prints: Decimal 255 = ff in hex
}

// Practice Problems:
// 1. Create variables storing the same number (8) in decimal, binary, and hex, then print all three.
// 2. Convert decimal 100 to hex and print it.
// 3. Convert binary 11001 to decimal and print it.
// 4. Print the number 255 in decimal, binary, and hex formats.
// 5. Create a hex number 0x20 and print what it equals in decimal.

// --------------------------------------------------
// Variables and Types
// --------------------------------------------------

/*
Variables in C store data and must be declared with a specific type before use. The main types are:
int (whole numbers), float (decimal numbers), double (more precise decimals), char (single characters),
and arrays for strings. Unlike Python, you must declare the type: "int age = 20;" or "float height = 5.9;".
Character literals use single quotes like 'A', while strings use double quotes like "Hello".
You can initialize variables when declaring them, or declare first then assign later.
C is "statically typed" meaning once a variable has a type, it cannot change.
*/

// Worked Example 1: Declaring and initializing variables
void workedExample1() {
    int age = 20;           // stores integer 20 in variable age
    float height = 5.9;     // stores float 5.9 in variable height  
    char grade = 'A';       // stores character 'A' in variable grade
    double pi = 3.14159;    // stores double-precision decimal in pi
    
    printf("Age: %d\n", age);          // %d for integers
    printf("Height: %.1f\n", height);  // %.1f for floats (1 decimal place)
    printf("Grade: %c\n", grade);      // %c for characters
    printf("Pi: %.5f\n", pi);          // %.5f for doubles (5 decimal places)
}

// Worked Example 2: Declaring then assigning
void workedExample2() {
    int x;              // declare x as an integer
    x = 10;             // assign 10 to x
    printf("x = %d\n", x);
    
    x = x + 5;          // update x to be x + 5 = 15
    printf("x + 5 = %d\n", x);
}

// Worked Example 3: Using variables in calculations
void workedExample3() {
    int radius = 5;
    float area = 3.14159 * radius * radius;  // calculate area of circle
    printf("Circle with radius %d has area %.2f\n", radius, area);
}

// Practice Problems:
// 1. Declare an integer variable for your birth year and print it.
// 2. Create a float for temperature and a char for grade, then print both.
// 3. Declare a double for a very precise number (like e = 2.718281828) and print it.
// 4. Create two integers, add them, and store the result in a third integer.
// 5. Declare a char variable storing your middle initial and print it.

// --------------------------------------------------
// Input and Output
// --------------------------------------------------

/*
In C, we use printf() to output text and numbers to the terminal, and scanf() to read input from the user.
printf() uses format specifiers like %d (integer), %f (float), %c (character), %s (string) to display
different types of data. scanf() uses the same format specifiers to read input, but requires the address
of the variable using the & operator (like &age). Always include \n in printf() for new lines.
For strings, we use character arrays and don't need & in scanf because array names are addresses.
*/

// Worked Example 1: Basic output
void workedExampleIO1() {
    printf("Hello, World!\n");                    // prints text with newline
    printf("The answer is %d\n", 42);            // prints text with number
    printf("Pi is approximately %.2f\n", 3.14);   // prints text with float (2 decimal places)
}

// Worked Example 2: Getting input from user
void workedExampleIO2() {
    int age;
    printf("What's your age? ");     // prompt user
    scanf("%d", &age);               // read integer into age (note the &)
    printf("You are %d years old\n", age);
}

// Worked Example 3: Multiple inputs
void workedExampleIO3() {
    char name[50];                   // create character array for string
    int number;
    
    printf("Enter your name: ");
    scanf("%s", name);               // read string (no & needed for arrays)
    printf("Enter a number: ");
    scanf("%d", &number);
    
    printf("Hello %s, your number squared is %d\n", name, number * number);
}

// Practice Problems:
// 1. Print your favorite quote using printf.
// 2. Ask the user for their height and print it back.
// 3. Read two integers from the user and print their sum.
// 4. Ask for the user's name and age, then print both.
// 5. Read a float from the user and print it with 3 decimal places.

// --------------------------------------------------
// Control Flow
// --------------------------------------------------

/*
Control flow allows programs to make decisions using if, else if, and else statements. The condition
goes in parentheses and uses comparison operators: == (equal), != (not equal), < (less than), 
> (greater than), <= (less than or equal), >= (greater than or equal). You can combine conditions
using && (and), || (or), and ! (not). The code block goes in curly braces {}. If the condition
is true, the code in the braces executes; otherwise it's skipped.
*/

// Worked Example 1: Simple if-else
void workedExampleControl1() {
    int age = 18;
    if (age >= 18) {
        printf("You are an adult\n");
    } else {
        printf("You are a minor\n");
    }
}

// Worked Example 2: Multiple conditions
void workedExampleControl2() {
    int score;
    printf("Enter your test score: ");
    scanf("%d", &score);
    
    if (score >= 90) {
        printf("Grade: A\n");
    } else if (score >= 80) {
        printf("Grade: B\n");
    } else if (score >= 70) {
        printf("Grade: C\n");
    } else if (score >= 60) {
        printf("Grade: D\n");
    } else {
        printf("Grade: F\n");
    }
}

// Worked Example 3: Logical operators
void workedExampleControl3() {
    int x = 5, y = 10;
    if (x > 0 && y > 0) {                    // both conditions must be true
        printf("Both numbers are positive\n");
    }
    if (x == 5 || y == 5) {                  // at least one condition must be true
        printf("At least one number is 5\n");
    }
}

// Practice Problems:
// 1. Ask for a number and print whether it's positive, negative, or zero.
// 2. Read two numbers and print which one is larger.
// 3. Ask for age and print if they can vote (18 or older).
// 4. Check if a number is even or odd using the modulo operator %.
// 5. Ask for temperature and print if it's freezing (below 32F).

// --------------------------------------------------
// Loops
// --------------------------------------------------

/*
Loops allow code to repeat multiple times. The for loop is used when you know how many times to repeat:
"for (initialization; condition; update)". The while loop repeats as long as a condition is true:
"while (condition)". The do-while loop is similar but checks the condition after each iteration.
Common patterns include counting from 1 to n, or getting input until a specific value is entered.
Use break to exit a loop early, and continue to skip to the next iteration.
*/

// Worked Example 1: For loop
void workedExampleLoop1() {
    for (int i = 1; i <= 5; i++) {          // loop from 1 to 5
        printf("Count: %d\n", i);
    }
}

// Worked Example 2: While loop
void workedExampleLoop2() {
    int number = 1;  // initialize to non-zero
    while (number != 0) {                    // keep going until user enters 0
        printf("Enter a number (0 to quit): ");
        scanf("%d", &number);
        if (number != 0) {
            printf("You entered: %d\n", number);
        }
    }
    printf("Goodbye!\n");
}

// Worked Example 3: Accumulating in a loop
void workedExampleLoop3() {
    int sum = 0;
    for (int i = 1; i <= 10; i++) {         // sum numbers 1 through 10
        sum += i;                            // add i to sum
    }
    printf("Sum of 1 to 10 is: %d\n", sum);
}

// Practice Problems:
// 1. Print numbers 1 through 10 using a for loop.
// 2. Use a while loop to print "Hello" 5 times.
// 3. Calculate the factorial of 5 using a loop.
// 4. Ask user for numbers until they enter -1, then print how many they entered.
// 5. Print all even numbers from 2 to 20.

// --------------------------------------------------
// Exercises
// --------------------------------------------------

// 1. Print "C programming is powerful!"
// 2. Create variables for name (string), age (int), and GPA (float), and print them.
// 3. Ask user for a number in decimal and print it in hex.
// 4. Read two integers and print their sum, difference, and product.
// 5. Ask for temperature in Celsius and convert to Fahrenheit.
// 6. Check if a year is a leap year (divisible by 4, but not 100, unless also divisible by 400).
// 7. Print the multiplication table for a number entered by the user.
// 8. Count how many digits are in a number entered by the user.
// 9. Ask for a character and print whether it's uppercase, lowercase, or neither.
// 10. Calculate the average of numbers entered by the user until they enter 0.

// --------------------------------------------------
// Project: Simple Calculator
// --------------------------------------------------

/*
Here you will build a program that acts as a simple calculator. The program will ask the user for
two numbers and an operation (+, -, *, /), then perform the calculation and display the result.
The program should handle division by zero appropriately.

The execution of the program in the terminal MUST match the following:

Simple Calculator
Enter first number: [input for num1]
Enter second number: [input for num2]  
Enter operation (+, -, *, /): [input for operation]
Result: [num1] [operation] [num2] = [result]
*/

int main() {
    // You can call any of the example functions here to test them
    // For example: example1();
    
    printf("Welcome to C Basics!\n");
    printf("This file contains examples and exercises for learning C.\n");
    printf("Uncomment function calls in main() to run specific examples.\n");
    
    return 0;
}
