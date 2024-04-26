while True:
    even_num_list = []
    odd_num_list = []

    try:
        data_input = int(input("Enter a number: "))

        # Open "numbers.txt" in append mode and write the input number
        with open("numbers.txt", "a") as number_file:
            number_file.write(str(data_input) + "\n")  # Convert integer to string before writing

        for num in range(data_input, data_input + 20):
            print("Number List:", num, end=" ")

            if num % 2 == 0:
                even_num_list.append(num)
            else:
                odd_num_list.append(num)

        # Create a file named "even.txt" for all the even numbers
        with open("even.txt", "w") as even_file:
            for data in even_num_list:
                even_file.write(str(data) + "\n")

        # Create a file named "odd.txt" for all the odd numbers
        with open("odd.txt", "w") as odd_file:
            for data in odd_num_list:
                odd_file.write(str(data) + "\n")

        print("\n\nThe Even Numbers detected in the list are:", even_num_list)
        print("\nThe Odd Numbers detected in the list are:", odd_num_list)

    except ValueError:
        print("Error! Enter a valid number.")

    user_answer = input("\nDo you want to input another number? (y/n): ")
    if user_answer.lower() != "y":
        break

print("\nThank you for your participation.")
