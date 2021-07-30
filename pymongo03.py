import conexion as net

db = net.client.test
mydb = net.client["mydatabase"] #acceso a la DB mydatabase

mycol = mydb["customers"] #acceso a la coleccion equipos

print(mycol)