<h1 align="center">POO con archivos</h1>

*He usado la Programación Orientada a Objetos para resolver este ejercicio*

---

En este [repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Archivos) queda resuelto el ejercicios de archivos en Python. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de otros medios.

***

## Índice
1. [Ejercicio 1: Calificaciones  ](#id1)

***

## Ejercicio 1: Calificaciones<a name="id1"></a>

El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.


```python
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
            lista_diccionario = []
            datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
            lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
            lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_ordinario1 = list(datos["Ordinario1"])
            lista_ordinario2 = list(datos["Ordinario2"]) ; lista_practicas = list(datos["Practicas"]) ; lista_ordinariopracticas = list(datos["OrdinarioPracticas"])
            for i in range (16):
                apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
                parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; ordinario1 = lista_ordinario1.pop(0)
                ordinario2 = lista_ordinario2.pop(0) ; practicas = lista_practicas.pop(0) ; ordinariopracticas = lista_ordinariopracticas.pop(0)
                diccionario={"Apellido": apellido,"Nombre": nombre,"Asistencia": asistencia,"Parcial 1": parcial1,"Parcial 2": parcial2,"Ordinario 1": ordinario1,"Ordinario 2": ordinario2,"Practicas": practicas,"Ordinario Practicas": ordinariopracticas}
                lista_diccionario.append(diccionario)
            print(lista_diccionario)
            elegir_subejercicio()
        elif visualizar == 3:
            with open("calificaciones.csv", "r", encoding="utf-8") as f:
                reader=csv.reader(f, delimiter=";")
                lista_de_listas = list(reader)
                lista_de_listas.pop(0)
                print(f"{lista_de_listas}\n")
                elegir_subejercicio()
        else:
            print(Fore.RED + "No válido")
            Calificaciones_estudiantes.recibir_datos()
    def nota_final():
        diccionario={}
        lista_diccionario2 = []
        datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
        lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
        lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_ordinario1 = list(datos["Ordinario1"])
        lista_ordinario2 = list(datos["Ordinario2"]) ; lista_practicas = list(datos["Practicas"]) ; lista_ordinariopracticas = list(datos["OrdinarioPracticas"])
        for i in range (16):
            apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
            parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; ordinario1 = lista_ordinario1.pop(0)
            ordinario2 = lista_ordinario2.pop(0) ; practicas = lista_practicas.pop(0) ; ordinariopracticas = lista_ordinariopracticas.pop(0)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4) ; nota_final = round(nota_final, 2)
            diccionario={"Apellido": apellido,"Nombre": nombre,"Asistencia": asistencia,"Parcial 1": parcial1,"Parcial 2": parcial2,"Ordinario 1": ordinario1,"Ordinario 2": ordinario2,"Practicas": practicas,"Ordinario Practicas": ordinariopracticas, "Nota final": nota_final}
            lista_diccionario2.append(diccionario)
        print(f"\nLos datos añadida la nota final son : \n\n\n{lista_diccionario2}")
        elegir_subejercicio()
    def aprobado_suspenso():
        aprobados = [] ; suspensos = []
        datos = pd.read_csv("calificaciones.csv", header=0 , sep =";")
        lista_apellidos = list(datos["Apellidos"]) ; lista_nombre = list(datos["Nombre"]) ; lista_asistencia = list(datos["Asistencia"])
        lista_parcial1 = list(datos["Parcial1"]) ; lista_parcial2 = list(datos["Parcial2"]) ; lista_practicas = list(datos["Practicas"])
        for i in range (16):
            apellido=lista_apellidos.pop(0) ; nombre=lista_nombre.pop(0) ; asistencia = lista_asistencia.pop(0)
            parcial1=lista_parcial1.pop(0) ; parcial2=lista_parcial2.pop(0) ; practicas = lista_practicas.pop(0)
            nota_final = ((parcial1 * 0.3) + (parcial2 * 0.3)) + (practicas * 0.4) ; nota_final = round(nota_final, 2)
            if asistencia >= "0.75" and nota_final >= 5 and practicas >= 4:
                alumno=f"{nombre} {apellido} y su nota es {nota_final}"
                aprobados.append(alumno)
            else:
                alumno=f"{nombre} {apellido} y su nota es {nota_final}"
                suspensos.append(alumno)
        print(f"\nLos alumnos que han aprobado son:\n")
        for x in aprobados:
            print(Fore.GREEN + x)
        print(Fore.WHITE + "\nLos alumnos que han suspendido son:\n")
        for x in suspensos:
            print(Fore.RED + x)
        elegir_subejercicio()


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n\n¿Qué enunciado quieres ejecutar? \n --> 1: Visualizar los datos\n --> 2: Diccionario con notas finales\n --> 3: Aprobados/suspensos\n --> 4: Finalizar el programa\n") ; print(Style.RESET_ALL, end="")
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
```
Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159691021-7f2c9976-b75a-4826-b3ac-91da70d05f05.png)

En formato [XML](https://github.com/Diegodesantos1/Ejecicios_POO_Archivos/blob/main/UML/Calificaciones.drawio)

