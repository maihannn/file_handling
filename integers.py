# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# File Handling
# 4.4: Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
# The first output file will be named double.txt containing the square of all even integers found in integers.txt 
# and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.


# Adding a while loop function to allow the users to use the program again.

while True:

    # Variables:
    integers_list = []
    even_num_list = []
    odd_num_list = []
    squared_list = []
    cubed_list = []

    # Ask for users input:

    try:
    
        data_input = int (input("Enter a number: "))
        
        # Create a file named "integers.txt" that contains 20 integers.

        with open("integers.txt", "w") as number_file:
            for num in range(data_input, data_input + 20):
                number_file.write(str(num) + "\n")
                print(num, end=" ")

                # Checking if the number is an odd or an even number:
                if int (num) % 2 == 0:
                    even_num_list.append(num)
                    # Getting the square of the even numbers:
                    squared_num = num ** 2
                    squared_list.append (squared_num)
                else:
                    odd_num_list.append (num)
                    # Getting the cube of the odd numbers:
                    cubed_num = num ** 3
                    cubed_list.append (cubed_num)

    # Create a file named "double.txt" for the sqaure of all even numbers.
        with open ("double.txt", "w") as squared_file:
            for data in even_num_list:
                squared_file.write(str(data) + "\n")

    # Create a file named "triple.txt" for rhe cube of all the odd numbers.
        with open ("triple.txt", "w") as cubed_file:
            for data in odd_num_list:
                cubed_file.write(str(data) + "\n")

        print ("\n\nThe Even Numbers detected in the list are: ", even_num_list)
        print ("\nThe Squared Numbers detected in the list are: ", squared_list)
        print ("\nThe Odd Numbers detected in the list are: ", odd_num_list)
        print ("\nThe Cubed Numbers detected in the list are: ", cubed_list)

    # Catch Errors (strings that are not a number)
    except ValueError:
        print ("Error! Enter a valid number.")

    user_answer = input ("\nDo you want to input another number? y/n ")
    if user_answer.lower() == "y":
        continue
    else:
        break

print ("\nThank you for your participation.")