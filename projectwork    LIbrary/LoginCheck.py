from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtWidgets,uic
import sys
import mysql.connector as c


class LoginCheckClass(QDialog):
    def __init__(self):
        super(LoginCheckClass,self).__init__()
        self.mydb=None
        uic.loadUi('loginform.ui',self)
        self.photolabel.setPixmap(QPixmap("login.png"))
        self.photolabel.setScaledContents(True)
        self.loginbut.clicked.connect(self.loginfun)
        
    def loginfun(self):
        username=self.usrtxt.toPlainText().strip()
        password=self.pwdtxt.text().strip()
        #Db connect & query
        self.DBConnect()
        cursor=self.mydb.cursor()
        cursor.execute("select * from logintb")
        rows=cursor.fetchall()
        found=0
        for x in rows:
            usr=x[1]
            pwd=x[2]
            if username==usr and password==pwd:
                found=1
                self.setVisible(False)
                from LibraryForm import LibrarySystem
                lib=LibrarySystem()
                lib.show()
                lib.exec_()


        if found==0:
            from PyQt5.QtWidgets import QMessageBox
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Login unsuccessful, Try Again!")
            msg.setWindowTitle("Error Login")
            msg.exec_()

    def DBConnect(self):
        
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
    win=LoginCheckClass()
    win.show()
    sys.exit(win.exec_())