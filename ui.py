#! /usr/bin/env python

import sys
from PyQt4 import QtGui, uic

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("gui.ui")
window.show()

sys.exit(app.exec_())