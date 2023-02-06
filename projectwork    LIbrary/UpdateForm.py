from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog
import sys
import mysql.connector as sql

class UpdateFormUI(QDialog):
    def __init__(self,bid):
        super(UpdateFormUI,self).__init__()
        uic.loadUi('UpdateFormUI.ui',self)
        self.mydb=None
        print("The book id is"+str(bid))
        self.LoadData(bid)
        self.updatebut.clicked.connect(self.UpdateData)
        self.insertbut.clicked.connect(self.InsertData)
        self.deletebut.clicked.connect(self.DeleteData)
        self.clearbut.clicked.connect(self.ClearData)

    def UpdateData(self):
        id=self.idtxt.toPlainText()
        title=self.titletxt.toPlainText()
        author=self.authortxt.toPlainText()
        publisher=self.publishertxt.toPlainText()
        copy=self.numcopytxt.toPlainText()
        self.DBConnect()
        cursor=self.mydb.cursor()
        sql_update="update booktb set title=%s, author=%s,publisher=%s,num_of_copies=%s where book_id="+str(id) 
        value=(title,author,publisher,copy)
        cursor.execute(sql_update,value)
        self.mydb.commit()
        self.showMessageText("Updated Successfully","OK")
        

    def showMessageText(self,body,title):
        from PyQt5.QtWidgets import QMessageBox
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(body)
        msg.setWindowTitle(title)
        msg.exec_()


    def InsertData(self):
        id=self.idtxt.toPlainText()
        title=self.titletxt.toPlainText()
        author=self.authortxt.toPlainText()
        publisher=self.publishertxt.toPlainText()
        copy=self.numcopytxt.toPlainText()
        self.DBConnect()
        cursor=self.mydb.cursor()
        insert_sql="insert into booktb(book_id,title,author,publisher,num_of_copies) values(%s,%s,%s,%s,%s)"
        value=(id,title,author,publisher,copy)  
        cursor.execute(insert_sql,value)
        self.mydb.commit()
        #self.ClearData()
        self.showMessageText("Insert successfully done","OK")

    def DeleteData(self):
        id=self.idtxt.toPlainText()
        if len(id)==0:
            self.showMessageText("Enter book Id to delete","No Data Error")
        else:
            self.DBConnect()
            cursor=self.mydb.cursor()
            delete_str="delete from booktb where book_id="+str(id)
            cursor.execute(delete_str)
            self.mydb.commit()
            self.ClearData()
            self.showMessageText("Delete data is successfully done","OK")

    def ClearData(self):
        self.idtxt.setPlainText("")
        self.titletxt.setPlainText("")
        self.authortxt.setPlainText("")
        self.publishertxt.setPlainText("")
        self.numcopytxt.setPlainText("")
        

    def LoadData(self,bid):
        self.DBConnect()
        sql="select * from booktb where book_id="+str(bid)
        cursor=self.mydb.cursor()
        cursor.execute(sql)
        values=cursor.fetchone()
        self.idtxt.setPlainText(str(values[1]))
        self.titletxt.setPlainText(values[2])
        self.authortxt.setPlainText(values[3])
        self.publishertxt.setPlainText(values[4])
        self.numcopytxt.setPlainText(str(values[5]))

    def DBConnect(self):
        import mysql.connector as c
        try:
            self.mydb=c.connect(
                host="localhost",
                user="root",
                password="YourPassword",
                database="libarydb"

            )   
        except c.Error as err:
            print("Something went wrong: {}".format(err)) 
    

if __name__=="__main__":
    app=QtWidgets.QApplication([])
    win=UpdateFormUI(1111)
    win.show()
    sys.exit(win.exec_())