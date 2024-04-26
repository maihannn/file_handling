# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program: File Handling (Compilations)

def program_1 (): # EVEN OR ODD
    while True:
    # Variables:
        even_num_list = []
        odd_num_list = []

        # Ask for users input:
        try:
            print ("\033[36m" + "\n\nWELCOME TO PROGRAM 1!")
            data_input = int(input("\033[32m" + "\nEnter a number: " + "\033[37m"))

            # Create a file named "numbers.txt" that contains all the numbers.
            with open("numbers.txt", "w") as number_file:
                for num in range(data_input, data_input + 20):
                    number_file.write(str(num) + "\n\n")
                    print(num, end=" ")

                    # Checking if the number is an odd or an even number:
                    if num % 2 == 0:
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
    
            print ("\033[35m" + "\n\nThe Even Numbers detected in the list are: " + "\033[37m", even_num_list)
            print ("\033[35m" + "\nThe Odd Numbers detected in the list are: " + "\033[37m", odd_num_list)

        # Catch Errors (strings that are not a number)
        except ValueError:
            print ("Error! Enter a valid number.")

        user_answer = input ("\033[33m" + "\nDo you want to input another number? y/n " + "\033[37m")
        if user_answer.lower() == "y":
            continue
        else:
            break

    print ("\033[36m" + "\nTHANK YOU FOR YOUR PARTICIPATION.")

def program_2 (): # GET STUDENTS GWA
    
    # Adding Variables
    name_list = []
    gwa_list = []

    # Read data from the file "students_gwa.txt"
    with open("students_gwa.txt", "r") as student_file:
        for line in student_file:
            try:
                name, gwa = line.strip().split(",")
                name_list.append(name)
                gwa_list.append(float(gwa))  # Convert GWA to float for comparison
            except: ValueError, IndexError


    # Find the student with the highest GWA
    highest_index = gwa_list.index(min(gwa_list))

    # Adding Greetings
    print ("\033[36m" + "\n\nWELCOME TO PROGRAM 2!")

    # Displaying the Results
    print(f"\033[32m \n\nThe student with the highest GWA is {name_list[highest_index]}")
    print(f"\033[35m Name: {name_list[highest_index]}")
    print(f"\033[35m GWA: {gwa_list[highest_index]}")
    
    # Thank you greetings
    print ("\033[36m" + "\nTHANK YOU FOR YOUR PARTICIPATION.")

def program_3 (): # Write a Line

    # Adding Greetings
    print ("\033[36m" + "\n\nWELCOME TO PROGRAM 3!")

    # Create a file named "mylife.txt"
    with open ("mylife.txt", "w") as text_file:
        
        # Adding a fucntion that will allows user to re-use the program.
        while True:

            # Ask user for input
            user_input = input ("\033[32m" + "\nEnter a line: " + "\033[37m")
            text_file.write (user_input + '\n')
        
        # check if the user wants to input another line or want to quit the program
            user_answer = input("\033[33m" + "Are there more lines? y/n? " + "\033[37m")
            if user_answer.lower() == "y":
                continue
            else:
                break

    # Thank you greetings
    print ("\033[36m" + "\nTHANK YOU FOR YOUR PARTICIPATION.")

def program_4 (): # Sqaure Even, Cube Odd

    # Adding Greetings
    print ("\033[36m" + "\n\nWELCOME TO PROGRAM 4!")

    while True:

        # Variables:
        even_num_list = []
        odd_num_list = []
        squared_list = []
        cubed_list = []

        # Ask for users input:

        try:
        
            data_input = int (input("\033[32m" + "Enter a number: " + "\033[37m"))
            
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

            print ("\033[35m" + "\n\nThe Even Numbers detected in the list are: " + "\033[37m", even_num_list)
            print ("\033[35m" + "\nThe Squared Numbers detected in the list are: " + "\033[37m", squared_list)
            print ("\033[35m" + "\nThe Odd Numbers detected in the list are: " + "\033[37m", odd_num_list)
            print ("\033[35m" + "\nThe Cubed Numbers detected in the list are: " + "\033[37m", cubed_list)

        # Catch Errors (strings that are not a number)
        except ValueError:
            print ("\033[33m" + "Error! Enter a valid number.")

        user_answer = input ("\033[33m" + "\nDo you want to input another number? y/n " + "\033[37m")
        if user_answer.lower() == "y":
            continue
        else:
            break

    # Thank you greetings
    print ("\033[36m" + "\nTHANK YOU FOR YOUR PARTICIPATION.")

def menu():
    while True:
        # Display Greetings
        print ("\n\n\033[33m" + "WELCOME TO THE PROGRAM!")
        print ("\033[33m" + "Kindly Choose What Program Would You Like to Try? ")
        
        # Display Options
        print ("\n")
        print ("\033[37m" + "1. Even or Odd Numbers.") # Program 1 - Even or Odd Numbers
        print ("\033[37m" + "2. Find the Student with the Highest GWA.") # Program 2 - Students GWA
        print ("\033[37m" + "3. Write a Line.") # Program 3 - Writing text contents
        print ("\033[37m" + "4. Squared Even, Cubed Odd.") # Program 4 - Getting the Square of an Even numbers and getting the Cube of an Odd Numbers.
        print ("\033[37m" + "5. Quit")
        print ("\n")
        user_pick = input ("\033[33m" + "Please Enter a Number: " + "\033[37m")

        if user_pick == "1":
            program_1()
        elif user_pick == "2":
            program_2()
        elif user_pick == "3":
            program_3()
        elif user_pick == "4":
            program_4()
        elif user_pick == "5":
            final = input ("\033[32m" + "Are you sure you want to exit the program? y/n " + "\033[37m")
            if final.lower() == "y":
                print ("\033[34m" + "EXITING PROGRAM. THANK YOU FOR YOUR PARTICIPATION.")
            else:
                continue
        else:
            print ("\033[37m" + "Invalid. Please Enter a Number.")
        
        user_answer = input ("\033[33m" + "\nDo you want to use the program again? y/n " + "\033[37m")
        if user_answer.lower() == "y":
            continue
        else:
            ("Thank you!")
            break

menu()