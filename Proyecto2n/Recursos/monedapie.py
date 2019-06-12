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
            cursor.execute("SELECT lado, count(lado) FROM `moneda` group by lado")
            for lado, tlado in cursor.fetchall():
                labels.append(lado)
                sizes.append(tlado)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()

        except:
            print("No tengo datos suficientes para realizar un diagrama de queso")
