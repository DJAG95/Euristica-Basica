import pymysql
import matplotlib.pyplot as plt
from Proyecto2n.Recursos import Constantes
import sys

class queso():
    def __init__(self):
        try:
            conn = pymysql.connect(host=Constantes.host, port=Constantes.puerto, user=Constantes.user,
                                   passwd=Constantes.passwd, db=Constantes.db)
            cursor = conn.cursor()

            labels = []
            sizes = []
            cursor.execute("SELECT palo, count(palo) FROM `cartalarga` group by palo")
            for palo, tpalo in cursor.fetchall():
                if(palo ==0):
                    labels.append("Oro")
                elif(palo == 1):
                    labels.append("Copa")
                elif(palo == 2):
                    labels.append("Espada")
                else:
                    labels.append("Bastos")
                sizes.append(tpalo)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()

        except:
            print("Error de conexión con la BD")
