# ASSIGNMENT-4
ASSIGNMENT 4
Module 5: Files, Exceptions, and Errors in Python
Overview

This repository contains Python programs for Assignment 4, focusing on file handling and exception handling in Python.
The assignment demonstrates reading from files, writing and appending data to files, and handling errors gracefully.

Task 1: Read a File and Handle Errors
Description

This program reads the contents of a text file named sample.txt and prints each line.
If the file does not exist, the program handles the error using exception handling.

Features

Opens and reads a text file

Prints file content line by line

Handles FileNotFoundError gracefully

File Name
task1_read_file.py

Expected Output

If the file exists:

File contents:

Line 1
Line 2
Line 3


If the file does not exist:

Error: The file 'sample.txt' does not exist.

Task 2: Write and Append Data to a File
Description

This program takes user input and writes it to a file named output.txt.
It then appends additional data to the same file and displays the final file content.

Features

Writes user input to a file

Appends additional user input

Reads and displays final file content

File Name
task2_write_append.py

Expected Output (Example)

User Input:

Enter text to write to the file: Hello, Python!
Enter additional text to append: Learning file handling in Python.


Output:

Data successfully written to output.txt.

Data successfully appended.

Final content of output.txt:

Hello, Python!
Learning file handling in Python.

Requirements

Python 3.x

No external libraries required
