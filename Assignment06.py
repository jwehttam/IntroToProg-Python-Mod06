# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   MatthewJohnson, 11/19/2023, Created Script
# ------------------------------------------------------------------------------------------ #

import json

#############
# Constants #
#############
MENU: str = '''
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = 'Enrollments.json'

#############
# Variables #
#############
menu_choice: str = ''
students: list = []


#########################
# Classes and Functions #
#########################
class FileProcessor:
    """
    Provides static methods for reading from and writing to files.

    These methods support the student registration system by handling the persistence of student data in JSON format.

    ChangeLog:
    - MatthewJohnson, 11.17.2023: Created Class.
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads JSON data from a specified file and appends it to the provided list.

        :param file_name: The name of the file to read from.
        :param student_data: The list to which the student data will be appended.
        :raises Exception: If the file cannot be read or the data cannot be parsed.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except Exception as error:
            IO.output_error_messages('Error reading from file', error)
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes JSON data to a specified file from the provided list.

        :param file_name: The name of the file to write to.
        :param student_data: The list containing student data to write.
        :raises Exception: If the file cannot be written to.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=4)
        except Exception as error:
            IO.output_error_messages('Error writing to file', error)
class IO:
    """
    Contains static methods for user input and output operations.

    This includes displaying menus, capturing user input, and formatting output for display.

    ChangeLog:
    - MatthewJohnson, 11.17.2023: Created Class.
    """
    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu to the user.

        :param menu: The menu string to be displayed.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        print(menu)
    @staticmethod
    def input_menu_choice() -> str:
        """
        Retrieves the user's menu choice.

        :return: The menu choice as a string.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        try:
            return input('What would you like to do: ')
        except KeyboardInterrupt:
            return 'INTERRUPTED'
    @staticmethod
    def output_student_courses(student_data: list):
        """
        Prints the courses for each student in the provided data list.

        :param student_data: A list of dictionaries, each representing a student's enrollment information.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        print('-' * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print('-' * 50)
    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the user for student information and adds it to the provided data list.

        :param student_data: The list to which the new student data will be added.
        :raises ValueError: If the input for the first or last name contains non-alphabetic characters.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        try:
            student_first_name = input('Enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('The first name should not contain numbers.')
            student_last_name = input('Enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('The last name should not contain numbers.')
            course_name = input('Please enter the name of the course: ')
            student_data.append({'FirstName': student_first_name,
                                 'LastName': student_last_name,
                                 'CourseName': course_name})
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        except ValueError as error:
            IO.output_error_messages('Invalid input', error)
        except Exception as error:
            IO.output_error_messages('An unexpected error occurred', error)
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Outputs the provided message and optional exception information.

        :param message: The error message to be displayed.
        :param error: Optional. The exception object containing additional error information.
        ChangeLog:
        - MatthewJohnson, 11.17.2023: Created Function.
        """
        print(message)
        if error:
            print('-- Technical Error Message --')
            print(error.__doc__)
            print(str(error))

############################
# Main Program Starts Here #
############################
FileProcessor.read_data_from_file(FILE_NAME, students)

###################
# -- Main Loop -- #
###################

while True:
    try:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == 'INTERRUPTED':
            print('\nProgram terminated by user. Goodbye!')
            break
        elif menu_choice == '1':
            IO.input_student_data(students)
        elif menu_choice == '2':
            print('The following students are registered:')
            IO.output_student_courses(students)
        elif menu_choice == '3':
            FileProcessor.write_data_to_file(FILE_NAME, students)
            print('The following data has been saved to Enrollments.json:')
            IO.output_student_courses(students)
        elif menu_choice == '4':
            print('Goodbye!')
            break
        else:
            print('Please only choose option 1, 2, 3 or 4')

    except Exception as e:
        IO.output_error_messages("An unexpected error occurred", e)
