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
            tabla = pd.read_csv("calificaciones.csv", on_bad_lines="skip", encoding = "UTF8", sep=";")
            print(f"{tabla}\n\n\n")
        elif visualizar == 2:
            diccionario = pd.read_csv("calificaciones.csv", on_bad_lines="skip", encoding = "UTF8", sep=";").to_dict()
            print(f"{diccionario}\n\n\n")
        elif visualizar == 3:
            with open("calificaciones.csv", "r") as f:
                reader=csv.reader(f, delimiter=";")
                lista_de_listas = list(reader)
                print(lista_de_listas)
        else:
            print(Fore.RED + "No válido")
            Calificaciones_estudiantes.recibir_diccionario()
    def nota_final(): #Apartado 2
        lista_de_listas = [["Anido Bonet", "David", "90%", "5.5", "2.75", "0", "5", "0", "0"],["Bueno Cerdeira", "Patricia", "95%", "9.5", "9", "0", "0", "6.25", "0"],["Casariego García", "Raúl", "98%", "4.25", "5.75", "0", "0", "4", "5"],["Curbelo Sánchez", "Jorge", "75%", "6.75", "4.25", "0", "0", "0", "6.5"],["Díaz Souto", "Sofía", "82%", "7", "6.5", "0", "0", "9", "0"],["García Perez", "Yaiza", "85%", "10", "8", "0", "0", "7.5", "0"],["Sánchez Jordán", "María", "92%", "8.75", "9", "0", "0", "6.5", "0"],["Lorenzo García", "Jaime", "100%", "9.75", "8.25", "0", "0", "7.5", "0"],["Martínez Lucas", "Cecilia", "86%", "7", "4", "0", "0", "6.25", "0"],["Mora Peñaloza", "Sandra", "70%", "5.25", "2", "0", "4", "6.5", "0"],["Morillo Escudero", "Ana", "100%", "9.5", "10", "0", "0", "8.75", "0"],["Muñoz Gómez", "Carolina", "94%", "7.75", "6.5", "0", "0", "4", "0"],["Ramirez de la Puente", "Raquel", "75%", "0", "1", "1", "2.75", "2.25", "3.25"],["Riego Pizarro", "Carlos", "75%", "4", "2.5", "5", "3.75", "0", "0"],["Rodríguez de Blas", "Ignacio", "80%", "8.25", "5.25", "0", "0", "6.5", "0"],["Moreno Angulo", "Antonio", "88%", "9", "6.75", "0", "0", "5.25", "0"]]
        n = 15
        for i in range (n):
            lista_inicial=lista_de_listas.pop(n)
            parcial1= (lista_inicial.pop(3)) ; parcial2 = (lista_inicial.pop(3)) ; final = (lista_inicial.pop(5))
            parcial1 = float(parcial1) ; parcial2 = float(parcial2) ; final = float(final)
            nota_final = ((((parcial1) + (parcial2)) * 0.6) + ((final) * 0.4))
            round(nota_final)
            lista_inicial.append(nota_final)
            n=+1
            print(lista_inicial)

Calificaciones_estudiantes.nota_final()