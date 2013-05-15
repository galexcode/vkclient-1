from PyQt4 import *
from authorization import Authorization

class ListItem(QtGui.QListView):
    def __init__(self, parent=None):
        QtGui.QListView.__init__(self, parent)
        self.scroll(0, 100)

class UserItem(QtGui.QVBoxLayout):
    def __init__(self, parent=None):
        QtGui.QVBoxLayout.__init__(self, parent)