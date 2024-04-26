# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Write a Python program that read a file containing the name of 20 students together 
# with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

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
print(f"The student with the highest GWA is {name_list[highest_index]}")
print(f"Name: {name_list[highest_index]}")
print(f"GWA: {gwa_list[highest_index]}")