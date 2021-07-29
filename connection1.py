import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.test

print(client.list_database_names()) #show databases en SQL

mydb = client["sample_restaurants"] #se accede a la bd

print(mydb.list_collection_names())

mycol = mydb["customers"]





