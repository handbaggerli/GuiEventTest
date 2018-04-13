# -*- coding: utf-8 -*-

from ui.Ui_DialogText import Ui_DialogText
from Worker import Worker
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class MyDialogText(Ui_DialogText):
    """Subfenster welches die eigentliche Texteingabe entgegen nimmt, erweitert Ui_DialogText.

    Die Ableitung von Ui_DialogText, welche vom Generator her mit Typ (objekt) angegeben wird, muss zwingend angepasst werden
    auf einen Typ von (QObject) oder einem Typen der von diesem abgeleitet ist. Ansonsten wird das Signal nicht korrekt
    initialisiert.

    Das Signal guiChangeValue übergibt die aktuelle Texteingabe an alle weiter, die es mitbekommen wollen.

    :param: Worker Objekt um die Eingabe ins Property zu schreiben.
    """

    guiChangedValue = pyqtSignal(str)

    def __init__(self, worker: Worker):
        super().__init__()
        self._worker = worker

    def init_user_data(self):
        """Einmaliges Setzten des Wertes im Textfenster mit dem Wert aus dem Property.

        """
        self.textEdit.setHtml(self._worker.text)

    def init_user_events(self):
        """Eingabe Event initialisieren.

        """
        self.textEdit.textChanged.connect(self.__textChanged)

    @pyqtSlot(name="__textChanged")
    def __textChanged(self):
        """Synchronisieren des Wertes aus dem Eingabefenster mit dem Property und Senden des Wertes über das Signal guiChangeValue.

        """
        self._worker.text = self.textEdit.toHtml()
        self.guiChangedValue.emit(self.textEdit.toHtml())
