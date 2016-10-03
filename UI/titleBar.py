#########################################################
## customize Title bar
## dotpy.ir
## iraj.jelo@gmail.com
#########################################################
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint);
        css = """
        QWidget{
            Background: #282C34;
            color:white;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            Background-image:url('img/titlebar bg.png');
            font-size:12px;
            color: black;

        }
        QToolButton{
            Background:#AA2020;
            font-size:11px;
        }
        QToolButton:hover{
            Background: #AAAAAA;
            font-size:11px;
        }
        """
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css) 
        self.minimize=QtWidgets.QToolButton(self);
        self.minimize.setIcon(QtGui.QIcon('img/min.png'));
        self.minimize.setStyleSheet("""QToolButton{
            Background:#AAAA20;
            font-size:11px;
        }""")
        self.maximize=QtWidgets.QToolButton(self);
        self.maximize.setIcon(QtGui.QIcon('img/max.png'));
        self.maximize.setStyleSheet("""QToolButton{
            Background:#20AA20;
            font-size:11px;
        }""")
        close=QtWidgets.QToolButton(self);
        close.setIcon(QtGui.QIcon('img/close.png'));
        self.minimize.setMinimumHeight(10);
        close.setMinimumHeight(10);
        self.maximize.setMinimumHeight(10);
        label=QtWidgets.QLabel(self);
        label.setText("Window Title");
        self.setWindowTitle("Window Title");
        hbox=QtWidgets.QHBoxLayout(self);
        hbox.addWidget(label);
        hbox.addWidget(self.minimize);
        hbox.addWidget(self.maximize);
        hbox.addWidget(close);
        hbox.insertStretch(1,500);
        hbox.setSpacing(3);
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed);
        self.maxNormal=False;
        close.clicked.connect(self.close);
        self.minimize.clicked.connect(self.showSmall);
        self.maximize.clicked.connect(self.showMaxRestore);

    def showSmall(self):
        box.showMinimized();

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal();
            self.maxNormal= False;
            self.maximize.setIcon(QtGui.QIcon('img/max.png'));
        else:
            box.showMaximized();
            self.maxNormal=  True;
            self.maximize.setIcon(QtGui.QIcon('img/max2.png'));

    def close(self):
        box.close()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True; box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)


class Frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.m_mouse_down= False;
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
QToolTip
{
     border: 1px solid black;
     background-color: #528BFF;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #b1b1b1;
    background-color: #21252B;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #8caef4);
    color: #000000;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #528BFF;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434/*,
        stop:0.2 #343434,
        stop:0.1 #528BFF*/
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QWidget:disabled
{
    color: #404040;
    background-color: #323232;
}

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #282C34, stop: 0.1 #282C34, stop: 1 #282C34);
}

QWidget:focus
{
    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);*/
}

QLineEdit
{
    background-color: #1B1D23;
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 2;
}

QPushButton
{
    color: #D7DAE0;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3C424E, stop: 1 #3A3F4B);
    border-width: 1px;
    border-color: #181A1F;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3E4451, stop: 1 #3A3F4B);
}

QComboBox
{
    selection-background-color: #528BFF;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QComboBox:hover,QPushButton:hover
{
    border: 2px solid #528BFF;
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #528BFF;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid; /* just a single line */
     border-top-right-radius: 3px; /* same radius as the QComboBox */
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{
     image: url(:/down_arrow.png);
}

QGroupBox
{
background-color:#282C34;
}

QGroupBox:focus
{
border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
}

QTextEdit:focus
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
}

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 7px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 0.5 #528BFF, stop: 1 #528BFF);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 1 #528BFF);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #528BFF, stop: 1 #528BFF);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 7px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 0.5 #528BFF, stop: 1 #528BFF);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #528BFF, stop: 1 #528BFF);
      height: 14px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

QTextEdit
{
    background-color: #242424;
}

QPlainTextEdit
{
    background-color: #242424;
}

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
color: #414141;
}

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #528BFF, stop:0.5 #528BFF stop:1 #528BFF);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QToolBar::handle
{
     spacing: 3px; /* spacing between items in the tool bar */
     background: url(resources/images/handle.png);
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #528BFF;
    width: 2.15px;
    margin: 0.5px;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */


    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    /*border-top: 2px solid #528BFF;
    padding-bottom: 3px;*/
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #528BFF);
}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 6px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #528BFF,
        stop: 0.3 #323232
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #528BFF;
}

