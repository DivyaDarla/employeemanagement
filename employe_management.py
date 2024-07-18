import mysql.connector
from mysql.connector import Error
from db_config import create_connection, close_connection

class Employee:
    def __init__(self, employee_id, name, department, designation, performance_score=0):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.performance_score = performance_score

    def update_employee(self, name=None, department=None, designation=None, performance_score=None):
        if name is not None:
            self.name = name
        if department is not None:
            self.department = department
        if designation is not None:
            self.designation = designation
        if performance_score is not None:
            self.performance_score = performance_score

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Dept: {self.department}, Desig: {self.designation}, Score: {self.performance_score}"

class EmployeeManager:
    def __init__(self):
        self.connection = create_connection()

    def add_employee(self, employee):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO Employees (employee_id, name, department, designation, performance_score)
                VALUES (%s, %s, %s, %s, %s)
            """, (employee.employee_id, employee.name, employee.department, employee.designation, employee.performance_score))
            self.connection.commit()
            print("Employee added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()

    def update_employee(self, employee_id, **kwargs):
        cursor = self.connection.cursor()
        updates = ", ".join([f"{k}=%s" for k in kwargs if kwargs[k] is not None])
        values = tuple(v for v in kwargs.values() if v is not None)
        query = f"UPDATE Employees SET {updates} WHERE employee_id=%s"
        values += (employee_id,)
        try:
            cursor.execute(query, values)
            self.connection.commit()
            if cursor.rowcount:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()

    def delete_employee(self, employee_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM Employees WHERE employee_id=%s", (employee_id,))
            self.connection.commit()
            if cursor.rowcount:
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()

    def update_performance_score(self, employee_id, score):
        self.update_employee(employee_id, performance_score=score)

    def add_performance_review(self, employee_id, review_date, review_comments):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO PerformanceReviews (employee_id, review_date, review_comments)
                VALUES (%s, %s, %s)
            """, (employee_id, review_date, review_comments))
            self.connection.commit()
            print("Performance review added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()

    def get_top_performers(self, threshold=85):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM Employees WHERE performance_score > %s", (threshold,))
            result = cursor.fetchall()
            top_performers = [Employee(*row) for row in result]
            return top_performers
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")
            return []
        finally:
            cursor.close()

    def __del__(self):
        close_connection(self.connection)