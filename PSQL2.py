##Insert value data
import mysql.connector as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="emp1")
print(mydb)
mycursor=mydb.cursor()
sql="insert into customers(name,address) values(%s,%s)"
val=("Chan Chan","Dawei")
#mycursor.execute(sql,val)
#mydb.commit()
#print(str(mycursor.rowcount)+" is inserted.")

##Multiple data insertion
import mysql.connector as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="emp1")
print(mydb)
mycursor=mydb.cursor()
val=[
    ("GG","Google"),
    ("HH","Hogwarts"),
    ("PP","UK")
]
values=','.join(map(str,val))
sql="insert into customers(name,address) values {}".format(values)
print(sql)
#mycursor.execute(sql)
#mydb.commit()
#print(str(mycursor.rowcount)+" is inserted")

##Query the data
mycursor.execute("select * from customers")
#mycursor.execute("selcet name from customers where address='UK')
#("select count(*) from customers where address='UK'")
results=mycursor.fetchall()
for x in results:
    print(x)
#print(results)



