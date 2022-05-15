import mysql.connector
#database creation
db=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=db.cursor()
# mycursor.execute("create database mydb")
mycursor.execute("show databases")
for dbs in mycursor:
    print(dbs)