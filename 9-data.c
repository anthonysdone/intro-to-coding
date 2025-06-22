// ==========================================
// 9: C Data Structures
// ==========================================

/*
In this module, you will learn about data structures and memory management in C, you will first learn 
about arrays and how to store multiple values, then about strings and string manipulation, then about 
pointers and memory addresses. In general, each module will consist of 2-4 topics, each with an explanation, a
few worked examples, and five practice problems, along with ten exercises and a project at the end of the module. 
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// --------------------------------------------------
// Arrays
// --------------------------------------------------

/*
Arrays in C store multiple values of the same type in contiguous memory locations. You declare an array
by specifying the type, name, and size: "int numbers[5];" creates an array of 5 integers. Array indices
start at 0, so the first element is array[0] and the last is array[size-1]. You can initialize arrays
with curly braces: "int arr[] = {1, 2, 3, 4, 5};" or "int arr[5] = {1, 2, 3, 4, 5};". Arrays have
fixed size and cannot be resized after declaration. You can loop through arrays to process all elements.
*/

// Example 1: Declaring and initializing arrays
void arrayExample1() {
    int numbers[5] = {10, 20, 30, 40, 50};    // declare and initialize array
    char grades[] = {'A', 'B', 'C', 'D', 'F'}; // array size determined by initializer
    
    printf("First number: %d\n", numbers[0]);  // access first element (index 0)
    printf("Last number: %d\n", numbers[4]);   // access last element (index 4)
    printf("First grade: %c\n", grades[0]);
}

// Example 2: Modifying array elements
void arrayExample2() {
    int scores[3];          // declare array without initialization
    scores[0] = 85;         // assign values to array elements
    scores[1] = 92;
    scores[2] = 78;
    
    printf("Scores: %d, %d, %d\n", scores[0], scores[1], scores[2]);
    
    scores[1] = 95;         // modify an element
    printf("Updated scores: %d, %d, %d\n", scores[0], scores[1], scores[2]);
}

// Example 3: Looping through arrays
void arrayExample3() {
    int values[] = {2, 4, 6, 8, 10};
    int size = 5;           // keep track of array size
    
    printf("Array elements: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", values[i]);
    }
    printf("\n");
    
    // Calculate sum of array elements
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += values[i];
    }
    printf("Sum: %d\n", sum);
}

// Practice Problems:
// 1. Create an array of 5 integers and print each element.
// 2. Declare an array of your favorite numbers and calculate their average.
// 3. Create a character array storing your initials and print them.
// 4. Make an array of test scores and find the highest score.
// 5. Create an array and print it in reverse order.

// --------------------------------------------------
// Strings
// --------------------------------------------------

/*
Strings in C are arrays of characters ending with a null terminator '\0'. You can declare strings
as character arrays: "char name[20];" or initialize them: "char greeting[] = "Hello";". C provides
string functions in <string.h> like strlen() (length), strcpy() (copy), strcat() (concatenate),
and strcmp() (compare). Always ensure your string arrays are large enough to hold the string plus
the null terminator. Use %s format specifier in printf() and scanf() for strings.
*/

// Worked Example 1: String declaration and basic operations
void stringExample1() {
    char name[50] = "Alice";                // declare and initialize string
    char greeting[] = "Hello";              // size determined automatically
    char message[100];                      // declare empty string
    
    printf("Name: %s\n", name);
    printf("Greeting: %s\n", greeting);
    printf("Name length: %lu\n", strlen(name));    // strlen returns length
    
    strcpy(message, greeting);              // copy greeting to message
    strcat(message, " ");                   // concatenate space
    strcat(message, name);                  // concatenate name
    printf("Message: %s\n", message);      // prints "Hello Alice"
}

// Worked Example 2: Reading and comparing strings
void stringExample2() {
    char word1[50], word2[50];
    
    printf("Enter first word: ");
    scanf("%s", word1);                     // read string (no & needed)
    printf("Enter second word: ");
    scanf("%s", word2);
    
    if (strcmp(word1, word2) == 0) {        // strcmp returns 0 if strings are equal
        printf("The words are the same\n");
    } else if (strcmp(word1, word2) < 0) {  // negative if word1 comes before word2
        printf("'%s' comes before '%s'\n", word1, word2);
    } else {
        printf("'%s' comes after '%s'\n", word1, word2);
    }
}

// Worked Example 3: String manipulation
void stringExample3() {
    char sentence[100] = "Programming in C";
    char word[20] = " is fun";
    
    printf("Original: %s\n", sentence);
    printf("Length: %lu\n", strlen(sentence));
    
    strcat(sentence, word);                 // add " is fun" to sentence
    printf("Modified: %s\n", sentence);    // prints "Programming in C is fun"
    
    // Access individual characters
    printf("First character: %c\n", sentence[0]);
    printf("Last character: %c\n", sentence[strlen(sentence) - 1]);
}

// Practice Problems:
// 1. Create a string with your full name and print its length.
// 2. Read two strings from user and concatenate them.
// 3. Compare two strings and print which comes first alphabetically.
// 4. Create a sentence and print each character on a separate line.
// 5. Count how many spaces are in a given string.

// --------------------------------------------------
// Pointers
// --------------------------------------------------

/*
Pointers are variables that store memory addresses of other variables. You declare a pointer using *:
"int *ptr;" declares a pointer to an integer. Use & to get the address of a variable: "ptr = &num;"
makes ptr point to num. Use * to dereference (access the value): "*ptr" gives you the value at the
address. Pointers are useful for dynamic memory allocation, passing large data efficiently, and
creating linked data structures. Array names are actually pointers to the first element.
*/

