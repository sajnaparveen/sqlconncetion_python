import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="")
print(db)

if(db):
    print("db connected successfully")
else:
  print("db connection failed")