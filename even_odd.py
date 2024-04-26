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

# Ask for users input:

data_input = int (input("Enter a number: "))

for num in range (data_input, data_input + 20):
    print (num, end = " ")
# Checking if the number is an odd or an even number:
    if int (num) % 2 == 0:
        even_num_list.append(num)
    else:
        odd_num_list.append (num)

print ("\n\nThe Even Numbers detected in the list are: ", even_num_list)
print ("\nThe Odd Numbers detected in the list are: ", odd_num_list)