QCheckBox::indicator:checked
{
    image:url(resources/images/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}

        """
        self.setStyleSheet(css) 
        self.setWindowFlags(Qt.FramelessWindowHint);
        self.setMouseTracking(True);
        self.m_titleBar= TitleBar(self);
        self.m_content= QtWidgets.QWidget(self);
        vbox=QtWidgets.QVBoxLayout(self);
        vbox.addWidget(self.m_titleBar);

        layout=QtWidgets.QVBoxLayout(self);
        layout.addWidget(self.m_content);

        vbox.addLayout(layout);
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos();
        self.m_mouse_down = event.button()== Qt.LeftButton;

    def mouseMoveEvent(self,event):
        x=event.x();
        y=event.y();

    def mouseReleaseEvent(self,event):
        m_mouse_down=False;

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv);
    box = Frame()
    box.move(60,60);
    l=QtWidgets.QVBoxLayout(box.contentWidget());
    edit=QtWidgets.QLabel("""I would've did anything for you to show you how much I adored you
But it's over now, it's too late to save our loveJust promise me you'll think of me
Every time you look up in the sky and see a star 'cuz I'm  your star.""");
    l.addWidget(edit)
    groupBoxEquity = QtWidgets.QGroupBox()
    groupBoxEquity.setObjectName("groupBoxEquity")
    groupBoxEquity.setTitle("Stats")
    verticalLayout_8 = QtWidgets.QVBoxLayout(groupBoxEquity)
    verticalLayout_8.setObjectName("verticalLayout_8")
    gridLayout_2 = QtWidgets.QGridLayout()
    gridLayout_2.setObjectName("gridLayout_2")
    
    labelEquityFlop = QtWidgets.QLabel(groupBoxEquity)
    labelEquityFlop.setObjectName("labelEquityFlop")
    labelEquityFlop.setText("Flop: ")
    gridLayout_2.addWidget(labelEquityFlop, 0, 0, 1, 1)
    progressBar = QtWidgets.QProgressBar()
    progressBar.setProperty("value", 24)
    progressBar.setObjectName("progressBar")
    gridLayout_2.addWidget(progressBar, 0, 1, 1, 1)
    verticalLayout_8.addLayout(gridLayout_2)

    labelEquityTurn = QtWidgets.QLabel(groupBoxEquity)
    labelEquityTurn.setObjectName("labelEquityTurn")
    labelEquityTurn.setText("Turn: ")
    gridLayout_2.addWidget(labelEquityTurn, 1, 0, 1, 1)
    progressBar_2 = QtWidgets.QProgressBar(groupBoxEquity)
    progressBar_2.setProperty("value", 24)
    progressBar_2.setObjectName("progressBar_2")
    gridLayout_2.addWidget(progressBar_2, 1, 1, 1, 1)

    labelEquityRiver = QtWidgets.QLabel(groupBoxEquity)
    labelEquityRiver.setObjectName("labelEquityRiver")
    labelEquityRiver.setText("River: ")
    gridLayout_2.addWidget(labelEquityRiver, 2, 0, 1, 1)
    progressBar_6 = QtWidgets.QProgressBar(groupBoxEquity)
    progressBar_6.setProperty("value", 24)
    progressBar_6.setObjectName("progressBar_6")
    gridLayout_2.addWidget(progressBar_6, 2, 1, 1, 1)
    
    l.addWidget(groupBoxEquity)
    box.show()
    app.exec_()
