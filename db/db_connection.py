import json
import mysql.connector

class Employee:
    def __init__(self, employeeId, firstName, lastName, salary, role):
        self.employeeId = employeeId
        self.firstName = firstName
        self.lastName=lastName
        self.salary= salary
        self.role = role


mydb = mysql.connector.connect(
  host="localhost",
  user="dev_user",
  passwd="devuser",
  database="code_orange"
)
mycursor = mydb.cursor()
mycursor.execute("select * from employee")
myresult = mycursor.fetchall()
print(myresult)
employees = []

for x in myresult:
#   print(x)
  employees.append(Employee(x[0], x[1], x[2], x[3], x[4]))
    
for emp in employees:
    if emp.firstName == 'Bhagat':
        print(emp.employeeId, emp.firstName, emp.lastName, emp.salary, emp.role)

'''
What is Relational and No Sql databases, why we need them?
Type of database?

Relational Databases:
1- Oracle Database    - Oracle
2- Sql Server         - Microsoft
3- MySql              - Oracle
4- amazon aurora      - Amazon
5- PostgreSQL   
6- SQLite 
7- Apache Derby
8- H2 
The Codd's 12 rules -> https://www.studytonight.com/dbms/codd-rule.php

No Sql:
    Document Based
    Column Base

SQL: Structured Query Language
SELECT
UPDAET
DELETE
CREATE
JOIN(INNER, OUTER)

No SQL Database:
 - MongoDB
 - CouchDB
 - DynomoDB
 - Cassandra
 - 
'''