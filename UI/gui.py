# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\theis_p\Desktop\neoPokerStars\resources\gui_qt-designer-beta.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 675)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #528BFF;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #21252B;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #8caef4);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #528BFF;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #528BFF*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #282C34, stop: 0.1 #282C34, stop: 1 #282C34);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #1B1D23;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #D7DAE0;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3C424E, stop: 1 #3A3F4B);\n"
"    border-width: 1px;\n"
"    border-color: #181A1F;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3E4451, stop: 1 #3A3F4B);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #528BFF;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid #528BFF;\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #528BFF;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"background-color: #21252B;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 0.5 #528BFF, stop: 1 #528BFF);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 0.5 #528BFF, stop: 1 #528BFF);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #528BFF, stop:0.5 #528BFF stop:1 #528BFF);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(resources/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #528BFF;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #528BFF;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #528BFF);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #528BFF,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #528BFF;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(resources/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutTitle = QtWidgets.QVBoxLayout()
        self.verticalLayoutTitle.setObjectName("verticalLayoutTitle")
        self.verticalLayout_2.addLayout(self.verticalLayoutTitle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setMaximumSize(QtCore.QSize(360, 100))
        self.labelLogo.setSizeIncrement(QtCore.QSize(0, 0))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout.addWidget(self.labelLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBoxInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInfo.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBoxInfo.setObjectName("groupBoxInfo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxInfo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelPlayerNumber = QtWidgets.QLabel(self.groupBoxInfo)
        self.labelPlayerNumber.setObjectName("labelPlayerNumber")
        self.gridLayout_4.addWidget(self.labelPlayerNumber, 2, 0, 1, 1)
        self.lcdNumberPlayer = QtWidgets.QLCDNumber(self.groupBoxInfo)
        self.lcdNumberPlayer.setDigitCount(2)
        self.lcdNumberPlayer.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberPlayer.setObjectName("lcdNumberPlayer")
        self.gridLayout_4.addWidget(self.lcdNumberPlayer, 2, 1, 1, 1)
        self.labelHandCard = QtWidgets.QLabel(self.groupBoxInfo)
        self.labelHandCard.setText("")
        self.labelHandCard.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHandCard.setObjectName("labelHandCard")
        self.gridLayout_4.addWidget(self.labelHandCard, 0, 0, 1, 1)
        self.labelBoardCard = QtWidgets.QLabel(self.groupBoxInfo)
        self.labelBoardCard.setText("")
        self.labelBoardCard.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBoardCard.setObjectName("labelBoardCard")
        self.gridLayout_4.addWidget(self.labelBoardCard, 0, 1, 1, 1)
        self.labelCombi = QtWidgets.QLabel(self.groupBoxInfo)
        self.labelCombi.setText("")
        self.labelCombi.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCombi.setObjectName("labelCombi")
        self.gridLayout_4.addWidget(self.labelCombi, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBoxInfo)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 3px solid #FFFFFF;\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
"     background: white;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     alignment: center;\n"
" }")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.StatsTab = QtWidgets.QWidget()
        self.StatsTab.setObjectName("StatsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.StatsTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBoxEquity = QtWidgets.QGroupBox(self.StatsTab)
        self.groupBoxEquity.setObjectName("groupBoxEquity")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBoxEquity)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelEquityFlop = QtWidgets.QLabel(self.groupBoxEquity)
        self.labelEquityFlop.setObjectName("labelEquityFlop")
        self.gridLayout_2.addWidget(self.labelEquityFlop, 0, 0, 1, 1)
        self.labelEquityTurn = QtWidgets.QLabel(self.groupBoxEquity)
        self.labelEquityTurn.setObjectName("labelEquityTurn")
        self.gridLayout_2.addWidget(self.labelEquityTurn, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBoxEquity)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 0, 1, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBoxEquity)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_2.addWidget(self.progressBar_2, 1, 1, 1, 1)
        self.labelEquityRiver = QtWidgets.QLabel(self.groupBoxEquity)
        self.labelEquityRiver.setObjectName("labelEquityRiver")
        self.gridLayout_2.addWidget(self.labelEquityRiver, 2, 0, 1, 1)
        self.progressBar_6 = QtWidgets.QProgressBar(self.groupBoxEquity)
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.gridLayout_2.addWidget(self.progressBar_6, 2, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBoxEquity)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.groupBoxOdds = QtWidgets.QGroupBox(self.StatsTab)
        self.groupBoxOdds.setObjectName("groupBoxOdds")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBoxOdds)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelOddsRiver = QtWidgets.QLabel(self.groupBoxOdds)
        self.labelOddsRiver.setObjectName("labelOddsRiver")
        self.gridLayout_3.addWidget(self.labelOddsRiver, 2, 0, 1, 1)
        self.labelOddsFlop = QtWidgets.QLabel(self.groupBoxOdds)
        self.labelOddsFlop.setObjectName("labelOddsFlop")
        self.gridLayout_3.addWidget(self.labelOddsFlop, 0, 0, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBoxOdds)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_3.addWidget(self.progressBar_3, 0, 2, 1, 1)
        self.labelOddsTurn = QtWidgets.QLabel(self.groupBoxOdds)
        self.labelOddsTurn.setObjectName("labelOddsTurn")
        self.gridLayout_3.addWidget(self.labelOddsTurn, 1, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBoxOdds)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_3.addWidget(self.progressBar_4, 1, 2, 1, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBoxOdds)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout_3.addWidget(self.progressBar_5, 2, 2, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout_4.addWidget(self.groupBoxOdds)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.progressBarLoop = QtWidgets.QProgressBar(self.StatsTab)
        self.progressBarLoop.setProperty("value", 0)
        self.progressBarLoop.setInvertedAppearance(False)
        self.progressBarLoop.setObjectName("progressBarLoop")
        self.verticalLayout_4.addWidget(self.progressBarLoop)
        self.labelInfo = QtWidgets.QLabel(self.StatsTab)
        self.labelInfo.setMaximumSize(QtCore.QSize(395, 16777215))
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout_4.addWidget(self.labelInfo)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.btnStart = QtWidgets.QPushButton(self.StatsTab)
        self.btnStart.setMinimumSize(QtCore.QSize(82, 28))
        self.btnStart.setStyleSheet("")
        self.btnStart.setDefault(True)
        self.btnStart.setFlat(False)
        self.btnStart.setObjectName("btnStart")
        self.verticalLayout_4.addWidget(self.btnStart)
        self.tabWidget.addTab(self.StatsTab, "")
        self.ConfigTab = QtWidgets.QWidget()
        self.ConfigTab.setObjectName("ConfigTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.ConfigTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem7)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.labelSrc = QtWidgets.QLabel(self.ConfigTab)
        self.labelSrc.setObjectName("labelSrc")
        self.gridLayout.addWidget(self.labelSrc, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditSrc = QtWidgets.QLineEdit(self.ConfigTab)
        self.lineEditSrc.setObjectName("lineEditSrc")
        self.horizontalLayout_5.addWidget(self.lineEditSrc)
        self.btnSrc = QtWidgets.QPushButton(self.ConfigTab)
        self.btnSrc.setObjectName("btnSrc")
        self.horizontalLayout_5.addWidget(self.btnSrc)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.ConfigTab)
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(50000)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.ConfigTab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem8)
        self.btnApply = QtWidgets.QPushButton(self.ConfigTab)
        self.btnApply.setMinimumSize(QtCore.QSize(0, 28))
        self.btnApply.setAutoDefault(False)
        self.btnApply.setObjectName("btnApply")
        self.verticalLayout_11.addWidget(self.btnApply)
        self.tabWidget.addTab(self.ConfigTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poker Stats v0.1b"))
        self.groupBoxInfo.setTitle(_translate("MainWindow", "information"))
        self.labelPlayerNumber.setText(_translate("MainWindow", "Player:"))
        self.groupBoxEquity.setTitle(_translate("MainWindow", "Equity Calculator"))
        self.labelEquityFlop.setText(_translate("MainWindow", "Flop:"))
        self.labelEquityTurn.setText(_translate("MainWindow", "Turn:"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p%"))
        self.labelEquityRiver.setText(_translate("MainWindow", "River:"))
        self.groupBoxOdds.setTitle(_translate("MainWindow", "Odds Calculator"))
        self.labelOddsRiver.setText(_translate("MainWindow", "River:"))
        self.labelOddsFlop.setText(_translate("MainWindow", "Flop:"))
        self.labelOddsTurn.setText(_translate("MainWindow", "Turn:"))
        self.labelInfo.setText(_translate("MainWindow", "info"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StatsTab), _translate("MainWindow", "Stats"))
        self.labelSrc.setText(_translate("MainWindow", "Select a file:"))
        self.btnSrc.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Generation"))
        self.btnApply.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConfigTab), _translate("MainWindow", "Config"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "About"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

from .resource_rc import *
