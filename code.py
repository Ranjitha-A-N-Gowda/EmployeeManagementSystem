import os

data_file = "employees.txt"
index_file = "index.txt"

def read_data():
    employees = []
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            for line in file:
                employee_data = line.strip().split(",")
                employees.append({
                    "id": int(employee_data[0]),
                    "name": employee_data[1],
                    "salary": float(employee_data[2]),
                    "designation": employee_data[3],
                    "phone": employee_data[4]
                })
    return employees

def write_data(employees):
    with open(data_file, "w") as file:
        for employee in employees:
            line = "{},{},{},{},{}\n".format(
                employee["id"],
                employee["name"],
                employee["salary"],
                employee["designation"],
                employee["phone"]
            )
            file.write(line)

def update_index(index):
    with open(index_file, "w") as file:
        for entry in index:
            file.write(f"{entry['id']},{entry['offset']}\n")

def read_index():
    index = []
    if os.path.exists(index_file):
        with open(index_file, "r") as file:
            for line in file:
                emp_id, offset = line.strip().split(",")
                index.append({
                    "id": int(emp_id),
                    "offset": int(offset)
                })
    return index

def generate_primary_index(employees):
    index = []
    offset = 0
    for employee in employees:
        index.append({
            "id": employee["id"],
            "offset": offset
        })
        offset += len(str(employee)) + 1  # Include newline character
    return index

def add_employee(employees, index):
    while True:
        emp_id = input("Enter employee id: ")
        if emp_id.isdigit():
            emp_id = int(emp_id)
            break
        else:
            print("Invalid Employee ID. Please enter a valid id.")

    for entry in index:
        if entry["id"] == emp_id:
            print("Employee with the given ID already exists!")
            return

    while True:
        name = input("Enter employee name: ")
        if name.isalpha():
            break
        else:
            print("Invalid name. Please enter letters only.")

    while True:
        salary = input("Enter employee salary: ")
        if salary.isdigit():
            salary = float(salary)
            break
        else:
            print("Invalid salary. Please enter a valid number.")

    while True:
        designation = input("Enter employee designation: ")
        if designation.isalpha():
            break
        else:
            print("Invalid designation. Please enter letters only.")

    while True:
        phone = input("Enter employee phone number : ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Check your number and Enter valid number : ")

    new_employee = {
        "id": emp_id,
        "name": name,
        "salary": salary,
        "designation": designation,
        "phone": phone
    }

    employees.append(new_employee)
    employees.sort(key=lambda x: x["id"])

    index = generate_primary_index(employees)
    update_index(index)
    write_data(employees)
    print("Employee added successfully!")

def display_employees(employees):
    for employee in employees:
        print(f"Employee ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Salary: {employee['salary']}")
        print(f"Designation: {employee['designation']}")
        print(f"Phone Number: {employee['phone']}")
        print("")

def search_employee(employees):
    emp_id = int(input("Enter employee ID to search: "))

    for employee in employees:
        if employee["id"] == emp_id:
            print(f"Employee ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Salary: {employee['salary']}")
            print(f"Designation: {employee['designation']}")
            print(f"Phone Number: {employee['phone']}")
            print("")
            return

    print("Employee not found!")


def modify_employee(employees, index):
    while True:
        emp_id = input("Enter employee id: ")
        if emp_id.isdigit():
            emp_id = int(emp_id)
            break
        else:
            print("Invalid Employee ID. Please enter a valid id.")

    for employee in employees:
        if employee["id"] == emp_id:
            print("Current Details:")
            print(f"Employee ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Salary: {employee['salary']}")
            print(f"Designation: {employee['designation']}")
            print(f"Phone Number: {employee['phone']}")
            print("")

            while True:
                name = input("Enter modified name (press enter to keep the current value): ")
                if not name or name.isalpha():
                    break
                else:
                    print("Invalid name. Please enter letters only.")

            while True:
                salary = input("Enter modified salary (press enter to keep the current value): ")
                if not salary or (salary.isdigit() and len(salary) == 10):
                    if salary:
                        employee["salary"] = float(salary)
                    break
                else:
                    print("Invalid salary. Please enter in digits only. ")

            while True:
                designation = input("Enter modified designation (press enter to keep the current value): ")
                if not designation or designation.isalpha():
                    break
                else:
                    print("Invalid designation. Please enter letters only.")

            while True:
                phone = input("Enter modified phone number (press enter to keep the current value): ")
                if not phone or (phone.isdigit() and len(phone) == 10):
                    if phone:
                        employee["phone"] = phone
                    break
                else:
                    print("Invalid phone number. Please enter 10 digits only.")

            write_data(employees)
            index = generate_primary_index(employees)
            update_index(index)
            print("Employee details modified successfully!")
            return

    print("Employee not found!")



def delete_employee(employees, index):
    emp_id = int(input("Enter employee ID to delete: "))

    for i, employee in enumerate(employees):
        if employee["id"] == emp_id:
            employees.remove(employee)  # Remove the employee from the list
            index = generate_primary_index(employees)  # Update the primary index
            update_index(index)
            write_data(employees)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")

def delete_all_employees(employees):
    employees.clear()  # Clear all employee records
    index = generate_primary_index(employees)  # Update the primary index
    update_index(index)
    write_data(employees)
    print("All employees deleted successfully!")

import time

def main():
    employees = read_data()
    index = read_index()

    while True:
        print("\n========== Employee Management System ==========")
        print("                MENU OPTIONS")
        print("================================================")
        print("1. Add Employee")
        time.sleep(0.5)
        print("2. Display Employees")
        time.sleep(0.5)
        print("3. Search Employee")
        time.sleep(0.5)
        print("4. Modify Employee")
        time.sleep(0.5)
        print("5. Delete Employee")
        time.sleep(0.5)
        print("6. Delete All Employees")
        time.sleep(0.5)
        print("7. Quit")
        time.sleep(0.5)
        print("================================================")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            print("\n===== Add Employee =====")
            add_employee(employees, index)
        elif choice == "2":
            print("\n=== Display Employees ===")
            display_employees(employees)
        elif choice == "3":
            print("\n==== Search Employee ====")
            search_employee(employees)
        elif choice == "4":
            print("\n=== Modify Employee ===")
            modify_employee(employees, index)
        elif choice == "5":
            print("\n=== Delete Employee ===")
            delete_employee(employees, index)
        elif choice == "6":
            print("\n== Delete All Employees ==")
            delete_all_employees(employees)
        elif choice == "7":
            print("\nThank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
