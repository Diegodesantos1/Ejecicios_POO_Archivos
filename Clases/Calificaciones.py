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
            diccionario={}
            datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
            lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
            lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_ordinario1 = list(datos["Ordinario1"])
            lista_ordinario2 = list(datos["Ordinario2"]) ; lista_practicas = list(datos["Practicas"]) ; lista_ordinariopracticas = list(datos["OrdinarioPracticas"])
            for i in range (16):
                apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
                parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; ordinario1 = lista_ordinario1.pop(0)
                ordinario2 = lista_ordinario2.pop(0) ; practicas = lista_practicas.pop(0) ; ordinariopracticas = lista_ordinariopracticas.pop(0)
                diccionario[i]={"Apellido": apellido,"Nombre": nombre,"Asistencia": asistencia,"Parcial 1": parcial1,"Parcial 2": parcial2,"Ordinario 1": ordinario1,"Ordinario 2": ordinario2,"Practicas": practicas,"Ordinario Practicas": ordinariopracticas}
            print(diccionario)
            elegir_subejercicio()
        elif visualizar == 3:
            with open("calificaciones.csv", "r", encoding="utf-8") as f:
                reader=csv.reader(f, delimiter=";")
                lista_de_listas = list(reader)
                print(f"{lista_de_listas}\n")
                elegir_subejercicio()
        else:
            print(Fore.RED + "No válido")
            Calificaciones_estudiantes.recibir_datos()
    def nota_final():
        diccionario={}
        datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
        lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
        lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_ordinario1 = list(datos["Ordinario1"])
        lista_ordinario2 = list(datos["Ordinario2"]) ; lista_practicas = list(datos["Practicas"]) ; lista_ordinariopracticas = list(datos["OrdinarioPracticas"])
        for i in range (16):
            apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
            parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; ordinario1 = lista_ordinario1.pop(0)
            ordinario2 = lista_ordinario2.pop(0) ; practicas = lista_practicas.pop(0) ; ordinariopracticas = lista_ordinariopracticas.pop(0)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4)
            diccionario[i]={"Apellido": apellido,"Nombre": nombre,"Asistencia": asistencia,"Parcial 1": parcial1,"Parcial 2": parcial2,"Ordinario 1": ordinario1,"Ordinario 2": ordinario2,"Practicas": practicas,"Ordinario Practicas": ordinariopracticas, "Nota final": nota_final}
        print(f"\nLos datos añadida la nota final son : \n\n\n{diccionario}")
        elegir_subejercicio()
    def aprobado_suspenso():
        aprobados = [] ; suspensos = []
        datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
        lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
        lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_practicas = list(datos["Practicas"])
        for i in range (16):
            apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
            parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; practicas = lista_practicas.pop(0)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4)
            if asistencia >= "0.75" and nota_final >= 5 and practicas >= 4:
                alumno=f"{nombre} {apellido} ,{nota_final}"
                aprobados.append(alumno)
            else:
                alumno=f"{nombre} {apellido} , {nota_final}"
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