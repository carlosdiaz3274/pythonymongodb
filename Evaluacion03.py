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
    print("ANALISIS DE LA LISTA DE PASAJEROS DEL TITANIC")
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
    elif opcion == "2": #VISUALIZAR SOBREVIVIENTES Y FALLECIDOS
        sobrevivientes = titanic_df.groupby('Sobrevivio')['Clase'].count()
        print(sobrevivientes)
        y = np.array([sobrevivientes[0], sobrevivientes[1]])
        colores = ["#38B3F9", "#A9E0FF"]
        mylabels = ["Fallecidos", "Sobrevivientes"]
        plt.pie(y, labels=mylabels, shadow=True, autopct="%0.1f %%", colors=colores)
        plt.title('Sobrevivientes y Fallecidos')
        plt.show()
        
        input()
    elif opcion == "3": #VISUALIZAR SEGUN CLASE
        clases = titanic_df.groupby('Clase')['Clase'].count()
        eje_x = ['Primera clase', 'Segunda clase', 'Tercera clase']
        eje_y = np.array([clases.loc[1], clases.loc[2], clases.loc[3]])
        plt.bar(eje_x, eje_y)
        plt.ylabel = ('Pasajeros')
        plt.xlabel = ('Clase')
        plt.title('Tipo (Clase) de boleto y viaje en el TITANIC')
        plt.show()
        input()
    
    elif opcion == "4": #CONOCER EL COSTO DE LOS TICKETS
        costos = titanic_df[titanic_df['Tarifa'].notnull()]
        print("El ticket mas caro fue: $", costos['Tarifa'].max())
        print("El ticket mas barato fue: $", costos['Tarifa'].min())
        input()
    elif opcion == "5":
        print("Saliendo del sistema")
        input()
        break #saliendo del ciclo
    
    else:
        print("Opcion incorrecta")
        input()
        continue  #Continuando con el ciclo