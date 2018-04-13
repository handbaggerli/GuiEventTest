# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitRepos\TestGuiEvents\GuiBuilder\TestGuiEvents\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 348)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEditGuiEvent = QtWidgets.QTextEdit(self.centralWidget)
        self.textEditGuiEvent.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditGuiEvent.setFont(font)
        self.textEditGuiEvent.setObjectName("textEditGuiEvent")
        self.verticalLayout_2.addWidget(self.textEditGuiEvent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEditPropertyEvent = QtWidgets.QTextEdit(self.centralWidget)
        self.textEditPropertyEvent.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.textEditPropertyEvent.setFont(font)
        self.textEditPropertyEvent.setObjectName("textEditPropertyEvent")
        self.verticalLayout.addWidget(self.textEditPropertyEvent)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout_2.addWidget(self.pushButtonOpen)
        self.pushButtonClear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gui Event Test"))
        self.label.setText(_translate("MainWindow", "Gui Event"))
        self.label_2.setText(_translate("MainWindow", "Property Event"))
        self.pushButtonOpen.setText(_translate("MainWindow", "Open"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

