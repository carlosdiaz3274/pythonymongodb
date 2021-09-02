import conexion as net
import pandas as pd


mydb = net.client["mydatabase"]
mycol = mydb["desert"]
df = pd.read_csv("pythonymongodb-1\data\surveys.csv", delimiter=',')
df10 = df.head(1000)
for i in df10.index:
    print("Total income in ", df["sex"][i])

df10.reset_index(inplace=True)
data_dict = df10.to_dict("records")
mycol.insert_many(data_dict)