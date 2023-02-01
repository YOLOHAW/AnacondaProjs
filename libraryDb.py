import mysql.connector as sql
db=sql.connect(
    host="localhost",
    user="root",
    password="YourPassword")
#print(db)

##show dbs
#mycursor=db.cursor()
#mycursor.execute("show databases")
#for x in mycursor:
#    print(x)

##Create database
#mycursor=db.cursor()
#mycursor.execute("create database libaryDb")
#print("Created new db")

##Connectin gto created db
import mysql.connector as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="libaryDb")
print("Connected")
print(mydb)

##Creating a table
#mycursor=mydb.cursor()
#mycursor.execute("create table book_tb(id int not null,book_name varchar(20),author varchar(20),published varchar(4),primary key (id))")
#print('Created new Table')

##Creating a new table again
#mycursor=mydb.cursor()
#mycursor.execute("create table login_tb(id int not null primary key,name varchar(20),password varchar(20),role varchar(20))")
#print('Create login table')

##Add new column to book_tb
#mycursor=mydb.cursor()
#mycursor.execute("alter table book_tb add number_of_copies int")
#print("add new column to book table")

##Delete column
#mycursor=mydb.cursor()
#mycursor.execute("alter table book_tb drop published")
#print("deleted column")

##Rename table
#mycursor=mydb.cursor()
#mycursor.execute("alter table book_tb rename to book_tbLayParBya")
#print("Renamed table")

##Change column Name
#mycursor=mydb.cursor()
#mycursor.execute("alter table login_tb change name nickname int")
#print("Changed column name")



