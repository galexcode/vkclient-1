from PyQt4 import *
from top_frame import TopFrame, UserFrame
from authorization import Authorization

class GlobalWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(400, 200, 400, 600)
        self.setWindowTitle('VkClient')
        self.setWhatsThis(QtCore.QString('hello'))
        self.setStyleSheet('background: #356AA0;')
        self.setFont(QtGui.QFont('Arial'))
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)
        self.layout = QtGui.QVBoxLayout()
        self.top_frame = TopFrame()
        self.top_frame.show()
        self.user_frame = UserFrame()
        self.authorization = Authorization(self.user_frame)
        self.authorization.show()
        self.user_frame.show()
        self.layout.addWidget(self.top_frame,1)
        self.layout.addWidget(self.user_frame, 2)
        self.setLayout(self.layout)