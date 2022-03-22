
def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Calificaciones\n"))
    if variable == 1:
        from Clases import Calificaciones
    else:
        eleccion_ejercicio()
eleccion_ejercicio()