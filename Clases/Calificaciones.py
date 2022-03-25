import csv
import pandas as pd
from colorama import Fore, Style
import re
class Calificaciones_estudiantes:
    def __init__(self, lista_de_listas, tabla, diccionario):
        self.lista_de_listas = lista_de_listas
        self.tabla = tabla
        self.diccionario= diccionario
    def recibir_datos(): #APARTADO 1
        visualizar = int(input((Fore.GREEN +"¿Qué quieres visualizar?" + Fore.BLUE + "\n --> 1: Tabla de datos\n --> 2: Diccionario de datos\n --> 3: Lista de datos\n"))) ; print(Style.RESET_ALL, end="")
        if visualizar == 1:
            tabla = pd.read_csv("calificaciones.csv", on_bad_lines="skip", encoding = "UTF8", sep=";")
            print(f"{tabla}\n")
            elegir_subejercicio()
        elif visualizar == 2:
            diccionario={} ; dic_apellidos={} ; dic_nombre = {}
            datos = pd.read_csv('calificaciones.csv', header=0 , sep =";")
            lista_apellidos = list(datos['Apellidos']) ; (datos["Nombre"])
            for i in range (16):
                apellido=lista_apellidos.pop(0)
                diccionario["Apellido"] = apellido
                diccionario["Nombre"] = nombre
                print(diccionario)

            elegir_subejercicio()
        elif visualizar == 3:
            with open('calificaciones.csv', 'r', encoding="utf-8") as f:
                reader=csv.reader(f, delimiter=';')
                lista_de_listas = list(reader)
                print(f"{lista_de_listas}\n")
                elegir_subejercicio()
        else:
            print(Fore.RED + "No válido")
            Calificaciones_estudiantes.recibir_datos()
    def nota_final(): #Apartado 2
        lista_de_listas = [["Anido Bonet", "David", "90%", "5.5", "2.75", "0", "5", "0", "0"],["Bueno Cerdeira", "Patricia", "95%", "9.5", "9", "0", "0", "6.25", "0"],["Casariego García", "Raúl", "98%", "4.25", "5.75", "0", "0", "4", "5"],["Curbelo Sánchez", "Jorge", "75%", "6.75", "4.25", "0", "0", "0", "6.5"],["Díaz Souto", "Sofía", "82%", "7", "6.5", "0", "0", "9", "0"],["García Perez", "Yaiza", "85%", "10", "8", "0", "0", "7.5", "0"],["Sánchez Jordán", "María", "92%", "8.75", "9", "0", "0", "6.5", "0"],["Lorenzo García", "Jaime", "100%", "9.75", "8.25", "0", "0", "7.5", "0"],["Martínez Lucas", "Cecilia", "86%", "7", "4", "0", "0", "6.25", "0"],["Mora Peñaloza", "Sandra", "70%", "5.25", "2", "0", "4", "6.5", "0"],["Morillo Escudero", "Ana", "100%", "9.5", "10", "0", "0", "8.75", "0"],["Muñoz Gómez", "Carolina", "94%", "7.75", "6.5", "0", "0", "4", "0"],["Ramirez de la Puente", "Raquel", "75%", "0", "1", "1", "2.75", "2.25", "3.25"],["Riego Pizarro", "Carlos", "75%", "4", "2.5", "5", "3.75", "0", "0"],["Rodríguez de Blas", "Ignacio", "80%", "8.25", "5.25", "0", "0", "6.5", "0"],["Moreno Angulo", "Antonio", "88%", "9", "6.75", "0", "0", "5.25", "0"]]
        n = 0
        while len(lista_de_listas) != 0:
            lista_inicial=lista_de_listas.pop(n)
            parcial1= (lista_inicial.pop(3)) ; parcial2 = (lista_inicial.pop(3)) ; practicas = (lista_inicial.pop(5))
            parcial1 = float(parcial1) ; parcial2 = float(parcial2) ; practicas = float(practicas)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4)
            lista_inicial.insert(3,parcial1) ; lista_inicial.insert(3,parcial2) ; lista_inicial.insert(5,practicas)
            nota_final =round(nota_final)
            lista_inicial.append(nota_final)
            print(lista_inicial)
        elegir_subejercicio()
    def aprobado_suspenso():
        lista_de_listas = [["Anido Bonet", "David", "0.9", "5.5", "2.75", "0", "5", "0", "0"],["Bueno Cerdeira", "Patricia", "0.95", "9.5", "9", "0", "0", "6.25", "0"],["Casariego García", "Raúl", "0.98", "4.25", "5.75", "0", "0", "4", "5"],["Curbelo Sánchez", "Jorge", "0.75", "6.75", "4.25", "0", "0", "0", "6.5"],["Díaz Souto", "Sofía", "0.82", "7", "6.5", "0", "0", "9", "0"],["García Perez", "Yaiza", "0.85", "10", "8", "0", "0", "7.5", "0"],["Sánchez Jordán", "María", "0.92", "8.75", "9", "0", "0", "6.5", "0"],["Lorenzo García", "Jaime", "1", "9.75", "8.25", "0", "0", "7.5", "0"],["Martínez Lucas", "Cecilia", "0.86", "7", "4", "0", "0", "6.25", "0"],["Mora Peñaloza", "Sandra", "0.7", "5.25", "2", "0", "4", "6.5", "0"],["Morillo Escudero", "Ana", "1", "9.5", "10", "0", "0", "8.75", "0"],["Muñoz Gómez", "Carolina", "0.94", "7.75", "6.5", "0", "0", "4", "0"],["Ramirez de la Puente", "Raquel", "0.75", "0", "1", "1", "2.75", "2.25", "3.25"],["Riego Pizarro", "Carlos", "0.75", "4", "2.5", "5", "3.75", "0", "0"],["Rodríguez de Blas", "Ignacio", "0.8", "8.25", "5.25", "0", "0", "6.5", "0"],["Moreno Angulo", "Antonio", "0.88", "9", "6.75", "0", "0", "5.25", "0"]]
        aprobados= []
        suspensos=[]
        while len(lista_de_listas) != 0:
            lista_inicial=lista_de_listas.pop(0)
            asistencia = (lista_inicial.pop(2)) ; parcial1= (lista_inicial.pop(2)) ; parcial2 = (lista_inicial.pop(2)) ; practicas = (lista_inicial.pop(4))
            parcial1 = float(parcial1) ; parcial2 = float(parcial2) ; practicas = float(practicas)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4)
            nota_final =round(nota_final)
            if asistencia >= "0.75" and nota_final >= 5 and practicas >= 4:
                nombre = lista_inicial.pop(1)
                apellidos = lista_inicial.pop(0)
                alumno=f"{nombre} {apellidos}"
                aprobados.append(alumno)
            else:
                nombre = lista_inicial.pop(1)
                apellidos = lista_inicial.pop(0)
                alumno=f"{nombre} {apellidos}"
                suspensos.append(alumno)
        print(f"\nLos alumnos que han aprobado son:\n")
        for x in aprobados:
            print(Fore.GREEN + x)
        print(Fore.WHITE + "\nLos alumnos que han suspendido son:\n")
        for x in suspensos:
            print(Fore.RED + x)
        elegir_subejercicio()


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n¿Qué enunciado quieres ejecutar?(1-3) o 4 para terminar el programa\n") ; print(Style.RESET_ALL, end="")
    enunciado=int(input())
    if enunciado == 1:
        Calificaciones_estudiantes.recibir_datos()
    elif enunciado == 2:
        Calificaciones_estudiantes.nota_final()
    elif enunciado == 3:
        Calificaciones_estudiantes.aprobado_suspenso()
    elif enunciado == 4:
        exit()
    else:
        elegir_subejercicio()
elegir_subejercicio()