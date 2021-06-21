# Abdoulaye Ndiaye
# Python 310 HR Assgmt
# 05/21/2021

"""
With your newly acquired Python skills you have been asked by a friend who runs a small business to develop
an application to keep track of her employees.There will be about 40-50 employees.
"""
import csv


# from Employee

def read_data_from_file(file_name):
    """ Reads in employee data from a csv file and write it to a dictionary of dictionaries.
    :param file_name: (string) name of file to read data from
    :return: (dictionary) of employees
    """

    employee_list = []

    # try:
    with open(file_name, 'r') as file:
        for line in file:
            employees = {}
            first_name, last_name, id, email_address, start_date = line.split(",")
            employees["first name"] = first_name.strip()
            employees["last name"] = last_name.strip()
            employees["ID"] = id.strip()
            employees["Email Address"] = email_address.strip()
            employees["start date"] = start_date.strip()
            employee_list.append(employees)
    return employee_list


def add_new_emp(emp_list):
    start_date = str(input("Enter Hire Date (MM-DD-YYYY): "))
    first_name = str(input("Enter First Name: "))

    last_name = str(input("Enter Last Name: "))

    id = str(input("Employee ID: "))

    email_address = str(input("Enter Email Address: "))

    employee = {}
    employee["first name"] = first_name.strip()
    employee["last name"] = last_name.strip()
    employee["ID"] = id.strip()
    employee["Email Address"] = email_address.strip()
    employee["start date"] = start_date.strip()
    emp_list.append(employee)


def update_emp(filename, id, **kwargs):
    with open(filename, 'a', newline="") as file:
        read_data = [row for row in csv.DictReader(filename)]
    print(read_data)
    for row in read_data:
        if row["id"] == ID:
            print("Updating employee ID: " + ID)
            row[kwargs] = kwargs


def current_emp_list(employee_list):
    #print(employee_list)
    #print("Currently employed employees:")
    print("{:20} {:20} {:20} {:15} {:20}".format("First Name", "Last Name", "ID", "Email", "Start Date"))


def main():
    employee = read_data_from_file("employee2.csv")

    while True:
        response = input("Welcome to the HR System!\n"
                         "Please choose the following options:\n"
                         "1 - Add a New Employee\n"
                         "2 - Display Current Employees \n"
                         "3 - quit\n"
                         )
        if response == "1":
            add_new_emp(employee)
        elif response == "2":
            update_emp(employee)
            current_emp_list(employee)
        elif response == "3":1
            verify = input("Would you like to quit (yes/no)?")
            if verify == "no":
                continue
            if verify == "yes":
                print("Thank you for visiting!")
            break
        else:
            print("You have enter an invalid option ")


if __name__ == "__main__":
    main()
