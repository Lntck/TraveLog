# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Login_form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 301, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Auth_lgn = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Auth_lgn.setStyleSheet("background-color: #DCDCDC;\n"
                                    "width: 100%;\n"
                                    "padding: 12px;\n"
                                    "border: 0pч;\n"
                                    "border-radius: 13px;\n"
                                    "box-sizing: border-box;\n"
                                    "font-family: \"Georgia\";")
        self.Auth_lgn.setText("")
        self.Auth_lgn.setMaxLength(20)
        self.Auth_lgn.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Auth_lgn.setObjectName("Auth_lgn")
        self.verticalLayout.addWidget(self.Auth_lgn)
        self.Auth_psw = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Auth_psw.setStyleSheet("background-color: #DCDCDC;\n"
                                    "width: 100%;\n"
                                    "padding: 12px;\n"
                                    "border: 0pч;\n"
                                    "border-radius: 13px;\n"
                                    "box-sizing: border-box;\n"
                                    "font-family: \"Georgia\";\n"
                                    "letter-spacing: 2px;")
        self.Auth_psw.setText("")
        self.Auth_psw.setMaxLength(20)
        self.Auth_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Auth_psw.setObjectName("Auth_psw")
        self.verticalLayout.addWidget(self.Auth_psw)
        self.Auth_btn = QtWidgets.QPushButton(self.widget)
        self.Auth_btn.setGeometry(QtCore.QRect(50, 320, 301, 61))
        self.Auth_btn.setStyleSheet("display: inline-block;\n"
                                    "margin: 10px 0px;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: #4267B2;\n"
                                    "background-position: 100% 0;\n"
                                    "font:19pt;\n"
                                    "font-family: \"Georgia\";\n"
                                    "font-weight: bold;\n"
                                    "color: white;\n"
                                    "box-shadow: 0 16px 32px 0 rgba(0, 40, 120, .35);\n"
                                    "transition: .5s;")
        self.Auth_btn.setObjectName("Auth_btn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 230, 101, 31))
        self.label.setStyleSheet("font-family: \"Georgia\";\n"
                                 "font-size: 14px;\n"
                                 "font-weight: 300;\n"
                                 "color: #A5A5A5;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-10, 30, 421, 61))
        self.label_2.setStyleSheet("font:19pt;\n"
                                   "font-family: \"Georgia\";\n"
                                   "font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ToRegister_btn = QtWidgets.QPushButton(self.widget)
        self.ToRegister_btn.setGeometry(QtCore.QRect(150, 230, 141, 31))
        self.ToRegister_btn.setStyleSheet("color: blue;\n"
                                          "font-size: 14px;\n"
                                          "border-radius: 20px;\n"
                                          "background-color: #f0f0f0;\n"
                                          "font-family: \"Georgia\";")
        self.ToRegister_btn.setObjectName("ToRegister_btn")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.Auth_lgn.setPlaceholderText(_translate("MainWindow", "Login:"))
        self.Auth_psw.setPlaceholderText(_translate("MainWindow", "Password:"))
        self.Auth_btn.setText(_translate("MainWindow", "Авторизоваться"))
        self.label.setText(_translate("MainWindow", "Нет аккаунта? "))
        self.label_2.setText(_translate("MainWindow", "Войдите"))
        self.ToRegister_btn.setText(_translate("MainWindow", "Зарегистрируйтесь!"))
