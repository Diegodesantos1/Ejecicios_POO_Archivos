import csv
import pandas as pd
from colorama import Fore, Style
import re
class Calificaciones_estudiantes:
    def __init__(self, lista_de_listas, tabla, diccionario):
        self.lista_de_listas = lista_de_listas
        self.tabla = tabla
        self.diccionario= diccionario
    def recibir_diccionario(): #APARTADO 1
        visualizar = int(input((Fore.GREEN +"¿Qué quieres visualizar?" + Fore.BLUE + "\n --> 1: Tabla de datos\n --> 2: Diccionario de datos\n --> 3: Lista de datos\n"))) ; print(Style.RESET_ALL, end="")
        if visualizar == 1:
            tabla = pd.read_csv('calificaciones.csv', on_bad_lines='skip', encoding = "UTF8", sep=";")
            print(f"{tabla}\n\n\n")
        elif visualizar == 2:
            diccionario = pd.read_csv('calificaciones.csv', on_bad_lines='skip', encoding = "UTF8", sep=';').to_dict()
            print(f"{diccionario}\n\n\n")
        elif visualizar == 3:
            with open('calificaciones.csv', 'r', encoding="utf-8") as f:
                reader=csv.reader(f, delimiter=';')
                lista_de_listas = list(reader)
                print(lista_de_listas)
        else:
            print(Fore.RED + "No válido")
            Calificaciones_estudiantes.recibir_diccionario()
    def nota_final(): #Apartado 2
        with open('calificaciones.csv', 'r', encoding="utf-8") as f:
                reader=csv.reader(f, delimiter=';')
                lista_de_listas = list(reader)
                print(lista_de_listas)
        n = 0
        for i in range (len(lista_de_listas)):
            n=+1
            lista_inicial=lista_de_listas.pop(n)

            parcial1= (lista_inicial.pop(3)) ; parcial2 = (lista_inicial.pop(3)) ; final = (lista_inicial.pop(5))
            float(parcial1) ; float(parcial2) ; float(final)
            nota_final = float(((parcial1 + parcial2) * 0.6) + (final * 0.4))
            lista_final = lista_inicial.append(nota_final)
            print(lista_final)
Calificaciones_estudiantes.nota_final()