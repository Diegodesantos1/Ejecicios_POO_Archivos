import csv
class Calificaciones_estudiantes:
    def __init__(self, alumnos, lista):
        self.alumnos = alumnos
        self.lista = lista
    def recibir_diccionario():
        lista = []
        with open('calificaciones.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                lista.append(row)
            print(lista)
Calificaciones_estudiantes.recibir_diccionario()