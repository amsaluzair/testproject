class Employee:
    def __init__(self,id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sort_param):
    if sort_param == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_param == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_param == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def print_employees(employees):
    print("ID\t\tName\t\tAge\t\tSalary")
    for emp in employees:
        print(f"{emp.id}\t\t{emp.name}\t\t{emp.age}\t\t{emp.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90","Raman",41,56000),
        Employee("161F91","Himadri",38,67500),
        Employee("161F99","jaya",51,82100),
        Employee("171E20","Tejas",30,55000),
        Employee("171G30","Ajay",45,44000)
    ]

    print("Choose a sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        sort_param = int(input("Enter your choice: "))
        sorted_employees = sort_employees(employees, sort_param)
        print("\nSorted Employee Data:")
        print_employees(sorted_employees)
    except ValueError:
        print("Invalid input. Please enter a valid sorting parameter (1, 2, or 3).")

