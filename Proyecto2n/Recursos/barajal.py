import sys
import random
from Proyecto2n import mainqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from Proyecto2n.Recursos import barajalpie

class Barajal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("barajal.ui", self)
        try:
            self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="estadistica")
            self.cursor = self.conn.cursor()
        except:
            print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")
        self.btnlanza.clicked.connect(self.lanzadado)
        self.btnautomatico.clicked.connect(self.automatico)
        self.btnhome.clicked.connect(self.home)
        self.btnreiniciarbd.clicked.connect(self.reinicio)
        self.btnestadisticas.clicked.connect(self.stats)
        self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                           self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
        self.i = 0

    def lanzadado(self):
        dado = random.randint(0, 9)
        self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/"+dado.__str__()+".png); border-style: none;")
        self.aparecidos[self.i].setStyleSheet(
            "background-image: url(Proyecto2n/Recursos/img/barc/"+dado.__str__()+"p.png); border-style: none;")
        self.i += 1

        self.guarda(dado)
        if (self.i == 16):
            self.i = 0

    def home(self):
        print("volvemos a la ventana principal")
        self.close()
        self.ventana = mainqt.Principal()
        self.ventana.show()

    def automatico(self):
        num, ok = QInputDialog.getInt(self, "Autolanzamientos", "¿Cuantas veces quieres que lo lance?", 0, 0, 100, 1)
        if ok:
            for i in range(num):
                self.lanzadado()

    def guarda(self, dado):
        try:
            if (dado > 7):
                dado += 2
            self.cursor.execute("insert into cartacorta values( %s, DEFAULT)", (dado))
            print(" * Se ha insertado la carta con valor ", dado, " de oros satisfactoriamente * ")
            self.conn.commit()
        except:
            print(
                "Las estadísticas generales continuan temporalmente deshabilitadas, por favor, ponga en marcha el servidor MySql")

    def stats(self):
        print("Mostramos estadísticas sobre las cartas de toda la baraja Española")
        barajalpie.queso()

    def reinicio(self):
        try:
            self.cursor.execute("truncate table cartacorta;")
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/enves.png); border-style: none;")
            self.i = 0
            for numero in self.aparecidos:
                numero.setStyleSheet(
                    "background-image: url(Proyecto2n/Recursos/img/moneda/iniciop.png);border-style: none; background-repeat: no-repeat;")
            print("Las estadísticas se han reiniciado satisfactoriamente")
        except:
            print("No hay datos que reiniciar")