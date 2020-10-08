import mysql.connector

class Department:
    def __init__(self, dept_id, dept_name, dept_location, dept_head):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.dept_location = dept_location
        self.dept_head = dept_head

mydb = mysql.connector.connect(
  host="localhost",
  user="dev_user",
  passwd="devuser",
  database="py_db"
)
mycursor = mydb.cursor()
mycursor.execute("select * from department")
myresult = mycursor.fetchall()

departments = []

for x in myresult:
    departments.append(Department(x[0], x[1], x[2], x[3]))

for dept1 in departments:
    print(dept1.dept_id, dept1.dept_name, dept1.dept_location, dept1.dept_head)