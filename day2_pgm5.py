#5 tuples (ID, Name, Age, Department)
def emp_details(sel):
    if 1<= sel <=5:
        emp = employees[sel-1]#to comply with index no.
        print(f"Employee ID: {emp[0]}")
        print(f"Name: {emp[1]}")
        print(f"Age: {emp[2]}")
        print(f"Department: {emp[3]}")
    else:
        print("Invalid selection.\nPlease choose a number between 1-5")

emp1 = (123, 'Akash', 35, 'Finance')
emp2 = (234, 'Bharath', 38, 'Marketing')
emp3 = (345, 'Chethana', 34, 'Sales')
emp4 = (456, 'Disha', 28, 'HR')
emp5 = (567, 'Eshwar', 32, 'IT')
employees = [emp1, emp2, emp3, emp4, emp5]
#selection = int(input("Select an employee (1-5):"))
emp_details(int(input("Select an employee (1-5):")))
