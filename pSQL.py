###connect to databases of database
import mysql.connector as sql
mydb=sql.connect(
    host="localhost",
    user="root",
    password="YourPassword")
print(mydb)
##show databases
#mycursor=mydb.cursor()
#mycursor.execute("show databases")
#for x in mycursor:
#    print(x)
###Create database
#mycursor.execute("create database testing")
#print("Created")

###Connecting to created database
import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="emp1")
#print('connected')
###Creating a table
#mycursor=mydb.cursor()
#mycursor.execute("create table customers(name varchar(20),address varchar(30))")
#print('created')                 

###Add primary key ot existing table
#mycursor=mydb.cursor()
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#print("altered")

###checking tables
mycursor=mydb.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)

###create a table with primary key
mycursor=mydb.cursor()
mycursor.execute("create table ambiverts(id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20),address varchar(20))")
print("table with primary key")

