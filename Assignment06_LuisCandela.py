# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Luis,11/20/2024,Modified Script
# ------------------------------------------------------------------------------------------ #
import json  # Importing the json module for working with JSON data

# Define the Data Constants (strings and filenames used throughout the program)
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# File name where the student enrollment data will be stored
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # A list that will hold all student data (dictionaries for each student)
menu_choice: str  # Variable to store the menu choice made by the user

# Class for processing file operations (reading from and writing to files)
class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str) -> list:
        # Tries to read student data from the specified file and load it into the student_data list
        try:
            with open(file_name, "r") as file:  # Open the file in read mode
                student_data = json.load(file)  # Load the data from the file (assumed to be JSON formatted)
            return student_data  # Return the loaded data
        except Exception as e:  # If there's an error, catch it and display a message
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)  # Print any error documentation
            print(e.__str__())  # Print the string representation of the error
            return []  # Return an empty list if reading fails

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Tries to write the student data to the specified file
        try:
            with open(file_name, "w") as file:  # Open the file in write mode
                json.dump(student_data, file)  # Write the student data as JSON to the file
            print("The following data was saved to file!")  # Notify the user that the data has been saved
            # Print the student data that was saved to the file
            for student in student_data:
                print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:  # If there's an error, catch it and display a message
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)  # Print any error documentation
            print(e.__str__())  # Print the string representation of the error

# Class for handling input/output operations like displaying the menu and getting user input
class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        # Placeholder method to output error messages if needed
        pass

    @staticmethod
    def output_menu(menu: str):
        # Display the menu to the user
        print(MENU)

    @staticmethod
    def input_menu_choice():
        # Prompt the user to input a choice from the menu and return it
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        # Display the list of students and their course enrollments
        print("-" * 50)  # Print a line for visual separation
        for student in student_data:  # Loop through all students in the list
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)  # Print another line for visual separation

    @staticmethod
    def input_student_data():
        # Prompt the user to enter a student's details and return the student dictionary
        try:
            student_first_name = input("Enter the student's first name: ")  # Get first name from user
            if not student_first_name.isalpha():  # Check if the first name contains only letters
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")  # Get last name from user
            if not student_last_name.isalpha():  # Check if the last name contains only letters
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")  # Get course name from user
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            return student_data  # Return the student dictionary
        except ValueError as e:  # If a ValueError occurs, print the error message
            print(e)
            print("-- Technical Error Message -- ")
            print(e.__doc__)  # Print any error documentation
            print(e.__str__())  # Print the string representation of the error
        except Exception as e:  # For any other error, print a generic error message
            IO.output_error_messages("Error: There was a problem with your entered data.", e)

# Read data from file at the start of the program (loads student data if available)
students = FileProcessor.read_data_from_file(FILE_NAME)

# Main loop: presents the menu and processes user input until the user decides to exit
while True:
    IO.output_menu(MENU)  # Display the menu
    menu_choice = IO.input_menu_choice()  # Get the user's choice from the menu

    if menu_choice == "1":  # If the user selects option 1 (Register a Student)
        student_data = IO.input_student_data()  # Get the new student data
        if student_data:  # If the student data was successfully entered
            students.append(student_data)  # Add the new student to the students list
            print(f"You have registered {student_data['FirstName']} {student_data['LastName']} for {student_data['CourseName']}.")
        continue  # Return to the start of the loop for another choice

    elif menu_choice == "2":  # If the user selects option 2 (Show current data)
        IO.output_student_courses(students)  # Display the current list of students and their courses
        continue  # Return to the start of the loop for another choice

    elif menu_choice == "3":  # If the user selects option 3 (Save data to a file)
        FileProcessor.write_data_to_file(FILE_NAME, students)  # Write the data to the file
        continue  # Return to the start of the loop for another choice

    elif menu_choice == "4":  # If the user selects option 4 (Exit the program)
        break  # Exit the loop and end the program

    else:  # If the user selects an invalid option
        print("Please only choose option 1, 2, or 3")  # Prompt the user to select a valid option

print("Program Ended")  # Print a message when the program ends
