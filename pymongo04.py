import conexion as net

db = net.client.test #un test de conexion

mydb = net.client["mydatabase2"] #seleccionamos o creamos la db

mycol = mydb["customers"] #seleccionamos o creamos la coleccion

mydic = { "name": "Carlos", "address":"San Salvador" } #creamos un diccionario de python para insertarlo

x = mycol.insert_one(mydic) #ejecutamos la insercion con insert_one y lo guardamos en una variable

print(x.inserted_id) #imprimimos el ID del registro ingresado.