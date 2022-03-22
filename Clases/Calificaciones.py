import csv
import pandas as pd
class Calificaciones_estudiantes:
    def __init__(self, lista_de_listas, tabla, diccionario):
        self.lista_de_listas = lista_de_listas
        self.tabla = tabla
        self.diccionario= diccionario
    def recibir_diccionario():
        tabla = pd.read_csv('calificaciones.csv', on_bad_lines='skip', encoding = "UTF8", sep=";")
        print(f"{tabla}\n\n\n")
        diccionario = pd.read_csv('calificaciones.csv', on_bad_lines='skip', encoding = "UTF8", sep=';').to_dict()
        print(f"{diccionario}\n\n\n")
        with open('calificaciones.csv', 'r', encoding="utf-8") as f:
            reader=csv.reader(f, delimiter=';')
            lista_de_listas = list(reader)
            print(lista_de_listas)

Calificaciones_estudiantes.recibir_diccionario()