import mysql.connector

# Define the database connection parameters
username = 'root'
password = ''
host = 'localhost'
database = 'sampledb'

# Establish a connection to the database
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT,
        name VARCHAR(50),
        age INT,
        salary INT,
        PRIMARY KEY (id)
    )
""")

# Commit the changes
cnx.commit()

print("Connected to the database and created the employees table")

# Create (Insert)
def create_employee(name, age, salary):
    query = "INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)"
    values = (name, age, salary)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Inserted 1 row into employees")

create_employee('John Doe', 30, 50000)
create_employee('Jane Doe', 31, 60000)

# Read (Select)
def read_employees():
    query = "SELECT * FROM employees"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Salary: {row[3]}")

read_employees()

# Update
def update_employee(name, age, salary, id):
    query = "UPDATE employees SET name = %s, age = %s, salary = %s WHERE id = %s"
    values = (name, age, salary, id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Updated 1 row in employees")

update_employee('John Doe Updated', 31, 55000, 1)

# Read (Select) again to see the updated result
read_employees()

# Delete
def delete_employee(id):
    query = "DELETE FROM employees WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Deleted 1 row from employees")

delete_employee(2)

# Read (Select) again to see the deleted result
read_employees()

# Close the cursor and connection
cursor.close()
cnx.close()

print("Disconnected from the database")
