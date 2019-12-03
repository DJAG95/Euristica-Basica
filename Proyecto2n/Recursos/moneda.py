import sys
import random
from Proyecto2n import mainqt
from Proyecto2n.Recursos import monedapie, Constantes
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

class Moneda(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("moneda.ui", self)
        self.btnlanza.clicked.connect(self.lanzadado)
        self.btnhome.clicked.connect(self.home)
        try:
            self.conn = pymysql.connect(host=Constantes.host, port=Constantes.puerto, user=Constantes.user,
                                        passwd=Constantes.passwd, db=Constantes.db)
            self.cursor = self.conn.cursor()
        except:
            print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")
        self.btnautomatico.clicked.connect(self.automatico)
        self.btnestadisticas.clicked.connect(self.estadisticas)
        self.btnreiniciarbd.clicked.connect(self.reinicio)
        self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                           self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
        self.i = 0

    def lanzadado(self):
        moneda = random.randint(1, 2)
        if (moneda == 1):
            self.pbmoneda.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/cara.png); border-style: none;")
            self.ultimos(moneda)
        elif (moneda == 2):
            self.pbmoneda.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/cruz.png); border-style: none;")
            self.ultimos(moneda)
        else:
            print(moneda)
        self.guarda(moneda)

    def home(self):
        print("volvemos a la ventana principal")
        self.close()
        self.ventana = mainqt.Principal()
        self.ventana.show()

    def ultimos(self, moneda):

        if(moneda == 1):
            self.aparecidos[self.i].setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/carap.png); border-style: none; ")
            self.i +=1
        else:
            self.aparecidos[self.i].setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/cruzp.png); border-style: none;")
            self.i += 1
        if (self.i == 16):
            self.i = 0

    def automatico(self):
        num, ok = QInputDialog.getInt(self ,"Autolanzamientos","¿Cuantas veces quieres que lo lance?", 0,0,100,1)
        if ok:
            for i in range(num):
                self.lanzadado()

    def guarda(self, moneda):
        try:
            if(moneda == 1):
                nuevamoneda = "cara"
            else:
                nuevamoneda = "cruz"
            self.cursor.execute("insert into moneda values( %s, DEFAULT)", (nuevamoneda))
            print(" * Se ha insertado el valor " , nuevamoneda , " satisfactoriamente * ")
            self.conn.commit()

        except:
            print("Las estadísticas generales continuan temporalmente deshabilitadas, por favor, ponga en marcha el servidor MySql")

    def estadisticas(self):
        print("Mostramos estadísticas")
        monedapie.queso()

    def reinicio(self):
        try:
            self.cursor.execute("truncate table moneda;")
            self.pbmoneda.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/canto.png); border-style: none;")
            self.i = 0
            for numero in self.aparecidos:
                numero.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/moneda/iniciop.png);border-style: none; background-repeat: no-repeat;")
            print("Las estadísticas se han reiniciado satisfactoriamente")
        except:
            print("Hubo algún tipo de error")