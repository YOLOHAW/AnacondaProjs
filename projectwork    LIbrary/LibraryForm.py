from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtWidgets,uic
import sys
import mysql.connector as sql

class LibrarySystem(QDialog):
    def __init__(self):
        super(LibrarySystem,self).__init__()
        self.mydb=None
        uic.loadUi('LibraryFormUi.ui',self)
        self.searchButton.clicked.connect(self.SearchBook)
        self.tableView.clicked.connect(self.TableSelect)
        self.updateBut.clicked.connect(self.UpdateData)

    def TableSelect(self):
        self.updateBut.setEnabled(True)
    def UpdateData(self):
        index=self.tableView.selectionModel().currentIndex()
        value=index.sibling(index.row(),index.column()).data()
        from UpdateForm import UpdateFormUI
        ui=UpdateFormUI(value)
        ui.show()
        ui.exec_() 


    def SearchBook(self):
        choosetype=None
        datainput=None
        if self.radioAuthor.isChecked():
            choosetype="author"
        elif self.radioTitle.isChecked():
            choosetype="title"
        else:
            choosetype="publisher"

        datainput=self.inputtxt.toPlainText().strip()
        print(choosetype)
        print(datainput)
        sql_str="select * from booktb where "+choosetype+" = '"+datainput+"'"
        print(sql_str)
        self.DBConnect()
        cursor=self.mydb.cursor()
        cursor.execute(sql_str)
        rows=cursor.fetchall()
         
        if len(rows)==0:
            from PyQt5.QtWidgets import QMessageBox
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Your information is not found, Try another search")
            msg.setWindowTitle("No Data")
            msg.exec()
        else:
            import pandas as pd
            sql_query=pd.read_sql(sql_str,self.mydb)
            df=pd.DataFrame(sql_query,columns=['id','title','author','publisher','num_of_copies'])
            from tableModel import pandasModel
            model=pandasModel(df)
            self.tableView.setModel(model)
            #plain text instead tableView
            # for x in rows:
            #     for y in range(len(x)):
            #         self.plainTextEdit_2.appendPlainText(str(x[y]))

    def DBConnect(self):
        try:
            self.mydb=sql.connect(
                host="localhost",
                user="root",
                password="YourPassword",
                database="libarydb"
            )
        except:
            print("Something went wrong")

if __name__=="__main__":
    app=QtWidgets.QApplication([])
    win=LibrarySystem()
    win.show()
    sys.exit(win.exec_())