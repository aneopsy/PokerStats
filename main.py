import sys
import os
import configparser

from neoEval import Card, Evaluator, Deck
from neoPS import PokerStars

from PyQt5.QtCore import QThread

from UI.gui import Ui_MainWindow
from UI.titleBar import TitleBar
from neoOdds import NeoOdds

# Setting custom variables
desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")
try:
    app_root = os.path.dirname(os.path.abspath(__file__))
except NameError:
    import sys
    app_root = os.path.dirname(os.path.abspath(sys.argv[0]))

import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtCore import *


class LoopThread(QThread):

    notifyProgress = QtCore.pyqtSignal(int)
    notifyOddsFlop = QtCore.pyqtSignal(int)
    notifyOddsTurn = QtCore.pyqtSignal(int)
    notifyOddsRiver = QtCore.pyqtSignal(int)
    notifyEquityFlop = QtCore.pyqtSignal(int)
    notifyEquityTurn = QtCore.pyqtSignal(int)
    notifyEquityRiver = QtCore.pyqtSignal(int)

    def __init__(self, cal, gui):
        QThread.__init__(self)
        self.cal = cal
        self.gui = gui
        self.i = 0

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        while True:
            self.cal.get_poker_cards()
            self.cal.pokerstars.get_info()
            self.gui.ui.lcdNumberPlayer.display(self.cal.pokerstars.nbrPlayers)
            if self.cal.cards[0]:
                self.gui.ui.labelHandCard.setText(Card.print_pretty_cards(self.cal.cards[0]))
            if self.cal.cards[1]:
                self.gui.ui.labelBoardCard.setText(Card.print_pretty_cards(self.cal.cards[1]))
            if len(self.cal.cards[0]) >= 2:
                a, b, c = self.cal.odds(self.gui.ui.spinBox.value(), self.cal.pokerstars.nbrPlayers)
                if len(self.cal.cards[1]) <= 3:
                    self.notifyOddsFlop.emit(int(a))
                    self.notifyEquityFlop.emit(self.cal.equity(self.gui.ui.spinBox.value(), 3))
                else:
                    self.notifyOddsFlop.emit(0)
                    self.notifyEquityFlop.emit(0)
                if len(self.cal.cards[1]) <= 4:
                    self.notifyOddsTurn.emit(int(b))
                    self.notifyEquityTurn.emit(self.cal.equity(self.gui.ui.spinBox.value(), 4))
                else:
                    self.notifyOddsTurn.emit(0)
                    self.notifyEquityTurn.emit(0)
                self.notifyOddsRiver.emit(int(c))
                self.notifyEquityRiver.emit(self.cal.equity(self.gui.ui.spinBox.value(), 5))
