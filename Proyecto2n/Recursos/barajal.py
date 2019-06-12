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
        dado = random.randint(1, 10)
        if (dado == 1):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/1.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/1p.png); border-style: none;")
            self.i += 1
        elif (dado == 2):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/2.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/2p.png); border-style: none;")
            self.i += 1
        elif (dado == 3):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/3.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/3p.png); border-style: none;")
            self.i += 1
        elif (dado == 4):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/4.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/4p.png); border-style: none;")
            self.i += 1
        elif (dado == 5):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/5.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/5p.png); border-style: none;")
            self.i += 1
        elif (dado == 6):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/6.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/6p.png); border-style: none;")
            self.i += 1
        elif (dado == 7):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/7.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/7p.png); border-style: none;")
            self.i += 1
        elif (dado == 8):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/10.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/10p.png); border-style: none;")
            self.i += 1
        elif (dado == 9):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/11.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/11p.png); border-style: none;")
            self.i += 1
        elif (dado == 10):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/12.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/12p.png); border-style: none;")
            self.i += 1
        else:
            print(dado)
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