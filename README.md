# User Information Management System

## Description
A simple command-line interface (CLI) User Information Management System where users can add, view, delete, and list_all_user. Tasks are saved and loaded from a CSV file (`out.csv`).

## Features
- **Add User**: Allows you to add a new user to the user list.
- **Update User**: Update user with the help of unique_id.
- **View User Details**: Displays all users, showing their all data (name, address, designation).
- **List All Users**: Display all users in list view.
- **Delete a Task**: Removes a user details by its ID.
- **Save and Load User**: Saves Users to and loads user details from `out.csv` file.

## Requirements
- Python 3.x installed on your system.
- Pandas library installed on your system.

## Installation
1. Creating a new directory for the project, e.g., user_information_management_system
2. Inside the directory, creating a Python file named main.py
3. Open the project folder in your terminal, Pycharm or VS Code.


## Running the Application
To run the application, use the following command in your terminal:
```bash
pip install pandas
python main.py
```

## Usage
Once the application is running, you will see a menu with the following options:
User Information Management System 
1. Add User 
2. Update User 
3. View User Details 
4. List All Users 
5. Delete 
6. Exit

Follow the on-screen prompts to manage your tasks effectively.


## Usage Guide

### Menu Options
1. **Add User:**
   - Enter user details: name, address, and designation.
   - The program assigns a unique ID automatically.

2. **Update User:**
   - Provide the unique ID of the user to update.

3. **View User Details:**
   - Enter the unique ID of the user to view their details.

4. **List All Users:**
   - Display all users stored in the system in a tabular format.

5. **Delete User:**
   - Provide the unique ID of the user to delete their record.

6. **Search Users:**
   - Specify a field (name, address, or designation) and a value to search for matching records.

7. **Exit:**
   - Close the program.

## Example
### Adding a User
User Information Management System 
1. Add User 
2. Update User 
3. View User Details 
4. List All Users 
5. Delete 
6. Exit
enter a choice: 1
User's name: gopal
User's address: pune
User's job designation: developer

 -- Added Successfully with Unique_id 13 

### List of all User
User Information Management System 
1. Add User 
2. Update User 
3. View User Details 
4. List All Users 
5. Delete 
6. Exit
enter a choice: 4
    unique_id    uname      address designation
0           1    Rohit        Hubli   Developer
1           2   Rahul         Hubli          Qa
2           3   Keerti       Kerala     Finance
3           4   Heerti          Ghk     Finance
4           5     Raju       Koppal         Com
5           6  Devaraj    Tamilnadu          Qa
6           7      Abc  Devanahalli          Qa
7           8     Roky          Hdk         Dhj
8           9     King          Klo         Hjk
9          10      Fun          Gun         Mun
10         11     Ram            Up         Jem
11         12    Kamal       Mumbai          Hr
12         13    Gopal         Pune   Developer

## code

# Creating the csv file and columns in the csv file
if not os.path.exists("out.csv"):
    data = pandas.DataFrame(columns=["unique_id", "uname", "address", "designation"])
    data.to_csv("out.csv", index=False)

# pandas dataframe
employee = {
            'unique_id': [unique_id],
            "uname": [uname],
            "address": [address],
            "designation": [designation]
        }
        employee_dict = pandas.DataFrame(employee)
        employee_dict.to_csv('out.csv', mode='a', header=False, index=False)

# read dataframe
data = pandas.read_csv("out.csv")

# Retrieve the row from dataframe
for (index, row) in data.iterrows():
    if 'Rohit' in row.uname:
        print(row)

# For modification in dataframe
data.loc[id, "uname"] = "Rohit"

# Remove from the dataframe
data.drop(id, inplace=True)

# Set specific column to index from dataframe
data.set_index("unique_id", inplace=True)

# Reset the default index
data.reset_index(inplace=True)

## Notes
- The application saves user details in a file called `out.csv` in the same directory. Ensure you have write permissions in this folder.
- If no users are found, the application will inform you accordingly.
- **Auto-Generated IDs:** Unique IDs are assigned sequentially and automatically.

## Acknowledgments
This program was created using Python's **pandas** library for efficient data manipulation and management.
