import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.test

print(client.list_database_names()) #show databases en SQL

mydb = client["mydatabase"] #se accede a la bd

mycol = mydb["customers"]

print("estare en github")



