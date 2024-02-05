import mysql.connector
host = 'localhost'
user = 'root'
password = 'root@12345'
database = 'mydb'
#Creating a connection cursor
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = connection.cursor()

cursor.execute(f"USE {database}")


#table info
table_info = """ 
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
 
cursor.execute(table_info)

#Executing SQL Statements
cursor.execute(''' INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES
('John Doe', '10th', 'A', 85),
('Jane Smith', '11th', 'B', 92),
('Bob Johnson', '9th', 'C', 78),
('Alice Brown', '12th', 'A', 95),
('Charlie Lee', '8th', 'D', 68)''')

#Display all the records
print("The inserted record are")

cursor.execute('Select * From STUDENT')

data = cursor.fetchall()

# Check if data is not None before iterating
if data is not None:
    print("The inserted records are:")
    for row in data:
        print(row)
else:
    print("No records found.")

 
#Saving the Actions performed on the DB
connection.commit()
 
#Closing the cursor
cursor.close()