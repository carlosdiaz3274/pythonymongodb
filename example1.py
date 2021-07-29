import pymongo
import connection1

mydb2 = connection1.mydb()

mycol = mydb["equipos"]

y = mycol.find_one()

print(y)