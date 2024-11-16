import sqlite3
from abc import ABC, abstractmethod
from contextlib import closing

db_path = 'sample-database.db'
def get_connection(db_path):
    return closing(sqlite3.connect(db_path))

def get_employee(db_path, employee_id):
    with get_connection(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?",(employee_id,))
        return cursor.fetchone()

def create_employee(database_path, first_name, last_name):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO employees (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        connection.commit()
        return cursor.lastrowid

def update_employee(database_path, employee_id, name=None, bio=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET name=? WHERE id=?", (name, employee_id))
        if bio:
            cursor.execute("UPDATE employees SET bio=? WHERE id=?", (bio, employee_id))
        connection.commit()


def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        connection.commit()


emp = get_employee(db_path, 101)
for i in emp:
    print(i)


# Class yordamida crud_sql buyruqlari

class BaseCRUD(ABC):
    def __init__(self, database_path, table_name):
        self.database_path = database_path
        self.table_name = table_name

    def get_connection(self):
        return closing(sqlite3.connect(self.database_path))


    def insert(self, **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(kwargs.values()))
            connection.commit()
            return cursor.lastrowid


    def get(self, id, id_column="id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            return cursor.fetchone()


    def update(self, id, id_column="id", **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(f"{key}=?" for key in kwargs)
            query = f"UPDATE {self.table_name} SET {columns} WHERE {id_column}=?"
            cursor.execute(query, (*kwargs.values(), id))
            connection.commit()


    def delete(self, id, id_column="id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            connection.commit()
# Insert a new employee
author_id = BaseCRUD.insert("sample-database (5).db", "employees", name="John Doe", bio="A tech enthusiast")

# Retrieve the employee
employees = BaseCRUD.get("sample-database (5).db", "employees",101,"employee_id")
print(employees)


BaseCRUD.update("sample-database (5).db", "employees", 101,"employee_id", first_name="Nena")
# employees = get("sample-database (5).db", "employees",101,"employee_id")
# print(employees)

# Delete the employee
BaseCRUD.delete("sample-database (5).db", "employees", 101)















