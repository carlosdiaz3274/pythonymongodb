import conexion as net
import os

db = net.client.test

mydb = net.client["mydatabase2"]
mycol = mydb["customers"] #Conectamos con la db y la coleccion
#input() se utilizará para hacer pausas y avanzar con el teclado

while True:
    os.system("cls") #Limpia la pantalla
    print("Menu: ")
    print("1. Añadir un registro")
    print("2. Ver los registros")
    print("3. Salir")

    opcion = input("Ingrese su opcion: ") #Capturamos la opcion

    if opcion == "1":
        Nombre = input("Digite el nombre del cliente: ") #Capturamos el nombre del cliente
        Direccion = input("Digite la direccion: ") #Capturamos la direccion

        mydic = { "name":  Nombre, "address": Direccion } #Creamos el diccionario
        x = mycol.insert_one(mydic) #lo insertamos en la base
        input()

    elif opcion == "2":
        for x in mycol.find():  #Ciclo For para imprimir todos los registros
            print(x)
        input()
    
    elif opcion == "3":
        print("Saliendo del sistema")
        input()
        break #saliendo del ciclo
    
    else:
        print("Opcion incorrecta")
        input()
        continue  #Continuando con el ciclo