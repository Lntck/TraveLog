# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs_icons = QtWidgets.QWidget(self.centralwidget)
        self.tabs_icons.setMinimumSize(QtCore.QSize(70, 0))
        self.tabs_icons.setStyleSheet("background-color:#4267B2;")
        self.tabs_icons.setObjectName("tabs_icons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabs_icons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tabs_icons)
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/logo_transparent.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.tabs_icons)
        self.home_btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.home_btn_1.setStyleSheet("QPushButton{\n"
                                      "    color:white;\n"
                                      "    border:0px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                      "}")
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/home-icon-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(24, 24))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.memory_btn_1 = QtWidgets.QPushButton(self.tabs_icons)
        self.memory_btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.memory_btn_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.memory_btn_1.setStyleSheet("QPushButton{\n"
                                        "    color:white;\n"
                                        "    border:0px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                        "}")
        self.memory_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/album.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.memory_btn_1.setIcon(icon1)
        self.memory_btn_1.setIconSize(QtCore.QSize(24, 24))
        self.memory_btn_1.setCheckable(True)
        self.memory_btn_1.setChecked(False)
        self.memory_btn_1.setAutoRepeat(False)
        self.memory_btn_1.setAutoExclusive(True)
        self.memory_btn_1.setObjectName("memory_btn_1")
        self.verticalLayout.addWidget(self.memory_btn_1)
        self.settings_btn_1 = QtWidgets.QPushButton(self.tabs_icons)
        self.settings_btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.settings_btn_1.setStyleSheet("QPushButton{\n"
                                          "    color:white;\n"
                                          "    border:0px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                          "}")
        self.settings_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn_1.setIcon(icon2)
        self.settings_btn_1.setIconSize(QtCore.QSize(24, 24))
        self.settings_btn_1.setCheckable(True)
        self.settings_btn_1.setAutoExclusive(True)
        self.settings_btn_1.setObjectName("settings_btn_1")
        self.verticalLayout.addWidget(self.settings_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 343, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.tabs_icons)
        self.exit_btn_1.setMinimumSize(QtCore.QSize(0, 70))
        self.exit_btn_1.setStyleSheet("QPushButton{\n"
                                      "    color:white;\n"
                                      "    border:0px;\n"
                                      "    padding-left:10px;\n"
                                      "    padding-right:10px;\n"
                                      "    padding-bottom:10px;\n"
                                      "    padding-upper:30px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                      "}")
        self.exit_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/on-off-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon3)
        self.exit_btn_1.setIconSize(QtCore.QSize(24, 24))
        self.exit_btn_1.setCheckable(True)
        self.exit_btn_1.setAutoExclusive(True)
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.tabs_icons, 0, 0, 1, 1)
        self.tabs_icons_text = QtWidgets.QWidget(self.centralwidget)
        self.tabs_icons_text.setStyleSheet("background-color:#4267B2;")
        self.tabs_icons_text.setObjectName("tabs_icons_text")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabs_icons_text)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.tabs_icons_text)
        self.label_4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_4.setMaximumSize(QtCore.QSize(60, 60))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons/logo_transparent.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.tabs_icons_text)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#F5F5F5;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.tabs_icons_text)
        self.home_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setStyleSheet("QPushButton{\n"
                                      "    color:white;\n"
                                      "    border:0px;\n"
                                      "    border-radius: 3px;\n"
                                      "    text-align: left;\n"
                                      "    padding: 8px 0 8px 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                      "}")
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.memory_btn_2 = QtWidgets.QPushButton(self.tabs_icons_text)
        self.memory_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.memory_btn_2.setStyleSheet("QPushButton{\n"
                                        "    color:white;\n"
                                        "    border:0px;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: left;\n"
                                        "    padding: 8px 0 8px 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                        "}")
        self.memory_btn_2.setIcon(icon1)
        self.memory_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.memory_btn_2.setCheckable(True)
        self.memory_btn_2.setAutoExclusive(True)
        self.memory_btn_2.setObjectName("memory_btn_2")
        self.verticalLayout_2.addWidget(self.memory_btn_2)
        self.settings_btn_2 = QtWidgets.QPushButton(self.tabs_icons_text)
        self.settings_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.settings_btn_2.setStyleSheet("QPushButton{\n"
                                          "    color:white;\n"
                                          "    border:0px;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: left;\n"
                                          "    padding: 8px 0 8px 15px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                          "}")
        self.settings_btn_2.setIcon(icon2)
        self.settings_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn_2.setCheckable(True)
        self.settings_btn_2.setAutoExclusive(True)
        self.settings_btn_2.setObjectName("settings_btn_2")
        self.verticalLayout_2.addWidget(self.settings_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 343, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.tabs_icons_text)
        self.exit_btn_2.setMinimumSize(QtCore.QSize(0, 70))
        self.exit_btn_2.setStyleSheet("QPushButton{\n"
                                      "    color:white;\n"
                                      "    border:0px;\n"
                                      "    padding-left:10px;\n"
                                      "    padding-right:10px;\n"
                                      "    padding-bottom:10px;\n"
                                      "    padding-upper:30px;\n"
                                      "    text-align: left;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: rgba( 86, 101, 115, 0.5)\n"
                                      "}")
        self.exit_btn_2.setIcon(icon3)
        self.exit_btn_2.setIconSize(QtCore.QSize(24, 24))
        self.exit_btn_2.setCheckable(True)
        self.exit_btn_2.setAutoExclusive(True)
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.tabs_icons_text, 0, 1, 1, 1)
        self.MainWin = QtWidgets.QWidget(self.centralwidget)
        self.MainWin.setObjectName("MainWin")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.MainWin)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.MainWin)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setStyleSheet("background-color:#4267B2;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setStyleSheet("QPushButton{\n"
                                      "    background-color:#4267B2;\n"
                                      "    border:0px;\n"
                                      "    padding:10px;\n"
                                      "}")
        self.change_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon4)
        self.change_btn.setIconSize(QtCore.QSize(30, 30))
        self.change_btn.setCheckable(True)
        self.change_btn.setChecked(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_3.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(588, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.MainWin)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setEnabled(True)
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setStyleSheet("font:14pt;\n"
                                   "margin: 0 auto;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.output_note = QtWidgets.QPlainTextEdit(self.page)
        self.output_note.setMinimumSize(QtCore.QSize(200, 0))
        self.output_note.setStyleSheet("font:11pt;")
        self.output_note.setBackgroundVisible(False)
        self.output_note.setObjectName("output_note")
        self.horizontalLayout_4.addWidget(self.output_note)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.timeEdit = QtWidgets.QTimeEdit(self.page)
        self.timeEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.timeEdit.setStyleSheet("margin-left:140px;\n"
                                    "margin-right:140px;\n"
                                    "heigh:20px;")
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_6.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page)
        self.calendarWidget.setStyleSheet("font:11pt;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_6.addWidget(self.calendarWidget)
        self.input_note = QtWidgets.QLineEdit(self.page)
        self.input_note.setMinimumSize(QtCore.QSize(0, 40))
        self.input_note.setObjectName("input_note")
        self.verticalLayout_6.addWidget(self.input_note)
        self.make_note_btn = QtWidgets.QPushButton(self.page)
        self.make_note_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.make_note_btn.setStyleSheet("text-decoration: none;\n"
                                         "display: inline-block;\n"
                                         "margin: 10px 0px;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: #4267B2;\n"
                                         "background-position: 100% 0;\n"
                                         "font-family: \'Montserrat\', sans-serif;\n"
                                         "font-size: 20px;\n"
                                         "font-weight: 300;\n"
                                         "color: white;\n"
                                         "box-shadow: 0 16px 32px 0 rgba(0, 40, 120, .35);\n"
                                         "transition: .5s;\n"
                                         "height:40;")
        self.make_note_btn.setObjectName("make_note_btn")
        self.verticalLayout_6.addWidget(self.make_note_btn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.memory_btn = QtWidgets.QPushButton(self.page)
        self.memory_btn.setMinimumSize(QtCore.QSize(0, 190))
        self.memory_btn.setStyleSheet("background-image: url(\"img/memory_btn.jpg\");\n"
                                      "font:30pt;\n"
                                      "color:#3d5075;\n"
                                      "font-weight:bold;\n"
                                      "background-position: center;")
        self.memory_btn.setObjectName("memory_btn")
        self.gridLayout_2.addWidget(self.memory_btn, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(10, 440, 71, 16))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.MainWin, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.change_btn.toggled['bool'].connect(self.tabs_icons.setVisible)
        self.change_btn.toggled['bool'].connect(self.tabs_icons_text.setHidden)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)
        self.memory_btn.clicked.connect(self.to_mem)
        self.memory_btn_1.clicked.connect(self.to_mem)
        self.memory_btn_2.clicked.connect(self.to_mem)
        self.home_btn_1.clicked.connect(self.to_main)
        self.home_btn_2.clicked.connect(self.to_main)
        self.settings_btn_1.clicked.connect(self.to_set)
        self.settings_btn_2.clicked.connect(self.to_set)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def to_main(self):
        self.stackedWidget.setCurrentIndex(0)

    def to_mem(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_set(self):
        self.stackedWidget.setCurrentIndex(2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "TraveLog"))
        self.home_btn_2.setText(_translate("MainWindow", "Главная страница"))
        self.memory_btn_2.setText(_translate("MainWindow", "Воспоминания"))
        self.settings_btn_2.setText(_translate("MainWindow", "Настройки"))
        self.exit_btn_2.setText(_translate("MainWindow", "Выход"))
        self.label_2.setText(_translate("MainWindow", "Главная страница"))
        self.output_note.setPlainText(_translate("MainWindow", "Вылет в 12:00"))
        self.input_note.setPlaceholderText(_translate("MainWindow", "Напишите напоминание/заметку здесь"))
        self.make_note_btn.setText(_translate("MainWindow", "Создать заметку"))
        self.memory_btn.setText(_translate("MainWindow", "Запечатлите свои воспоминания!"))
        self.label_5.setText(_translate("MainWindow", "Воспоминания"))
        self.label_6.setText(_translate("MainWindow", "Настройки"))
