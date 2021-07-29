import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

#db = client.test

#print(client.list_database_names()) #show databases en SQL

mydb = client["mydatabase"] #se crea la base de datos mydatabase
mycol = mydb["equipos"] #se crea una coleccion
mydic = { "_id": 3,  "name": "Aguila", "mascota": "Aguila", "departamento":"San Miguel", "integrantes": 22 } #preparamos los datos a ingrear
#print(mydb.list_collection_names())
x = mycol.insert_one(mydic) #ingresamos los datos

print(x)







