import conexion as net

db = net.client.test
mydb = net.client["mydatabase2"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x) #imprime el primer registro.
print()
for x in mycol.find():  #muestra todos los registros
    print(x) 

print()
for x in mycol.find({}, {"_id": 0, "name": 1}):
    print(x) #muestra solo los nombres

print()
myquery = { "address" : "San Salvador" } 
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x) #muestra los documentos que en address contenga San Salvador

print("busqueda especifica")
myquery2 = { "name": { "$gt": "Andrea" } }
mydoc2 = mycol.find(myquery2)
for x in mydoc2:
    print(x) #muestra los documentos donde inicie con S
