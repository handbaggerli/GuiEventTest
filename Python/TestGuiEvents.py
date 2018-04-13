# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from ui.MyMainWindow import MyMainWindow
from Worker import Worker

class TestGuiEvents:
    """Kleines Testprogramm welches die Kommunikation von Daten zwischen zwei verschiedenen Fenstern darstellt.

    Das Hauptfenster besteht aus zwei Bereichen, welche durch Events Synchron gehalten wird. Wobei die Daten einmal
    direkt von der Eingabe im Subfenster gefeuert und einmal über ein Property gelesen wird. Jede Eingabe sendet ein
    entsprechender Event.

    """

    def run(self):
        """Startet das Programm.

        """
        worker = Worker()
        app = QtWidgets.QApplication(sys.argv)
        win1 = QtWidgets.QMainWindow()
        ui1 = MyMainWindow(worker=worker)
        ui1.setupUi(win1)
        ui1.init_user_data()
        ui1.connect_user_events()
        win1.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    tge = TestGuiEvents()
    tge.run()
