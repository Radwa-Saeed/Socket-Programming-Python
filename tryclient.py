from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox  

from Symptom import Ui_MainWindow
import os
import socket
import sys
import errno

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Online_Diagnosis")
        self.msg = QMessageBox()

        self.ui.Combos= [ self.ui.comboBox_2 , self.ui.comboBox_3,self.ui.comboBox , self.ui.comboBox_4 , self.ui.comboBox_5, self.ui.comboBox_6 ]
        self.answers = []
        self.a=0
        self.y=0
        self.n=0
        for Combo in self.ui.Combos:
            Combo.activated.connect(self.take_answers)
        self.ui.pushButton.clicked.connect(lambda: self.get_diagnasis(self.y,self.n))
        self.HEADER_LENGTH = 10

        self.IP = "127.0.0.1"
        self.PORT = 5000
        self.my_username = input("Username: ")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.IP, self.PORT))
# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
        self.client_socket.setblocking(False)
# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
        username = self.my_username.encode('utf-8')
        username_header = f"{len(username):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)
    def take_answers(self):
        if (self.a<=5):  
            answer=self.ui.Combos[self.a].currentText()
            message = answer.encode('utf-8')
            message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode('utf-8')
            self.client_socket.send(message_header + message)
            if answer == "Yes":   
               self.y=self.y+1
            elif answer == "No":  
               self.n=self.n+1               
            self.answers.append(answer)
            self.a=self.a+1
                 # Now we want to loop over received messages (there might be more than one) and print them
            while True:
                    # Receive our "header" containing username length, it's size is defined and constant
                    username_header = self.client_socket.recv(self.HEADER_LENGTH)
                    # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()
                    # Convert header to int value
                    username_length = int(username_header.decode('utf-8').strip())
                    # Receive and decode username
                    username = self.client_socket.recv(username_length).decode('utf-8')
                    # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                    message_header = self.client_socket.recv(self.HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = self.client_socket.recv(message_length).decode('utf-8')
                    # Print message
                    print(f'{username} > {message}')
                    #print(answer)
        if (self.a>5):
            self.a=0
            #self.y=0
            #self.n=0
            print(self.answers)
            self.answers=[]
              
    def get_diagnasis(self,k,l):     
        if (k==6 and l==0) or (k==5 and l==1) :
           QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "covid_19")
            #sys.exit()
           print("covid_19")
        elif (k==4 and l==2):
            QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "Flu")
            print("FLu")
        elif (k==3 and l==3):
            QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "May be Flu or colds")
            print("May be Flu or colds")
        elif k==2 and l==4:
            QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "colds")
            print ("colds")
        elif k==0 and l==6:
            QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "you are fineee")
            print("you are fineee")
        else:
            QtWidgets.QMessageBox.about(self, "Diagnosis Reault", "please answer all questions")
            print("please answer all questions")
        print(k)
        print(l)

        self.y=0
        self.n=0    
               

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
      main()
       