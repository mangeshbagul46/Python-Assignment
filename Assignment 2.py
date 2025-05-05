#Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.

user = int(input("Enter your number:"))

#2. 	Checks whether the number is even or odd using an if-else statement.
#3. 	Displays the result accordingly.

if user %2==0:
    print(f"{user} is an Even number")
else:
    print(f"{user} is an Odd number")



# Task 2: Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total = 0
for num in range(1,51):
    total = total+num

print(f'The sum of number from 1 to 50 is: {total}')
