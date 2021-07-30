import pymongo
import certifi

ca = certifi.where()

url = "mongodb+srv://jcdiaz:cd119105@cluster0.6ue2j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url, tlsCAFile=ca)

#usuario con privilegios de lectura y escritura