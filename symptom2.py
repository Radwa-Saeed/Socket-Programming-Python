# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symptom2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setStyleSheet("  QWidget {\n"
"            \n"
"    background-color: rgb(255, 255, 255);\n"
"            color:  rgb(52, 143, 217);\n"
"font-weight: 500;\n"
"font-size:13px;\n"
"            }\n"
"QLabel{color: rgb(91, 91, 91);}\n"
"QLabel#label_8{\n"
"color: rgb(0,0,0);\n"
"font-size:30px\n"
"\n"
"}\n"
"QLabel#label_9{background-image: url(:/newPrefix/appointment.png);}\n"
"QLabel#label_7{\n"
"    color: rgb(91, 91, 91);}\n"
"QPushButton#pushButton{\n"
"  background-color: #0078d0;\n"
"  border: 0;\n"
"  border-radius: 20px;\n"
"  color: #fff;\n"
"  display: inline-block;\n"
"  font-family: system-ui,-apple-system,system-ui,\"Segoe UI\",Roboto,Ubuntu,\"Helvetica Neue\",sans-serif;\n"
"  font-size: 18px;\n"
"  font-weight: 600;\n"
"  outline: 0;\n"
"  padding: 16px 21px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  transition: all .3s;\n"
" }\n"
"\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgb(0, 80, 138);\n"
"cursor:pointer;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"color: rgb(0, 80, 138);\n"
"cursor:pointer;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 330, 461, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("border:none;\n"
"text-decoration:underline;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 120, 461, 211))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, 5, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 40, 481, 62))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit symptoms"))
        self.label_7.setText(_translate("MainWindow", "Once you submit we will get back to you again very shortly with the diagnosis."))
        self.pushButton_2.setText(_translate("MainWindow", "Switch to live chat instead?"))
        self.label.setText(_translate("MainWindow", "Do you have a fever?"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "No"))
        self.label_2.setText(_translate("MainWindow", "Do you have a headache?"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "No"))
        self.label_3.setText(_translate("MainWindow", "Do you have a sore throat?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox.setItemText(1, _translate("MainWindow", "No"))
        self.label_4.setText(_translate("MainWindow", "Do you have a runny or stuffy nose?"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "No"))
        self.label_5.setText(_translate("MainWindow", "Are you facing shortness of breath?"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "No"))
        self.label_6.setText(_translate("MainWindow", "Do you feel any aches and pain?"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "No"))
        self.label_8.setText(_translate("MainWindow", "What Are Your Symptoms?"))

import images_rc