#            if len(self.cal.cards[0]) == 2 and len(self.cal.cards[1]) >= 3:
#                a, b, c = self.cal.evaluate()
#                self.cal.calculate()
#                self.gui.ui.labelCombi.setText("Player 1 hand rank = %d (%s)\n" % (
#                self.cal.p_score, self.cal.eval.evaluator.class_to_string(self.cal.p_class)))
#                self.gui.ui.labelInfo.setText("Player 1 hand rank = %d (%s) %f" % (a, b, c))
            self.i += 1
            self.notifyProgress.emit(self.i % 100)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.FramelessWindowHint)
        self.m_titleBar = TitleBar(self, "PokerStats")
        self.m_content = QtWidgets.QWidget(self)
        self.size = []
        self.size.append(380)
        self.size.append(HEIGHT - 38)
        self.move((WIDTH - self.size[0]), 0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, self.size)
        self.ui.verticalLayoutTitle.addWidget(self.m_titleBar)
        path = os.path.join(app_root, 'UI', 'images', 'icon.png')
        self.setWindowIcon(QtGui.QIcon(path))
        self.set_connections()
        self.url_list = []
        self.complete_url_list = {}
        self.convert_list = []
        self.thread_pool = {}
        self.rowcount = 0
        self.show()
        self.cal = NeoOdds()
        self.loopthread = LoopThread(self.cal, self)
        self.buttonStart = False
        defaults = {'path': 'C:\\Users\\theis_p\\AppData\\Local\\PokerStars.FR\\PokerStars.log.0', 'result': '2000'}
        self.config = configparser.SafeConfigParser(defaults=defaults)
        self.loadIni()

        for i in range(200):
            self.ui.listWidgetHistory.addItem(str(i))

    def set_connections(self):
        self.ui.btnStart.clicked.connect(self.handleButton)
        self.ui.btnApply.clicked.connect(self.saveIni)
        self.ui.btnSrc.clicked.connect(self.set_destination)
        # self.ui.BatchAdd.clicked.connect(self.batch_file)
        # self.ui.BrowseConvertButton.clicked.connect(self.convert_file_browse)
        # self.ui.ConvertMultipleButton.clicked.connect(self.convert_button)
        # self.ui.BrowseConvertToButton.clicked.connect(self.browse_convert_destination)

    def set_destination(self):
        file_name = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file_name is not '':
            self.ui.lineEditSrc.setText(file_name)

    def handleButton(self):
        if not self.buttonStart:
            self.src = str(self.ui.lineEditSrc.text())
            self.ui.labelInfo.setText(self.src)
            self.cal.config(self.src)
            self.onThread()
            self.buttonStart = True
            self.ui.btnStart.setText("Stop")
        else:
            self.ui.labelInfo.setText("Stop...")
            self.loopthread.stop()
            self.ui.btnStart.setText("Start ")
            self.reset()
            self.buttonStart = False

    def onThread(self):
        self.loopthread = LoopThread(self.cal, self)
        self.loopthread.notifyProgress.connect(self.onProgress)
        self.loopthread.notifyOddsFlop.connect(self.onOddsFlop)
        self.loopthread.notifyOddsTurn.connect(self.onOddsTurn)
        self.loopthread.notifyOddsRiver.connect(self.onOddsRiver)
        self.loopthread.notifyEquityFlop.connect(self.onEquityFlop)
        self.loopthread.notifyEquityTurn.connect(self.onEquityTurn)
        self.loopthread.notifyEquityRiver.connect(self.onEquityRiver)
        self.loopthread.start()

    def onProgress(self, i):
        self.ui.progressBarLoop.setValue(i)

    def onOddsFlop(self, a):
        if a == 0:
            self.ui.progressBar_3.setEnabled(False)
        else:
            self.ui.progressBar_3.setEnabled(True)
        self.ui.progressBar_3.setValue(a)

    def onOddsTurn(self, a):
        if a == 0:
            self.ui.progressBar_4.setEnabled(False)
        else:
            self.ui.progressBar_4.setEnabled(True)
        self.ui.progressBar_4.setValue(a)

    def onOddsRiver(self, a):
        if a == 0:
            self.ui.progressBar_5.setEnabled(False)
        else:
            self.ui.progressBar_5.setEnabled(True)
        self.ui.progressBar_5.setValue(a)

    def onEquityFlop(self, a):
        if a == 0:
            self.ui.progressBar.setEnabled(False)
        else:
            self.ui.progressBar.setEnabled(True)
        self.ui.progressBar.setValue(a)

    def onEquityTurn(self, a):
        if a == 0:
            self.ui.progressBar_2.setEnabled(False)
        else:
            self.ui.progressBar_2.setEnabled(True)
        self.ui.progressBar_2.setValue(a)

    def onEquityRiver(self, a):
        if a == 0:
            self.ui.progressBar_6.setEnabled(False)
        else:
            self.ui.progressBar_3.setEnabled(True)
        self.ui.progressBar_6.setValue(a)

    def reset(self):
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_6.setValue(0)
        self.ui.progressBar_3.setValue(0)
        self.ui.progressBar_4.setValue(0)
        self.ui.progressBar_5.setValue(0)
        self.ui.labelBoardCard.setText('')
        self.ui.labelHandCard.setText('')
        self.ui.lcdNumberPlayer.display(0)
        self.cards = []

    def loadIni(self):
        self.config.read('pokerstats.ini')
        if not self.config.has_section('config'):
            self.config.add_section('config')
        self.ui.lineEditSrc.setText(self.config.get('config', 'path'))
        self.ui.spinBox.setValue(int(self.config.get('config', 'result')))

    def saveIni(self):
        self.config.set('config', 'path', str(self.ui.lineEditSrc.text()))
        self.config.set('config', 'result', str(self.ui.spinBox.value()))
        with open('pokerstats.ini', 'w') as configfile:
            self.config.write(configfile)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    WIDTH, HEIGHT = screen_rect.width(), screen_rect.height()
    box = MainWindow()
    box.show()
    sys.exit(app.exec_())
