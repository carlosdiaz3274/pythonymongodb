#BECA DE CIENCIA DE DATOS - SECRETARIA DE INNOVACION - GOBIERNO DE EL SALVADOR
#JUAN CARLOS DIAZ HERNANDEZ - 00635193-8 (dui)
# juan.diaz@cnr.gob.sv carlosdiaz.app@gmail.com
#TERCERA EVALUACION


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titanic_df = pd.read_csv("pythonymongodb-1/pasajeros-titanic.csv", delimiter=',', header=0)
pasajeros = pd.DataFrame(titanic_df)

while True:
    os.system("cls") #Limpia la pantalla
    print("Menu: ")
    print("1. Buscar por Ticket")
    print("2. Visualizar grafico de sobrevivencia y fallecidos")
    print("3. Visualizar grafico de sobrevivientes segun su clase")
    print("4. Costos de los tickets")
    print("5. Salir")

    opcion = input("Ingrese su opcion: ") #Capturamos la opcion

    if opcion == "1": #BUSQUEDA DE INFORMACION POR TICKET
        ticket = input("Digite el ticket a buscar: ")
        print(titanic_df[(titanic_df['Ticket']==ticket)])

        input()
    elif opcion == "2": #VISUALIZAR UN CE EN LA DB POR ID
        sobrevivientes = titanic_df.groupby('Sobrevivio')['Clase'].count()
        print(sobrevivientes)
        y = np.array([sobrevivientes[0], sobrevivientes[1]])
        mylabels = ["Fallecidos", "Sobrevivientes"]
        plt.pie(y, labels=mylabels, shadow=True)
        plt.show()
        
        input()
    elif opcion == "3": #ACTUALIZAR UN CE POR ID
        key = int(input("Digite el _id del CE cuyo NOMBRE se actualizará: "))
        myquery = { "_id" : key }
        mydoc = mycol.find(myquery, {"_id":0, "Departamento":0, "Municipio":0 })
        for x in mydoc:  #Mostramos el valor a cambiar
            print("El nombre a cambiar es: ", x)
        valor = input("Digite el nombre del CE: ")
        doc2 = { "$set" : {"Nombre": valor }}
        mycol.update_one(myquery, doc2)
        mydoc = mycol.find(myquery, {"_id":0 })
        for x in mydoc:  #imprimimos nuevamente el valor ya actualizado
            print(x)
        input()
    
    elif opcion == "4": #ELIMINAR UN CE POR ID
        key = int(input("Digite el _id del CE a eliminar: "))
        eliminar = { "_id" : key }
        mycol.delete_one(eliminar)
        print("El CE ", key, " ha sido eliminiado...")
        input()

    elif opcion == "5":
        print("Saliendo del sistema")
        input()
        break #saliendo del ciclo
    
    else:
        print("Opcion incorrecta")
        input()
        continue  #Continuando con el ciclo