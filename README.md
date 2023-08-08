# Programming-in-Python-Coursera-
This is an example of a Python script that handles creating a JSON object from employee details and writing it to a file.

This Python script handles employee data, creates a dictionary containing employee information, converts it to a JSON string, and writes it to a file. Here's a breakdown of what each section does:
1. Import Statements: Imports the necessary modules and functions.
2. 'create_dict()' Function: Creates a dictionary with employee information (name, age, title) as keys and values.
3. 'write_json_to_file()' Function: Writes a JSON object to a file.
4. 'main()' Function: The main program logic.
    - Calls the details() function from the employee module.
    - Calls the create_dict() function to create an employee dictionary.
    - Uses json.dumps() to convert the dictionary to a JSON string.
    - Calls write_json_to_file() to write the JSON string to a file named "employee.json".
5. 'if __name__ == "__main__":' block: Ensures that the main() function is executed when the script is run directly, not when it's imported as a module.

Overall, this script takes employee information, creates a JSON representation of it, and writes it to a file named "employee.json". The script also includes print statements for displaying the details of the employee dictionary and the JSON object.
