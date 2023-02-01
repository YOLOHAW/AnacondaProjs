import mysql.connector as sql
class LoginClass:
    def __init__(self):
        try:
            self.db2=sql.connect(
            host="localhost",
            user="root",
            password="YourPassword",
            database="libarydb"
            )
            self.mycur=self.db2.cursor() #global variable
            
        except:
            print("DB error")

    def logincheckfun(self):
        self.mycur.execute("select * from logintb")
        values=self.mycur.fetchall()
        for x in values:
            print(x)
if __name__=="__main__":
    login=LoginClass()
    login.logincheckfun()



