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
###
        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.useImageToRender(False)
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapCanvas.show()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)
        self.centralWidget.setLayout(layout)


        self.actionShowBasemapLayer.setChecked(True)
        self.actionShowLandmarkLayer.setChecked(True)





    def loadMap(self):
       cur_dir = os.path.dirname(os.path.realpath(__file__))
       filename = os.path.join(cur_dir, "data",
                                "NE1_50M_SR",
                                "NE1_50M_SR.tif")
       self.basemap_layer = QgsRasterLayer(filename, "basemap")
       QgsMapLayerRegistry.instance().addMapLayer(self.basemap_layer)

       filename = os.path.join(cur_dir, "data",
                                "ne_10m_populated_places",
                                "ne_10m_populated_places.shp")
       self.landmark_layer = QgsVectorLayer(filename, "landmarks", "ogr")
       QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)

       self.showVisibleMapLayers()
       self.mapCanvas.setExtent(QgsRectangle(-127.7, 24.4, -79.3, 49.1))

    def showVisibleMapLayers(self):
       layers = []
       if self.actionShowLandmarkLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.landmark_layer))
       if self.actionShowBasemapLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.basemap_layer))
       self.mapCanvas.setLayerSet(layers)

##########
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




def main():

 app = QApplication(sys.argv)
 QgsApplication.setPrefixPath('/usr', True)
 QgsApplication.initQgis()

 window = MapExplorer()
 window.show()
 window.raise_()
 window.loadMap()

 app.exec_()
 app.deleteLater()
 QgsApplication.exitQgis()

if __name__ == "__main__":
  main()
