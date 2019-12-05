import sys
from Proyecto2n.Recursos import cubo
from Proyecto2n.Recursos import dodecaedro
from Proyecto2n.Recursos import icosaedro
from Proyecto2n.Recursos import moneda
from Proyecto2n.Recursos import barajac
from Proyecto2n.Recursos import barajal
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Principal(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            uic.loadUi("MainWindow.ui", self)
            self.btncubo.clicked.connect(self.cubo)
            self.btndodecaedro.clicked.connect(self.dodecaedro)
            self.btnicosaedro.clicked.connect(self.icosaedro)
            self.btnmoneda.clicked.connect(self.moneda)
            self.btnbarajaestandar.clicked.connect(self.barajaestandar)
            self.btnbarajaextendida.clicked.connect(self.barajaextendida)
        except:
            print(sys.exc_info())


    def cubo(self):
        print("Entramos en la ventana cubo")
        self.close()
        self.ventana = cubo.Cubo()
        self.ventana.show()


    def dodecaedro(self):
        print("Entramos en la ventana dodecaedro")
        self.close()
        self.ventana = dodecaedro.Dodecaedro()
        self.ventana.show()

    def icosaedro(self):
        print("Entramos en la ventana icosaedro")
        self.close()
        self.ventana = icosaedro.Icosaedro()
        self.ventana.show()

    def moneda(self):
        print("Entramos en la ventana moneda")
        self.close()
        self.ventana = moneda.Moneda()
        self.ventana.show()

    def barajaestandar(self):
        print("Entramos en la ventana baraja Española")
        self.close()
        self.ventana = barajac.Barajac()
        self.ventana.show()

    def barajaextendida(self):
        print("Entramos en la ventana baraja de oro")
        self.close()
        self.ventana = barajal.Barajal()
        self.ventana.show()

    @staticmethod
    def ejecucion():
        app = QApplication(sys.argv)
        splashLogo = QPixmap('Proyecto2n/Recursos/splash/splash.png')
        splash = QSplashScreen(splashLogo, Qt.WindowStaysOnTopHint)
        splash.setMask(splashLogo.mask())
        splash.show()
        app.processEvents()
        print("Bienvenido a RGDE - Representación Gráfica de datos Estadísticos")
        print("R - Representación")
        print("G - Gráfica")
        print("D - Datos")
        print("E - Estadisticos")
        print("En consola se mostrarán datos relevantes de cara al programador, la experiencia del usuario final no se verá afectada por esta ausencia de información")
        vista = Principal()
        splash.finish(vista)
        vista.show()
        app.exec_()