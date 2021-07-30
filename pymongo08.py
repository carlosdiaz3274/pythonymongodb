import conexion as net

db = net.client.test    

mydb = net.client["mydatabase2"]
mycol = mydb["customers"]
doc = { "name" : "Andrea" } #documento con el registro a buscar
doc2 = { "$set": {"address": "San Salvador" } } # el campo a actualizar

mycol.update_one(doc, doc2) #se actualiza