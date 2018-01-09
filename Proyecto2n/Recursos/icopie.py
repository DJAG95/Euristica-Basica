import pymysql
import matplotlib.pyplot as plt
import sys

class queso():
    def __init__(self):
        try:
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="estadistica")
            cursor = conn.cursor()

            labels = []
            sizes = []
            cursor.execute("SELECT numero, count(numero) FROM `dado20` group by numero")
            for numero, tnumero in cursor.fetchall():
                labels.append(numero)
                sizes.append(tnumero)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()

        except:
            print("No tengo datos suficientes para realizar un diagrama de queso")
