import mysql.connector
#table creation and insert values
db=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")
mycursor=db.cursor()
# mycursor.execute("create table marks(tamil_mark int,english_mark int)")

sqlform="insert into marks (tamil_mark ,english_mark) values(80,90)"

# sqlform =("insert into students(PersonID,LastName,FirstName,Address,City ) values('3', 'sajna', 'parveen', 'karur', 'karur')")
# mycursor.execute(sqlform)
# db.commit()

#altertable
mycursor.execute("ALTER TABLE  marks ADD contact int")
