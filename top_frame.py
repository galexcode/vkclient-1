from PyQt4 import *
from user_objects import *
from authorization import Authorization

class TopFrame(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)
        self.setStyleSheet('background: #fff; border-radius: 10px;')
        
class UserFrame(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)
        self.setStyleSheet('background: #fff; border-radius: 10px;')
        self.setFrameRect(QtCore.QRect(400,400,400,400))
        self.setFrameShadow(self.Shadow())
        self.scroll(0, 100)
        self.item = UserItem()
        self.setLayout(self.item)