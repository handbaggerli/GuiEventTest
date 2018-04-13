# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitRepos\TestGuiEvents\GuiBuilder\TestGuiEvents\dialogtext.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogText(QtWidgets.QDialog): ### Ableitung von object auf QtWidgets.QDialog manuell angepasst.
    def setupUi(self, DialogText):
        DialogText.setObjectName("DialogText")
        DialogText.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogText)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(DialogText)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogText)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogText)
        self.buttonBox.accepted.connect(DialogText.accept)
        self.buttonBox.rejected.connect(DialogText.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogText)

    def retranslateUi(self, DialogText):
        _translate = QtCore.QCoreApplication.translate
        DialogText.setWindowTitle(_translate("DialogText", "Text Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogText = QtWidgets.QDialog()
    ui = Ui_DialogText()
    ui.setupUi(DialogText)
    DialogText.show()
    sys.exit(app.exec_())

