import json


class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Title:", self.title)
        print("Department:", self.department)

    def __str__(self):
        return f"{self.name} ({self.emp_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.emp_id == employee_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        if self.employees:
            print(f"Employees in {self.name}:")
            for employee in self.employees:
                print(employee)
        else:
            print(f"No employees in {self.name}")


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print(f"Department '{department_name}' already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print(f"Department '{department_name}' does not exist.")

    def display_departments(self):
        if self.departments:
            print("Departments:")
            for department in self.departments.values():
                print(department.name)
        else:
            print("No departments found.")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.departments, file, default=lambda o: o.__dict__, indent=4)
        print("Data saved successfully.")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for department_name, department_data in data.items():
                department = Department(department_name)
                for emp_data in department_data['employees']:
                    employee = Employee(**emp_data)
                    department.add_employee(employee)
                self.departments[department_name] = department
        print("Data loaded successfully.")


def print_menu():
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. List Departments")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")


def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")
            if department in company.departments:
                employee = Employee(name, emp_id, title, department)
                company.departments[department].add_employee(employee)
                print("Employee added successfully.")
            else:
                print("Department not found.")

        elif choice == '2':
            emp_id = input("Enter employee ID to remove: ")
            removed = False
            for department in company.departments.values():
                if department.remove_employee(emp_id):
                    print("Employee removed successfully.")
                    removed = True
                    break
            if not removed:
                print("Employee not found.")

        elif choice == '3':
            department_name = input("Enter department name to list employees: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Department not found.")

        elif choice == '4':
            department_name = input("Enter new department name: ")
            company.add_department(department_name)

        elif choice == '5':
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)

        elif choice == '6':
            company.display_departments()

        elif choice == '7':
            filename = input("Enter filename to save data: ")
            company.save_data(filename)

        elif choice == '8':
            filename = input("Enter filename to load data: ")
            company.load_data(filename)

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
