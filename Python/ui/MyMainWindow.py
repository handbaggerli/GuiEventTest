# -*- coding: utf-8 -*-

from ui.Ui_MainWindow import Ui_MainWindow
from ui.MyDialogText import MyDialogText
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot


class MyMainWindow(Ui_MainWindow):
    """Hauptfenster der Applikation, ist eine Erweiterung des generierten Codes aus Ui_MainWindow.

    Mit dem Open Button kann ein Eingabefenster geöffnet werden, wo eine entsprechende Eingabe gemacht werden kann.
    Im Fenster Gui Event wird der eingebende Text angezeigt, welcher über einen Event des Subfensters gefeuert wird.
    Im Fenster Property Event wird der eingebende Text angezeigt, welcher über das Property im Worker Objekt verbunden ist.
    Dafür wird der Event aus dem Worker Objekt verwendet.

    Der Clear Button löscht den aktuellen Text.

    :param: Worker Objekt.
    """

    def __init__(self, worker):
        super().__init__()
        self._worker = worker

    def init_user_data(self):
        """Hier könnte eine zusätzliche Initalisierung kommen.

        """
        pass

    def connect_user_events(self):
        """Verbindet die entsprechenden Events mit den Funktionen.

        Der Event aus dem Worker Objekt wird hier ebenfalls angebunden. Nicht aber der Event aus dem Subfenster, dieses
        existiert im allgemeinen Kontext nicht.
        """
        self.pushButtonClear.clicked.connect(self.__clear)
        self.pushButtonOpen.clicked.connect(self.__open)
        self._worker.myTextHasChanged.connect(self.__propertyTextChanged)

    @pyqtSlot(name="__claer")
    def __clear(self):
        """Event Slot für den Clear Button.

        Setzt das Text Property auf einen leeren String und ruft die Aktualsierung des Fensters Gui Event auf.
        """
        self._worker.text = ""
        self.__guiValueChanged(text=self._worker.text)

    @pyqtSlot(name="__open")
    def __open(self):
        """Event Slot für den Open Button.

        Es wird der Eingabe Dialog geöffnet und den Event Slot für den Gui Event initialisert.

        """
        textDialog = QtWidgets.QDialog()
        textDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ui = MyDialogText(worker=self._worker)
        ui.setupUi(textDialog)
        ui.init_user_data()
        ui.init_user_events()
        ui.guiChangedValue.connect(self.__guiValueChanged)
        textDialog.exec_()

    @pyqtSlot(name="__guiValueChanged")
    def __guiValueChanged(self, text: str):
        """Gui Event Text Feld wird abgefüllt mit dem Wert welcher über den Übergabestring aus dem Event vom Subfenster geworfen wird.

        :param text: Text String aus dem Subfenster.
        """
        self.textEditGuiEvent.setHtml(text)

    @pyqtSlot(name="__propertyTextChanged")
    def __propertyTextChanged(self):
        """Property Event Text Feld wird abgefüllt mit dem Wert aus dem Property.

        Die Aktualisierung erfogt vom Emit Event aus dem Worker Objekt.
        """
        self.textEditPropertyEvent.setHtml(self._worker.text)
