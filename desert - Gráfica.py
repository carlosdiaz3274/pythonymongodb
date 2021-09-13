import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
surveys_df = pd.read_csv("pythonymongodb-1/data/surveys.csv", delimiter=',')

print(surveys_df , " \n")

#Generamos un nuevo dataset con campos no vacios en la columna de Sexo
species_counts = surveys_df.groupby('sex')['record_id'].count()
print(species_counts)

y = np.array([ species_counts[0], species_counts[1]])

mylabels = ["F", "M"]

#plt.pie(y, labels = mylabels, shadow = True)
#plt.legend(title = "Sexo de Especies Monitoreadas:")
#plt.show()