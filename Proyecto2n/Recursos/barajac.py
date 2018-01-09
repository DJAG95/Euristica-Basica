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
            self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="estadistica")
            self.cursor = self.conn.cursor()
        except:
            print("No hay conexión a la base de datos, temporalmente las estadísticas globales estarán desactivadas")

        self.aparecidos = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9,
                           self.pb10, self.pb11, self.pb12, self.pb13, self.pb14, self.pb15, self.pb16]
        self.i = 0

    def lanzadado(self):
        dado = random.randint(1, 40)
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
        elif (dado == 11):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/1c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/1cp.png); border-style: none;")
            self.i += 1
        elif (dado == 12):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/2c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/2cp.png); border-style: none;")
            self.i += 1
        elif (dado == 13):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/3c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/3cp.png); border-style: none;")
            self.i += 1
        elif (dado == 14):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/4c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/4cp.png); border-style: none;")
            self.i += 1
        elif (dado == 15):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/5c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/5cp.png); border-style: none;")
            self.i += 1
        elif (dado == 16):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/6c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/6cp.png); border-style: none;")
            self.i += 1
        elif (dado == 17):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/7c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/7cp.png); border-style: none;")
            self.i += 1
        elif (dado == 18):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/10c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/10cp.png); border-style: none;")
            self.i += 1
        elif (dado == 19):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/11c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/11cp.png); border-style: none;")
            self.i += 1
        elif (dado == 20):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/12c.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/12cp.png); border-style: none;")
            self.i += 1
        elif (dado == 21):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/1e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/1ep.png); border-style: none;")
            self.i += 1
        elif (dado == 22):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/2e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/2ep.png); border-style: none;")
            self.i += 1
        elif (dado == 23):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/3e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/3ep.png); border-style: none;")
            self.i += 1
        elif (dado == 24):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/4e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/4ep.png); border-style: none;")
            self.i += 1
        elif (dado == 25):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/5e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/5ep.png); border-style: none;")
            self.i += 1
        elif (dado == 26):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/6e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/6ep.png); border-style: none;")
            self.i += 1
        elif (dado == 27):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/7e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/7ep.png); border-style: none;")
            self.i += 1
        elif (dado == 28):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/10e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/10ep.png); border-style: none;")
            self.i += 1
        elif (dado == 29):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/11e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/11ep.png); border-style: none;")
            self.i += 1
        elif (dado == 30):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/12e.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/12ep.png); border-style: none;")
            self.i += 1
        elif (dado == 31):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/1b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/1bp.png); border-style: none;")
            self.i += 1
        elif (dado == 32):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/2b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/2bp.png); border-style: none;")
            self.i += 1
        elif (dado == 33):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/3b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/3bp.png); border-style: none;")
            self.i += 1
        elif (dado == 34):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/4b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/4bp.png); border-style: none;")
            self.i += 1
        elif (dado == 35):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/5b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/5bp.png); border-style: none;")
            self.i += 1
        elif (dado == 36):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/6b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/6bp.png); border-style: none;")
            self.i += 1
        elif (dado == 37):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/7b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/7bp.png); border-style: none;")
            self.i += 1
        elif (dado == 38):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/10b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/10bp.png); border-style: none;")
            self.i += 1
        elif (dado == 39):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/11b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/11bp.png); border-style: none;")
            self.i += 1
        elif (dado == 40):
            self.pbcarta.setStyleSheet("background-image: url(Proyecto2n/Recursos/img/barc/12b.png); border-style: none;")
            self.aparecidos[self.i].setStyleSheet(
                "background-image: url(Proyecto2n/Recursos/img/barc/12bp.png); border-style: none;")
            self.i += 1
        else:
            print(dado)
        self.guarda(dado)
        if (self.i == 16):
            self.i = 0

    def guarda(self, dado):
        try:
            if(dado < 11):
                if (dado > 7):
                    dado += 2
                self.cursor.execute("insert into cartalarga values( %s, 0,DEFAULT)", (dado))
                print(" * Se ha insertado la carta con valor ", dado, " de oros satisfactoriamente * ")
                self.conn.commit()
            elif(dado < 21):
                nuevodado = dado-10
                if(nuevodado > 7):
                    nuevodado +=2
                self.cursor.execute("insert into cartalarga values( %s, 1, DEFAULT)", (nuevodado))
                print(" * Se ha insertado la carta con valor ", nuevodado, " de copas satisfactoriamente * ")
                self.conn.commit()
            elif (dado < 31):
                nuevodado = dado - 20
                if (nuevodado > 7):
                    nuevodado += 2
                self.cursor.execute("insert into cartalarga values( %s, 2, DEFAULT)", (nuevodado))
                print(" * Se ha insertado la carta con valor ", nuevodado, " de espadas satisfactoriamente * ")
                self.conn.commit()
            elif (dado < 41):
                nuevodado = dado - 30
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


