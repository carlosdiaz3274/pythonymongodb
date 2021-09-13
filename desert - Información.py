import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
surveys_df = pd.read_csv("pythonymongodb-1/data/surveys.csv", delimiter=',')


print(surveys_df, " \n")

print(surveys_df.describe(), " \n")

print(surveys_df.info(), " \n")

# Echemos un vistazo a las columnas
print(surveys_df.columns, " \n")



#Generamos un nuevo dataset con campos no vacios en la columna de Sexo
grouped_sex = surveys_df[surveys_df['sex'].notnull()]

print(grouped_sex, " \n")


