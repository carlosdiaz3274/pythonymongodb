import pymongo
import certifi
import os

ca = certifi.where()

url = "mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url, tlsCAFile=ca)

db = client.test

mydb = client["Evaluacion01"]
mycol = mydb["CE"] #Conectamos con la db y la coleccion
#input() se utilizará para hacer pausas y avanzar con el teclado

while True:
    os.system("cls") #Limpia la pantalla
    print("Menu: ")
    print("1. Añadir un CE")
    print("2. Buscar un CE por _id")
    print("3. Actualizar un CE")
    print("4. Eliminar registro de CE")
    print("5. Salir")

    opcion = input("Ingrese su opcion: ") #Capturamos la opcion

    if opcion == "1":
        Identificador = int(input("Digite el _id del Centro Escolar: "))
        Nombre = input("Digite el nombre del Centro Escolar: ") #Capturamos el nombre del cliente
        Departamento = input("Digite el departamento: ") #Capturamos la direccion
        Municipio = input("Digite el municipio: ")

        mydic = { "_id":  Identificador, "Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio } #Creamos el diccionario
        x = mycol.insert_one(mydic) #lo insertamos en la base
        input()

    elif opcion == "2":
        key = int(input("Digite el _id a buscar en la base de datos: "))

        myquery = { "_id" : key }
        mydoc = mycol.find(myquery)
        for x in mydoc:  #Muestra el documento donde el _id sea el buscado
            print(x)
        input()
    elif opcion == "3":
        key = int(input("Digite el _id del CE a actualizar: "))
        myquery = { "_id" : key }
        mydoc = mycol.find(myquery)
        for x in mydoc:  #Muestra el documento donde el _id sea el buscado
            print(x)
        valor = input("Digite el nombre del CE: ")
        doc2 = { "$set" : {"Nombre": valor }}
        mycol.update_one(myquery, doc2)
        mydoc = mycol.find(myquery)
        for x in mydoc:  #Muestra el documento donde el _id sea el buscado
            print(x)
        input()
    
    elif opcion == "4":
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