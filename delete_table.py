import mysql.connector
#table creation and insert values
db=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")
mycursor=db.cursor()
mycursor.execute("DELETE FROM students")