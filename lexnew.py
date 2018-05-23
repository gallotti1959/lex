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

        self.setupUi(self)
#######################

        self.connect(self.actionQuit, SIGNAL("triggered()"),
                     qApp.quit)
        self.connect(self.actionShowBasemapLayer, SIGNAL("triggered()"),
                     self.showBasemapLayer)
        self.connect(self.actionShowLandmarkLayer, SIGNAL("triggered()"),
                     self.showLandmarkLayer)
        self.connect(self.actionZoomIn, SIGNAL("triggered()"),
                     self.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("triggered()"),
                     self.zoomOut)

        self.connect(self.actionPan, SIGNAL("triggered()"),
                     self.setPanMode)
        self.connect(self.actionExplore, SIGNAL("triggered()"),
                     self.setExploreMode)

    def showBasemapLayer(self):
#        self.showVisibleMapLayers()
     pass

    def showLandmarkLayer(self):
#        self.showVisibleMapLayers()
     pass

    def zoomIn(self):
#        self.mapCanvas.zoomIn()
     pass

    def zoomOut(self):
#        self.mapCanvas.zoomOut()
     pass

    def setPanMode(self):
     pass
#        self.actionPan.setChecked(True)
#        self.actionExplore.setChecked(False)
#        self.mapCanvas.setMapTool(self.panTool)


    def setExploreMode(self):
     pass
#        self.actionPan.setChecked(False)
#        self.actionExplore.setChecked(True)
#        self.mapCanvas.setMapTool(self.exploreTool)




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
