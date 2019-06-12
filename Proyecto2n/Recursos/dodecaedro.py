import sys
import random
from Proyecto2n import mainqt
from Proyecto2n.Recursos import dodepie
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

class Dodecaedro(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("dodecaedro.ui", self)
        try:
            self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="estadistica")
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
        dado = random.randint(1, 12)
        if (dado == 1):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/1.png);  border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/1p.png); border-style: none;")
            self.i += 1
        elif (dado == 2):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/2.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/2p.png); border-style: none;")
            self.i += 1
        elif (dado == 3):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/3.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/3p.png); border-style: none;")
            self.i += 1
        elif (dado == 4):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/4.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/4p.png); border-style: none;")
            self.i += 1
        elif (dado == 5):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/5.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/5p.png); border-style: none;")
            self.i += 1
        elif (dado == 6):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/6.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/6p.png); border-style: none;")
            self.i += 1
        elif (dado == 7):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/7.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/7p.png); border-style: none;")
            self.i += 1
        elif (dado == 8):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/8.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/8p.png); border-style: none;")
            self.i += 1
        elif (dado == 9):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/9.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/9p.png); border-style: none;")
            self.i += 1
        elif (dado == 10):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/10.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/10p.png); border-style: none;")
            self.i += 1
        elif (dado == 11):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/11.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/11p.png); border-style: none;")
            self.i += 1
        elif (dado == 12):
            self.pbdode.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/dode/12.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/dode/12p.png); border-style: none;")
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
        num, ok = QInputDialog.getInt(self ,"Autolanzamientos","¿Cuantas veces quieres que lo lance?", 0,0,100,1)
        if ok:
            for i in range(num):
                self.lanzadado()

    def guarda(self, dado):
        try:
            self.cursor.execute("insert into dado12 values( %s, DEFAULT)", (dado))
            print(" * Se ha insertado el dodecaedro con valor ", dado, " satisfactoriamente * ")
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