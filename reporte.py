import json

def reporte():  
    print("********************************************************************")
    print("*  Autor                           Cantidad de libros prestados    *")
    print("********************************************************************")
    print("Gabriel García Márquez                           1                  ")
    print("Isabel Allende                                   0                  ")
    print("Julio Cortazár                                  10                  ")
    print("Jorge Luis Borges                                7                  ")
    print("Pablo Neruda                                     5                  ")

with open ("reportes_bivlioteca_mundo_libros.json" , "r") as archivo:
    leer = json.load(reporte , archivo)