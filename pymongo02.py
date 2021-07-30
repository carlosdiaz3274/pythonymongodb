import conexion as net

print(net.client.list_database_names()) #se listan las db disponibles y existentes en la nube de mongo

mydb1 = net.client["mydatabase"] #se convierte en un acceso directo a la base de datos mydatabase
print(mydb1)