import sys
import random
from Proyecto2n import mainqt
from Proyecto2n.Recursos import dodepie, Constantes
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

class Dodecaedro(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("dodecaedro.ui", self)
        try:
            self.conn = pymysql.connect(host=Constantes.host, port=Constantes.puerto, user=Constantes.user,
                                        passwd=Constantes.passwd, db=Constantes.db)
            self.cursor = self.conn.cursor()
        except:
            print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")
        self.btnlanza.clicked.connect(self.lanzadado)
        self.btnhome.clicked.connect(self.home)
        self.btnautomatico.clicked.connect(self.automatico)
        self.btnestadisticas.clicked.connect(self.estadisticas)
        self.btnreiniciarbd.clicked.connect(self.reinicio)
        self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                           self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
        self.i = 0

    def lanzadado(self):
        dadeCaedro = random.randint(1, 12)
        self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/"+dadeCaedro.__str__()+".png);  border-style: none;")
        self.aparecidos[self.i].setStyleSheet(
            "background-image: url(Proyecto2n/Recursos/img/dode/"+dadeCaedro.__str__()+"p.png); border-style: none;")
        self.i += 1

        self.guarda(dadeCaedro)
        if (self.i == 16):
            self.i = 0

    def home(self):
        print("volvemos a la ventana principal")
        self.close()
        self.ventana = mainqt.Principal()
        self.ventana.show()
    def automatico(self):
        num, ok = QInputDialog.getInt(self ,"Autolanzamientos","¿Cuantas veces quieres que lo lance?", 0,0,100,1)
        if ok:
            for i in range(num):
                self.lanzadado()

    def guarda(self, dadeCaedro):
        try:
            self.cursor.execute("insert into dado12 values( %s, DEFAULT)", (dadeCaedro))
            print(" * Se ha insertado el dodecaedro con valor ", dadeCaedro, " satisfactoriamente * ")
            self.conn.commit()
        except:
            print(
                "Las estadísticas generales continuan temporalmente deshabilitadas, por favor, ponga en marcha el servidor MySql")

    def estadisticas(self):
        print("Mostramos estadísticas")
        dodepie.queso()

    def reinicio(self):
        self.cursor.execute("truncate table dado12;")
        self.i = 0
        self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/plantilla.png); border-style: none;")
        for numero in self.aparecidos:
            numero.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/iniciop.png);border-style: none; background-repeat: no-repeat;")
        print("Las estadísticas se han reiniciado satisfactoriamente")