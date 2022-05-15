import mysql.connector
#join table
db=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")
mycursor=db.cursor()

join='''SELECT * from students INNER JOIN marks ON students.PersonID = marks.contact'''
mycursor.execute(join)
result = mycursor.fetchall();
print(result)

