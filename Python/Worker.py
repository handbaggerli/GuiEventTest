# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal


class Worker(QObject):
    """Woker steht für eine Klasse, welche die eigentiche Arbeit übernimmt.

    In diesem Fall besteht die Arbeit aus einem einzigen Property. Wird dieses verändert, gibt dieses eine Benachrichtigung
    (Event) weiter, an alle die es mitbekommen wollen.
    Das Objekt muss zwingend von QObject abgeleitet werden und auch mit dem entsprechenden Konstrutor initialisert werden,
    ansonsten wird der Event nicht korrekt weitergeben.

    Das Signal myTextHasChanged kann von allen die es mitbekommen wollen, abonniert werden.
    """

    myTextHasChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._text = ""

    @property
    def text(self) -> str:
        """Property (Get / Set) welches den aktuellen Text beinhaltet.

        Wird das Property verändert, wird ein entsprechender Event gesendet.

        :return: Aktueller Text als String.
        """
        return self._text

    @text.setter
    def text(self, val: str):
        self._text = val
        self.myTextHasChanged.emit()
