import os, os.path, sys

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
from ui_explorerWindow import Ui_ExplorerWindow

import resources


class MapExplorer(QMainWindow, Ui_ExplorerWindow):
    def __init__(self):
        QMainWindow.__init__(self)
#        self.setWindowTitle("Landmark Explorer")
#        self.resize(1200, 400)

        self.setupUi(self)

#def main():

app = QApplication(sys.argv)
QgsApplication.setPrefixPath('/usr', True)
QgsApplication.initQgis()

# app = QApplication(sys.argv)
window = MapExplorer()
window.show()
window.raise_()

app.exec_()
app.deleteLater()
QgsApplication.exitQgis()

#if __name__ == "__main__":
#  main()
