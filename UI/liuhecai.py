# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liuhecai.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 1, 1161, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(31)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.time_date_label = QtWidgets.QLabel(self.layoutWidget)
        self.time_date_label.setText("")
        self.time_date_label.setObjectName("time_date_label")
        self.horizontalLayout_3.addWidget(self.time_date_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.commit = QtWidgets.QPushButton(self.layoutWidget)
        self.commit.setObjectName("commit")
        self.horizontalLayout_2.addWidget(self.commit)
        self.personnel = QtWidgets.QPushButton(self.layoutWidget)
        self.personnel.setObjectName("personnel")
        self.horizontalLayout_2.addWidget(self.personnel)
        self.number_edit = QtWidgets.QPushButton(self.layoutWidget)
        self.number_edit.setObjectName("number_edit")
        self.horizontalLayout_2.addWidget(self.number_edit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.analysis_report = QtWidgets.QPushButton(self.layoutWidget)
        self.analysis_report.setObjectName("analysis_report")
        self.horizontalLayout_3.addWidget(self.analysis_report)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 1164, 711))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clear = QtWidgets.QPushButton(self.layoutWidget1)
        self.clear.setObjectName("clear")
        self.horizontalLayout_5.addWidget(self.clear)
        self.table_commit = QtWidgets.QPushButton(self.layoutWidget1)
        self.table_commit.setObjectName("table_commit")
        self.horizontalLayout_5.addWidget(self.table_commit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.composite_single = QtWidgets.QPushButton(self.layoutWidget1)
        self.composite_single.setObjectName("composite_single")
        self.gridLayout.addWidget(self.composite_single, 2, 3, 1, 1)
        self.tail_large = QtWidgets.QPushButton(self.layoutWidget1)
        self.tail_large.setObjectName("tail_large")
        self.gridLayout.addWidget(self.tail_large, 3, 5, 1, 1)
        self.red_single = QtWidgets.QPushButton(self.layoutWidget1)
        self.red_single.setObjectName("red_single")
        self.gridLayout.addWidget(self.red_single, 0, 1, 1, 1)
        self.tiger = QtWidgets.QPushButton(self.layoutWidget1)
        self.tiger.setObjectName("tiger")
        self.gridLayout.addWidget(self.tiger, 0, 7, 1, 1)
        self.mouse = QtWidgets.QPushButton(self.layoutWidget1)
        self.mouse.setObjectName("mouse")
        self.gridLayout.addWidget(self.mouse, 0, 5, 1, 1)
        self.green = QtWidgets.QPushButton(self.layoutWidget1)
        self.green.setObjectName("green")
        self.gridLayout.addWidget(self.green, 1, 0, 1, 1)
        self.tail_minor = QtWidgets.QPushButton(self.layoutWidget1)
        self.tail_minor.setObjectName("tail_minor")
        self.gridLayout.addWidget(self.tail_minor, 3, 6, 1, 1)
        self.monkey = QtWidgets.QPushButton(self.layoutWidget1)
        self.monkey.setObjectName("monkey")
        self.gridLayout.addWidget(self.monkey, 2, 5, 1, 1)
        self.blue = QtWidgets.QPushButton(self.layoutWidget1)
        self.blue.setObjectName("blue")
        self.gridLayout.addWidget(self.blue, 2, 0, 1, 1)
        self.rabbit = QtWidgets.QPushButton(self.layoutWidget1)
        self.rabbit.setObjectName("rabbit")
        self.gridLayout.addWidget(self.rabbit, 0, 8, 1, 1)
        self.dog = QtWidgets.QPushButton(self.layoutWidget1)
        self.dog.setObjectName("dog")
        self.gridLayout.addWidget(self.dog, 2, 7, 1, 1)
        self.blue_single = QtWidgets.QPushButton(self.layoutWidget1)
        self.blue_single.setObjectName("blue_single")
        self.gridLayout.addWidget(self.blue_single, 2, 1, 1, 1)
        self.minor = QtWidgets.QPushButton(self.layoutWidget1)
        self.minor.setObjectName("minor")
        self.gridLayout.addWidget(self.minor, 1, 4, 1, 1)
        self.single = QtWidgets.QPushButton(self.layoutWidget1)
        self.single.setObjectName("single")
        self.gridLayout.addWidget(self.single, 0, 3, 1, 1)
        self.blue_even = QtWidgets.QPushButton(self.layoutWidget1)
        self.blue_even.setObjectName("blue_even")
        self.gridLayout.addWidget(self.blue_even, 2, 2, 1, 1)
        self.composite_single_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.composite_single_2.setObjectName("composite_single_2")
        self.gridLayout.addWidget(self.composite_single_2, 2, 4, 1, 1)
        self.soil = QtWidgets.QPushButton(self.layoutWidget1)
        self.soil.setObjectName("soil")
        self.gridLayout.addWidget(self.soil, 3, 4, 1, 1)
        self.pig = QtWidgets.QPushButton(self.layoutWidget1)
        self.pig.setObjectName("pig")
        self.gridLayout.addWidget(self.pig, 2, 8, 1, 1)
        self.snake = QtWidgets.QPushButton(self.layoutWidget1)
        self.snake.setObjectName("snake")
        self.gridLayout.addWidget(self.snake, 1, 6, 1, 1)
        self.even = QtWidgets.QPushButton(self.layoutWidget1)
        self.even.setObjectName("even")
        self.gridLayout.addWidget(self.even, 1, 3, 1, 1)
        self.green_even = QtWidgets.QPushButton(self.layoutWidget1)
        self.green_even.setObjectName("green_even")
        self.gridLayout.addWidget(self.green_even, 1, 2, 1, 1)
        self.fire = QtWidgets.QPushButton(self.layoutWidget1)
        self.fire.setObjectName("fire")
        self.gridLayout.addWidget(self.fire, 3, 3, 1, 1)
        self.green_single = QtWidgets.QPushButton(self.layoutWidget1)
        self.green_single.setObjectName("green_single")
        self.gridLayout.addWidget(self.green_single, 1, 1, 1, 1)
        self.wood = QtWidgets.QPushButton(self.layoutWidget1)
        self.wood.setObjectName("wood")
        self.gridLayout.addWidget(self.wood, 3, 1, 1, 1)
        self.red = QtWidgets.QPushButton(self.layoutWidget1)
        self.red.setObjectName("red")
        self.gridLayout.addWidget(self.red, 0, 0, 1, 1)
        self.chicken = QtWidgets.QPushButton(self.layoutWidget1)
        self.chicken.setObjectName("chicken")
        self.gridLayout.addWidget(self.chicken, 2, 6, 1, 1)
        self.red_even = QtWidgets.QPushButton(self.layoutWidget1)
        self.red_even.setObjectName("red_even")
        self.gridLayout.addWidget(self.red_even, 0, 2, 1, 1)
        self.bull = QtWidgets.QPushButton(self.layoutWidget1)
        self.bull.setObjectName("bull")
        self.gridLayout.addWidget(self.bull, 0, 6, 1, 1)
        self.gold = QtWidgets.QPushButton(self.layoutWidget1)
        self.gold.setObjectName("gold")
        self.gridLayout.addWidget(self.gold, 3, 0, 1, 1)
        self.horse = QtWidgets.QPushButton(self.layoutWidget1)
        self.horse.setObjectName("horse")
        self.gridLayout.addWidget(self.horse, 1, 7, 1, 1)
        self.dragon = QtWidgets.QPushButton(self.layoutWidget1)
        self.dragon.setObjectName("dragon")
        self.gridLayout.addWidget(self.dragon, 1, 5, 1, 1)
        self.large = QtWidgets.QPushButton(self.layoutWidget1)
        self.large.setObjectName("large")
        self.gridLayout.addWidget(self.large, 0, 4, 1, 1)
        self.water = QtWidgets.QPushButton(self.layoutWidget1)
        self.water.setObjectName("water")
        self.gridLayout.addWidget(self.water, 3, 2, 1, 1)
        self.goat = QtWidgets.QPushButton(self.layoutWidget1)
        self.goat.setObjectName("goat")
        self.gridLayout.addWidget(self.goat, 1, 8, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setMaximumSize(QtCore.QSize(80, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(500, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_4.addWidget(self.textEdit_3)
        self.commit_two = QtWidgets.QPushButton(self.layoutWidget1)
        self.commit_two.setMaximumSize(QtCore.QSize(50, 16777215))
        self.commit_two.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.commit_two.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commit_two.setObjectName("commit_two")
        self.horizontalLayout_4.addWidget(self.commit_two)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 15000000))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "类型"))
        self.comboBox.setItemText(0, _translate("MainWindow", "老澳门"))
        self.comboBox.setItemText(1, _translate("MainWindow", "香港"))
        self.label_2.setText(_translate("MainWindow", "日期时间"))
        self.commit.setText(_translate("MainWindow", "录单"))
        self.personnel.setText(_translate("MainWindow", "人员"))
        self.number_edit.setText(_translate("MainWindow", "号码编辑"))
        self.analysis_report.setText(_translate("MainWindow", "分析上报"))
        self.clear.setText(_translate("MainWindow", "清空"))
        self.table_commit.setText(_translate("MainWindow", "提交"))
        self.composite_single.setText(_translate("MainWindow", "合单"))
        self.tail_large.setText(_translate("MainWindow", "尾大"))
        self.red_single.setText(_translate("MainWindow", "红单"))
        self.tiger.setText(_translate("MainWindow", "虎"))
        self.mouse.setText(_translate("MainWindow", "鼠"))
        self.green.setText(_translate("MainWindow", "绿"))
        self.tail_minor.setText(_translate("MainWindow", "尾小"))
        self.monkey.setText(_translate("MainWindow", "猴"))
        self.blue.setText(_translate("MainWindow", "蓝"))
        self.rabbit.setText(_translate("MainWindow", "兔"))
        self.dog.setText(_translate("MainWindow", "狗"))
        self.blue_single.setText(_translate("MainWindow", "蓝单"))
        self.minor.setText(_translate("MainWindow", "小"))
        self.single.setText(_translate("MainWindow", "单"))
        self.blue_even.setText(_translate("MainWindow", "蓝双"))
        self.composite_single_2.setText(_translate("MainWindow", "合双"))
        self.soil.setText(_translate("MainWindow", "土"))
        self.pig.setText(_translate("MainWindow", "猪"))
        self.snake.setText(_translate("MainWindow", "蛇"))
        self.even.setText(_translate("MainWindow", "双"))
        self.green_even.setText(_translate("MainWindow", "绿双"))
        self.fire.setText(_translate("MainWindow", "火"))
        self.green_single.setText(_translate("MainWindow", "绿单"))
        self.wood.setText(_translate("MainWindow", "木"))
        self.red.setText(_translate("MainWindow", "红"))
        self.chicken.setText(_translate("MainWindow", "鸡"))
        self.red_even.setText(_translate("MainWindow", "红双"))
        self.bull.setText(_translate("MainWindow", "牛"))
        self.gold.setText(_translate("MainWindow", "金"))
        self.horse.setText(_translate("MainWindow", "马"))
        self.dragon.setText(_translate("MainWindow", "龙"))
        self.large.setText(_translate("MainWindow", "大"))
        self.water.setText(_translate("MainWindow", "水"))
        self.goat.setText(_translate("MainWindow", "羊"))
        self.label_3.setText(_translate("MainWindow", "单个录入"))
        self.commit_two.setText(_translate("MainWindow", "提交"))