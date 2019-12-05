import threading
from Proyecto2n import mainqt
from Proyecto2n.Recursos import cubopie, Constantes
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
import random
import sys


class Cubo(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            uic.loadUi("cubo.ui", self)
            self.btnlanza.clicked.connect(self.lanzadado)
            self.btnhome.clicked.connect(self.home)
            try:
                self.conn = pymysql.connect(host=Constantes.host, port=Constantes.puerto, user=Constantes.user, passwd=Constantes.passwd, db=Constantes.db)
                self.cursor = self.conn.cursor()
            except:
                print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")
            self.btnautomatico.clicked.connect(self.automatico)
            self.btnestadisticas.clicked.connect(self.estadisticas)
            self.btnreiniciarbd.clicked.connect(self.reinicio)
            self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                               self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
            self.i = 0
        except:
            print(sys.exc_info())

    def lanzadado(self):
        dado = random.randint(1,6)
        self.pbdado.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/cubo/"+dado.__str__()+".png); border-style: none;")
        self.aparecidos[self.i].setStyleSheet("background-image: url(Proyecto2n/Recursos/img/cubo/"+dado.__str__()+"p.png); border-style: none;")
        self.i += 1
        self.guarda(dado)
        if (self.i == 16):
            self.i = 0



    def guarda(self, dado):
        try:
            self.cursor.execute("insert into dado6 values( %s, DEFAULT)", (dado))
            print(" * Se ha insertado el cubo con valor ", dado, " satisfactoriamente * ")
            self.conn.commit()
        except:
            print(
                "Las estadísticas generales continuan temporalmente deshabilitadas, por favor, ponga en marcha el servidor MySql")

    def home(self):
        print("volvemos a la ventana principal")
        self.close()
        self.ventana = mainqt.Principal()
        self.ventana.show()

    def estadisticas(self):
        print("Mostramos estadísticas")
        cubopie.queso()

    def reinicio(self):
        try:
            self.cursor.execute("truncate table dado6;")
            self.i = 0
            self.pbdado.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/cubo/plantilla.png); border-style: none;")
            for numero in self.aparecidos:
                numero.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/iniciop.png);border-style: none; background-repeat: no-repeat;")
            print("Las estadísticas se han reiniciado satisfactoriamente")
        except:
            print("No hay datos que reiniciar")



    def automatico(self):
        num, ok = QInputDialog.getInt(self ,"Autolanzamientos","¿Cuantas veces quieres que lo lance?", 0,0,100,1)
        if ok:
            for i in range(num):
                self.lanzadado()




