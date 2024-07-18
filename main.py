from employe_management import Employee, EmployeeManager

def main():
    manager = EmployeeManager()

    while True:
        print("\n1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Update Performance Score")
        print("5. Add Performance Review")
        print("6. View Top Performers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            performance_score = int(input("Enter Performance Score: "))
            try:
                manager.add_employee(Employee(employee_id, name, department, designation, performance_score))
            except Exception as e:
                print(e)
        
        elif choice == '2':
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Name (leave blank to skip): ") or None
            department = input("Enter Department (leave blank to skip): ") or None
            designation = input("Enter Designation (leave blank to skip): ") or None
            performance_score = input("Enter Performance Score (leave blank to skip): ")
            performance_score = int(performance_score) if performance_score else None
            try:
                manager.update_employee(employee_id, name=name, department=department, designation=designation, performance_score=performance_score)
            except Exception as e:
                print(e)

        elif choice == '3':
            employee_id = int(input("Enter Employee ID: "))
            try:
                manager.delete_employee(employee_id)
            except Exception as e:
                print(e)
        
        elif choice == '4':
            employee_id = int(input("Enter Employee ID: "))
            score = int(input("Enter Performance Score: "))
            try:
                manager.update_performance_score(employee_id, score)
            except Exception as e:
                print(e)
        
        elif choice == '5':
            employee_id = int(input("Enter Employee ID: "))
            review_date = input("Enter Review Date (YYYY-MM-DD): ")
            review_comments = input("Enter Review Comments: ")
            try:
                manager.add_performance_review(employee_id, review_date, review_comments)
            except Exception as e:
                print(e)

        elif choice == '6':
            top_performers = manager.get_top_performers()
            print("\nTop Performers:")
            for emp in top_performers:
                print(emp)

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()