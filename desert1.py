import pandas as pd

#ESTOS SIRVEN PARA CONOCER EL DIRECTORIO RAIZ DE DONDE SE ESTÁ EJECUTANDO
#import os
#current_directory = os.getcwd()
#print(current_directory)

#path relativo: pythonymongodb-1\data\surveys.csv
surveys_df = pd.read_csv("pythonymongodb-1/data/surveys.csv", delimiter=',')

#print(surveys_df, " \n")
#print(surveys_df.describe(), " \n")
#print(surveys_df.info(), " \n")
#print(surveys_df.columns, " \n")
grouped_sex = surveys_df[surveys_df['sex'].notnull()]
print(grouped_sex, " \n")