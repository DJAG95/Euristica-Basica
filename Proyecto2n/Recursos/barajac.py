import sys
import random
from Proyecto2n.Recursos import barajacpie,barajacpiepalo
from Proyecto2n import mainqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

class Barajac(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("barajac.ui", self)
        self.btnlanza.clicked.connect(self.lanzadado)
        self.btnhome.clicked.connect(self.home)
        self.btnautomatico.clicked.connect(self.automatico)
        self.btnreiniciarbd.clicked.connect(self.reinicio)
        self.btnestadisticas.clicked.connect(self.stats)
        self.btnestadisticaspalo.clicked.connect(self.statspalo)


        try:
            self.conn = pymysql.connect(host="localhost", port=8889, user="root", passwd="", db="estadistica")
            self.cursor = self.conn.cursor()
        except:
            print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")

        self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                           self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
        self.i = 0

    def lanzadado(self):
        carta = random.randint(0, 39)
        self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/"+carta.__str__()+".png); border-style: none;")
        self.aparecidos[self.i].setStyleSheet(
            "background-image: url(Proyecto2n/Recursos/img/barc/"+carta.__str__()+"p.png); border-style: none;")
        self.i += 1

        self.guarda(carta)
        if (self.i == 16):
            self.i = 0

    def guarda(self, carta):
        try:
            if(carta < 10):
                self.cursor.execute("insert into cartalarga values( %s, 0,DEFAULT)", (carta))
                print(" * Se ha insertado la carta con valor ", carta, " de oros satisfactoriamente * ")
            elif(carta < 20):
                nuevodado = carta-10
                self.cursor.execute("insert into cartalarga values( %s, 1, DEFAULT)", (nuevodado))
                print(" * Se ha insertado la carta con valor ", nuevodado, " de copas satisfactoriamente * ")
            elif (carta < 30):
                nuevodado = carta - 20
                self.cursor.execute("insert into cartalarga values( %s, 2, DEFAULT)", (nuevodado))
                print(" * Se ha insertado la carta con valor ", nuevodado, " de espadas satisfactoriamente * ")
            elif (carta < 40):
                nuevodado = carta - 30
                if (nuevodado > 7):
                    nuevodado += 2
                self.cursor.execute("insert into cartalarga values( %s, 3, DEFAULT)", (nuevodado))
                print(" * Se ha insertado la carta con valor ", nuevodado, " de bastos satisfactoriamente * ")
            self.conn.commit()

        except:
            print("Las estadísticas generales continuan temporalmente deshabilitadas, por favor, ponga en marcha el servidor MySql")

    def home(self):
        print("volvemos a la ventana principal")
        self.close()
        self.ventana = mainqt.Principal()
        self.ventana.show()


    def statspalo(self):
        print("Mostramos estadísticas sobre los palos de la baraja de cartas Española")
        barajacpiepalo.queso()


    def stats(self):
        print("Mostramos estadísticas sobre las cartas de toda la baraja Española")
        barajacpie.queso()

    def reinicio(self):
        try:
            self.cursor.execute("truncate table cartalarga;")
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/enves.png); border-style: none;")
            self.i = 0
            for numero in self.aparecidos:
                numero.setStyleSheet(
                    "background-image: url(Proyecto2n/Recursos/img/moneda/iniciop.png);border-style: none; background-repeat: no-repeat;")
            print("Las estadísticas se han reiniciado satisfactoriamente")
        except:
            print("No hay datos que reiniciar")



    def automatico(self):
        num, ok = QInputDialog.getInt(self ,"Autolanzamientos","¿Cuantas veces quieres que lo lance?", 0,0,100,1)
        if ok:
            for i in range(num):
                self.lanzadado()


