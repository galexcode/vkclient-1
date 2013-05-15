#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from global_window import GlobalWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = GlobalWindow()
    window.show()
    sys.exit(app.exec_())