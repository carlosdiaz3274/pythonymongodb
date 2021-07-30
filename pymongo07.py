import conexion as net

db = net.client.test

mydb = net.client["mydatabase2"]
mycol = mydb["customers"]

myquery = { "name" : "Carlos" }

mydoc = mycol.delete_one(myquery)
