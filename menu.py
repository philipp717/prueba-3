import json

def menu():
    while True:
        print("**********************")
        print("*    MUNDO LIBRO     *")
        print("**********************")
        print("[1] Mantenedor de autores")
        print("[2] Reportes")
        print("[3] SALIR")
        opc = input("Indique una opcion: ")
 
    
        if opc == "1":
            print("**********************")
            print("* MANTENEDOR AUTORES *")
            print("**********************")
            print("[1] Agregar autor")
            print("[2] Editar autor")
            print("[3] Eliminar autor")
            print("[4] Buscar autor")
            print("[5] Volver")
            opc_mantenedor_autores = input("Indique una opción: ")
            if opc_mantenedor_autores == "1":
                agregar_autor = input("Indique el Autor que desea agregar: ")
                with open ("menu.json", "x") as archivo:
                    agrega = json.dump(menu, agregar_autor)
            if opc_mantenedor_autores == "2":
                nom = input("indique un nuevo nombre: ")
                nacionalidad = ("Indique la nueva nacionalidad: ")
                with open ("menu.json", "w") as archivo:
                    edita = json.dump(menu , [nom , nacionalidad])
            if opc_mantenedor_autores == "3":
                elimina_autor = input("ingrese el id del autor: ")
                with open ("menu.json" , "w") as archivo:
                    edita = json.dump(menu , " ")
            if opc_mantenedor_autores == "4":
                buscar_autor = input("ingrese el id del autor: ")
                with open ("menu.json" , "r") as archivo:
                    busca = json.load(menu, archivo)



        elif opc == "2":
            print("********************************************************************")
            print("*  Autor                           Cantidad de libros prestados    *")
            print("********************************************************************")
            print("Gabriel García Márquez                           1                  ")
            print("Isabel Allende                                   0                  ")
            print("Julio Cortazár                                  10                  ")
            print("Jorge Luis Borges                                7                  ")
            print("Pablo Neruda                                     5                  ")

        elif opc == "3":
            print("SALIENDO...")
            break
        else:
            print("Opción incorrecta") 
            break

    with open ("menu.json" , "r") as archivo:
        lectura = json.load(menu , archivo)