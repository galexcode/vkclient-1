from PyQt4 import QtWebKit, QtGui, QtCore

class Authorization(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)
        webview = QtWebKit.QWebView(self)
        webview.load(QtCore.QUrl('http://vk.com'))
        webview.setGeometry(100, 100, 100, 100)
        webview.show()
       