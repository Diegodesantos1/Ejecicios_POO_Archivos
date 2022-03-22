import csv
import pandas as pd
class Calificaciones_estudiantes:
    def __init__(self, lista):
        self.lista = lista
    def recibir_diccionario():
        diccionario = pd.read_csv('calificaciones.csv', on_bad_lines='skip', encoding = "UTF8")
        print(diccionario)

Calificaciones_estudiantes.recibir_diccionario()