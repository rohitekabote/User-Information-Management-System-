import pandas
import os


def add_user():
    data = pandas.read_csv("out.csv")
    if len(data.unique_id.to_list()) == 0:
        unique_id = 1
    else:
        unique_id = max(data.unique_id.to_list()) + 1
    uname = input("User's name: ").title()
    address = input("User's address: ").title()
    designation = input("User's job designation: ").title()
    if uname in data.uname.to_list():
        print("\n -- Name is already present -- ")
    else:
        employee = {
            'unique_id': [unique_id],
            "uname": [uname],
            "address": [address],
            "designation": [designation]
        }
        employee_dict = pandas.DataFrame(employee)
        employee_dict.to_csv('out.csv', mode='a', header=False, index=False)
        print(f"\n -- Added Successfully with Unique_id {unique_id} --")


def update_user():
    id = int(input("enter the unique_id to update: "))
    data = pandas.read_csv("out.csv")
    if id in data.unique_id.to_list():
        data.set_index("unique_id", inplace=True)
        data.loc[id, "uname"] = input("enter name: ").title()
        data.loc[id, "address"] = input("enter the address: ").title()
        data.loc[id, "designation"] = input("enter the designation: ").title()
        data.reset_index(inplace=True)
        data.to_csv('out.csv', index=False)
        print(f"\n -- Updated Successfully in Unique_id:{id}  --")
    else:
        print("\n -- Unique_id does't existed --")


def view_user_details():
    data = pandas.read_csv("out.csv")
    search_option = input("Enter option to search 'unique_id', 'name', 'address', 'designation', 'any': ").strip()
    if search_option == "unique_id":
        search = input("Enter input to search: ").title()
        for (index, row) in data.iterrows():
            if search == str(row.unique_id):
                print("\n", row)
    elif search_option == 'name':
        search = input("Enter input to search: ").title()
        for (index, row) in data.iterrows():
            if search.strip() in row.uname:
                print("\n", row)
    elif search_option == "address":
        search = input("enter input to search: ").title()
        for (index, row) in data.iterrows():
            if search.strip() in row.address:
                print("\n", row)
    elif search_option == "designation":
        search = input("enter input to search: ").title()
        for (index, row) in data.iterrows():
            if search.strip() in row.designation:
                print("\n", row)
    elif search_option == "any":
        search = input("enter input to search: ").title()
        for (index, row) in data.iterrows():
            if search == str(row.unique_id):
                print("\n", row)
            if search.strip() in row.uname:
                print("\n", row)
            if search.strip() in row.address:
                print("\n", row)
            if search.strip() in row.designation:
                print("\n", row)
    else:
        print("\n -- Enter proper input -- ")


def list_all_user():
    data = pandas.read_csv("out.csv")
    print(data)


def delete():
    id = int(input("enter unique_id to delete the data: "))
    data = pandas.read_csv("out.csv")
    if id in data.unique_id.to_list():
        data.set_index("unique_id", inplace=True)
        data.drop(id, inplace=True)
        data.reset_index(inplace=True)
        data.to_csv('out.csv', index=False)
        print("Deleted Successfully")
    else:
        print("ID didn't matched")

stop = False
while not stop:
    if not os.path.exists("out.csv"):
        data = pandas.DataFrame(columns=["unique_id", "uname", "address", "designation"])
        data.to_csv("out.csv", index=False)
    print("\nUser Information Management System \n1. Add User \n2. Update User \n3. View User Details \n4. List All Users \n5. Delete \n6. Exit")
    choice = int(input("enter a choice: "))
    match choice:
        case 1:
            add_user()
        case 2:
            update_user()
        case 3:
            view_user_details()
        case 4:
            list_all_user()
        case 5:
            delete()
        case 6:
            stop = True
        case _:
            print("enter correct input")

# switch case
'''def exit():
    global stop
    stop = True

def default():
    print("Invalid Input")


def run_case(case):

    options = {
        '1': add_user,
        '2': update_user,
        '3': view_user_details,
        '4': list_all_user,
        '5': delete,
        '6': exit
    }
    options.get(case, default)()

def main():
    if not os.path.exists("out.csv"):
        data = pandas.DataFrame(columns=["unique_id", "uname", "address", "designation"])
        data.to_csv("out.csv", index=False)
    global stop
    while not(stop):

        print("\nUser Information Management System \n1. Add User \n2. Update User \n3. View User Details \n4. List All Users \n5. Delete \n6. Exit")
        run_case(input("enter your Input: "))
main()'''