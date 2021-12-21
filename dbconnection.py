from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
import mysql.connector
 
 
class Window(QDialog):
    def __init__(self):
        super().__init__()
 
        self.title = "PyQt5 Database Connection"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.button = QPushButton('DB Connection', self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.DBConnection)
 
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
 
    def DBConnection(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql",
                database="Socket")
            # mycursor = db.cursor(buffered=True)  
            # mycursor.execute("CREATE TABLE IF NOT EXISTS Doctors(Dcode VARCHAR (255)  NOT NULL PRIMARY KEY,password VARCHAR(255) UNIQUE NOT NULL , Dname VARCHAR(255),Mname VARCHAR(255),Lname VARCHAR(255),phone INT(50),mail VARCHAR(255) UNIQUE,Birth_date Date,Doctor_ID INT(150) UNIQUE,syndicate_number INT (100) UNIQUE,salary INT(50),gender VARCHAR(255),address text,job_rank VARCHAR(255),access_level int DEFAULT 2,image LONGBLOB,calendarid VARCHAR (600) UNIQUE )")
            # db.commit()
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
 
        except mysql.connector.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
