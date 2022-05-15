import mysql.connector
#update table
db=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")
mycursor=db.cursor()
#
# update='''update students set LastName='parveen' where PersonID=2 '''
# mycursor.execute(update)
#
#
# delete='''delete from students where PersonID=3 '''
# mycursor.execute(delete)
# db.commit()

# mycursor.execute("select * from students")
# myresult=mycursor.fetchall()
# for row in myresult:
#     print(row)

update='''update marks set contact='2' where tamil_mark=80 '''
mycursor.execute(update)
db.commit()