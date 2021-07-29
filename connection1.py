import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

#db = client.test

#print(client.list_database_names()) #show databases en SQL

mydb = client["mydatabase"] #se crea la base de datos mydatabase
mycol = mydb["equipos"] #se crea una coleccion
#mydic = { "_id": 3,  "name": "Aguila", "mascota": "Aguila", "departamento":"San Miguel", "integrantes": 22 } #preparamos los datos a ingrear
#print(mydb.list_collection_names())
#x = mycol.insert_one(mydic) #ingresamos los datos

x = mycol.find_one() #Encuentra el primer registro

print(x)

print("-------------------------")

for x in mycol.find({}, {"_id": 0, "name": 1, "departamento": 1}): #con un filtro, es decir, se menciona el nombre del campo : (0 si no debe aparecer, 1 si debe aparecer)
    print(x)







