# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.

num1 = int(input("Enter your num1"))
num2 = int(input("Enter your num2"))

#2.  Performs the basic mathematical operations on these two numbers:

# 1 : Addition
add = num1 + num2

# 2 : Substraction
subs = num2 - num1

# 3 : Multiplication
mult = num1 * num2

# 4 : Division

div = num2/num1

# 3.  Displays the results of each operation on the screen.

print("Addition :", add)
print("Substraction :", subs)
print("Multiplication :", mult)
print("Division :", div)


# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.

first_name = input("enter your first name")
second_name = input("enter your second name")

# 2.  Concatenates the first name and last name into a full name.

full_name = first_name + second_name

# 3.  Prints a personalized greeting message using the full name.

print(f'hello ,{full_name} ! Welcome to the Python program')