// Worked Example 1: Basic pointer operations
void pointerExample1() {
    int number = 42;                        // regular integer variable
    int *ptr = &number;                     // pointer to number's address
    
    printf("Value of number: %d\n", number);
    printf("Address of number: %p\n", (void*)&number);
    printf("Value of ptr: %p\n", (void*)ptr);
    printf("Value pointed to by ptr: %d\n", *ptr);
    
    *ptr = 100;                             // change value through pointer
    printf("New value of number: %d\n", number);  // number is now 100
}

// Worked Example 2: Pointers and arrays
void pointerExample2() {
    int array[] = {10, 20, 30, 40, 50};
    int *ptr = array;                       // array name is a pointer to first element
    
    printf("Array elements using array notation:\n");
    for (int i = 0; i < 5; i++) {
        printf("array[%d] = %d\n", i, array[i]);
    }
    
    printf("\nArray elements using pointer notation:\n");
    for (int i = 0; i < 5; i++) {
        printf("*(ptr + %d) = %d\n", i, *(ptr + i));  // pointer arithmetic
    }
}

// Worked Example 3: Pointers as function parameters
void modifyValue(int *ptr) {                // function takes pointer parameter
    *ptr = *ptr * 2;                        // modify value through pointer
}

void pointerExample3() {
    int value = 15;
    printf("Original value: %d\n", value);
    
    modifyValue(&value);                    // pass address of value
    printf("Modified value: %d\n", value); // value is now 30
}

// Practice Problems:
// 1. Create an integer variable and a pointer to it, print both the value and address.
// 2. Use a pointer to change the value of a variable and print the result.
// 3. Create an array and use a pointer to print all its elements.
// 4. Write a function that uses pointers to swap two integer values.
// 5. Use pointer arithmetic to access every other element of an array.

// --------------------------------------------------
// Memory Management
// --------------------------------------------------

/*
C allows dynamic memory allocation using malloc() (allocate memory) and free() (deallocate memory).
malloc() returns a pointer to allocated memory, or NULL if allocation fails. Always check if malloc()
succeeded before using the memory. Use free() to release memory when done to prevent memory leaks.
malloc() allocates uninitialized memory, while calloc() allocates zero-initialized memory. realloc()
can resize previously allocated memory. Dynamic memory is allocated on the heap, not the stack.
*/

// Worked Example 1: Basic dynamic memory allocation
void memoryExample1() {
    int *ptr = malloc(sizeof(int));         // allocate memory for one integer
    
    if (ptr == NULL) {                      // always check if malloc succeeded
        printf("Memory allocation failed\n");
        return;
    }
    
    *ptr = 25;                              // use the allocated memory
    printf("Value stored: %d\n", *ptr);
    
    free(ptr);                              // free the memory
    ptr = NULL;                             // good practice: set pointer to NULL
}

// Worked Example 2: Dynamic arrays
void memoryExample2() {
    int size;
    printf("Enter array size: ");
    scanf("%d", &size);
    
    int *array = malloc(size * sizeof(int)); // allocate memory for array
    
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return;
    }
    
    // Fill array with values
    for (int i = 0; i < size; i++) {
        array[i] = (i + 1) * 10;            // assign values 10, 20, 30, ...
    }
    
    // Print array
    printf("Dynamic array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    free(array);                            // free the memory
}

// Worked Example 3: Dynamic string allocation
void memoryExample3() {
    char *str = malloc(50 * sizeof(char));  // allocate memory for string
    
    if (str == NULL) {
        printf("Memory allocation failed\n");
        return;
    }
    
    printf("Enter a message: ");
    scanf("%s", str);                       // read into dynamically allocated string
    
    printf("You entered: %s\n", str);
    printf("String length: %lu\n", strlen(str));
    
    free(str);                              // free the memory
}

// Practice Problems:
// 1. Dynamically allocate memory for 5 integers and fill them with user input.
// 2. Create a dynamic array of floats and calculate their average.
// 3. Allocate memory for a string, read user input, and print it in reverse.
// 4. Use malloc to create an array, then use realloc to resize it.
// 5. Write a function that dynamically allocates memory for an array and returns it.

// --------------------------------------------------
// Exercises
// --------------------------------------------------

// 1. Create an array of 10 integers, fill with random values, and find min and max.
// 2. Write a program that reads a sentence and counts vowels and consonants.
// 3. Create two arrays and write a function to merge them into a third array.
// 4. Implement a simple string reversal function using pointers.
// 5. Read a string and count how many times each letter appears.
// 6. Create a dynamic array that grows as the user enters more numbers.
// 7. Write a function that removes all spaces from a string using pointers.
// 8. Implement a simple spell checker that compares words to a dictionary array.
// 9. Create a program that sorts an array of strings alphabetically.
// 10. Build a dynamic phone book that stores names and numbers.

// --------------------------------------------------
// Project: Text Analyzer
// --------------------------------------------------

/*
Here you will build a program that analyzes a text file or user input. The program will read text,
then provide statistics including word count, character count, average word length, and most frequent
words. Use dynamic memory allocation to handle text of unknown length.

The execution of the program in the terminal MUST match the following:

Text Analyzer
Enter text (type 'END' to finish):
[user inputs multiple lines of text]
[user types 'END']

Analysis Results:
Total characters: [count]
Total words: [count]
Average word length: [average]
Longest word: [word]
Most frequent word: [word] (appears [count] times)
*/

int main() {
    // You can call any of the example functions here to test them
    // For example: arrayExample1();
    
    printf("Welcome to C Data Structures!\n");
    printf("This file contains examples and exercises for learning arrays, strings, pointers, and memory.\n");
    printf("Uncomment function calls in main() to run specific examples.\n");
    
    return 0;
}