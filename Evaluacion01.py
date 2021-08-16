#BECA DE CIENCIA DE DATOS - SECRETARIA DE INNOVACION - GOBIERNO DE EL SALVADOR
#JUAN CARLOS DIAZ HERNANDEZ - 00635193-8 (dui)
# juan.diaz@cnr.gob.sv carlosdiaz.app@gmail.com
#PRIMERA EVALUACION

import pymongo
import certifi
import os

ca = certifi.where()

url = "mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url, tlsCAFile=ca)

db = client.test

mydb = client["Evaluacion01"]
mycol = mydb["CE"] #Conectamos con la db y la coleccion


while True:
    os.system("cls") #Limpia la pantalla
    print("Menu: ")
    print("1. Añadir un CE")
    print("2. Visualizar un CE por _id")
    print("3. Actualizar un CE")
    print("4. Eliminar registro de CE")
    print("5. Salir")

    opcion = input("Ingrese su opcion: ") #Capturamos la opcion

    if opcion == "1": #INSERTAR UN CE
        Identificador = int(input("Digite el _id del Centro Escolar: "))
        Nombre = input("Digite el nombre del Centro Escolar: ") #Capturamos el nombre del cliente
        Departamento = input("Digite el departamento: ") #Capturamos la direccion
        Municipio = input("Digite el municipio: ")

        mydic = { "_id":  Identificador, "Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio } #Creamos el diccionario
        x = mycol.insert_one(mydic) #lo insertamos en la base
        input()

    elif opcion == "2": #VISUALIZAR UN CE EN LA DB POR ID
        key = int(input("Digite el _id a buscar en la base de datos: "))

        myquery = { "_id" : key }
        mydoc = mycol.find(myquery)
        for x in mydoc:  #Muestra el documento donde el _id sea el buscado
            print(x)
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