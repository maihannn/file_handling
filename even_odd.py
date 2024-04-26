# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# File Handling
# 4.1: Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt

# Variables:

numbers_list = []
even_num_list = []
odd_num_list = []

# Create a file named "numbers.txt" that contains all the numbers.

with open ("numbers.txt", "r") as number_file:
    for value in number_file:
        value = int(value.strip())
        numbers_list.append(value)
        
# Ask for users input:

data_input = int (input("Enter a number: "))

for num in range (data_input, data_input + 20):
    print ("Number List: ", num, end = " ")

# Checking if the number is an odd or an even number:
    if int (num) % 2 == 0:
        even_num_list.append(num)
    else:
        odd_num_list.append (num)

# Create a file named "even.txt" for all the even numbers.
with open ("even.txt", "w") as even_file:
    for data in even_num_list:
        even_file.write(str(data) + "\n")

# Create a file named "odd.txt" for all the odd numbers.
with open ("odd.txt", "w") as odd_file:
    for data in odd_num_list:
        odd_file.write(str(data) + "\n")

print ("\n\nThe Even Numbers detected in the list are: ", even_num_list)
print ("\nThe Odd Numbers detected in the list are: ", odd_num_list)

