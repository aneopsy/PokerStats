import sys
import os
import time

from neoEval import Card, Evaluator, Deck
from neoPS import PokerStars

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

from UI.gui import Ui_MainWindow
from neoOdds import NeoOdds
from GUI.BatchAddUrls import BatchAddDialogue
from GUI.LicenseDialog import LicenseDialogue
from GUI.AboutDialog import AboutDialog

# Setting custom variables
desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")
try:
    app_root = os.path.dirname(os.path.abspath(__file__))
except NameError:
    import sys
    app_root = os.path.dirname(os.path.abspath(sys.argv[0]))

class getPostsThread(QThread):

    def __init__(self, cal, gui):
        QThread.__init__(self)
        self.cal = cal
        self.gui = gui

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.cal.get_poker_cards()
            self.cal.pokerstars.get_info()
            self.gui.ui.labelPlayerNumber.setText("Player: " + str(self.cal.pokerstars.nbrPlayers))
            if self.cal.cards[0]:
                print('Hand: ')
                Card.print_pretty_cards(self.cal.cards[0])
            if self.cal.cards[1]:
                print(' Board: ')
                Card.print_pretty_cards(self.cal.cards[1])
            if len(self.cal.cards[0]) >= 2:
                a, b, c = self.cal.odds(1000, self.cal.pokerstars.nbrPlayers)
                self.gui.ui.progressBar.setValue(self.cal.equity(1000, 3))
                self.gui.ui.progressBar_2.setValue(self.cal.equity(1000, 4))
                self.gui.ui.progressBar_6.setValue(self.cal.equity(1000, 5))

                self.gui.ui.progressBar_3.setValue(int(a))
                self.gui.ui.progressBar_4.setValue(int(b))
                self.gui.ui.progressBar_5.setValue(int(c))
            if len(self.cal.cards[0]) == 2 and len(self.cal.cards[1]) >= 3:
                a, b, c = self.cal.evaluate()
                self.gui.ui.labelInfo.setText("Player 1 hand rank = %d (%s) %f" % (a, b, c))
            self.sleep(0.1)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        path = os.path.join(app_root, 'UI', 'images', 'icon.png')
        self.setWindowIcon(QtGui.QIcon(path))
        self.batch_dialog = BatchAddDialogue(self)
        self.ui.lineEditSrc.setText("C:\\Users\\theis_p\\AppData\\Local\\PokerStars.FR\\PokerStars.log.0")
        self.set_connections()
        self.url_list = []
        self.complete_url_list = {}
        self.convert_list = []
        self.thread_pool = {}
        self.rowcount = 0
        self.show()
        self.cal = NeoOdds()

    def set_connections(self):
        self.ui.btnStart.clicked.connect(self.handleButton)
        # self.ui.browse_btn.clicked.connect(self.set_destination)
        # self.ui.BatchAdd.clicked.connect(self.batch_file)
        # self.ui.BrowseConvertButton.clicked.connect(self.convert_file_browse)
        # self.ui.ConvertMultipleButton.clicked.connect(self.convert_button)
        # self.ui.BrowseConvertToButton.clicked.connect(self.browse_convert_destination)

    def handleButton(self):
        self.src = str(self.ui.lineEditSrc.text())
        self.ui.labelInfo.setText("Start on :" + self.src)
        self.cal.config(self.src)
        self.get_thread = getPostsThread(self.cal, self)
        self.get_thread.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
