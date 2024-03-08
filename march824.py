"""Here are examples demonstrating file 
handling in Python, including opening a file,
reading from it, writing to it, and closing it:
"""
1. #Opening a File:

# Open a file for reading
f = open("demofile.txt", "r")
print(f)

# Equivalent to: f = open("demofile.txt", "rt")
# (Because "r" for read and "t" for text are the default values)

# Make sure the file exists, or you'll get an error


2. #Reading from a File:

# Reading the entire content of the file
content = f.read()
print(content)

# Reading a single line from the file
line = f.readline()
print(line)

# Reading all lines into a list
lines = f.readlines()
print(lines)


3. #Writing to a File:

# Open a file for writing (creates if it doesn't exist)
f = open("newfile.txt", "w")

# Writing content to the file
f.write("Hello, World!\n")
f.write("This is a new line.")


4. #Closing the File:

# Close the file to free up system resources
f.close()


"""Remember, it's important to handle file closing properly 
to avoid memory leaks and ensure that your data is safely written to
the file. Always use proper error handling, especially when working 
with files, to manage exceptions that might occur during file operations."""