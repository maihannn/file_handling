# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program #4
# Program #4.3
with open ("text_contents.txt", "w") as text_file:
    while True:
        user_input = input ("Enter a line: ")
        text_file.write (user_input + '\n')
    
    # check if the user wants to input another line or want to quit the program
        user_answer = input("Are there more lines? y/n? ")
        if user_answer.lower() == "y":
            continue
        else:
            break

print ("Thank you for your participation.")

