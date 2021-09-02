import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

surveys_df = pd.read_csv("pythonymongodb-1\data\surveys.csv", delimiter=',')

print(surveys_df, " \n")

species_counts = surveys_df.groupby('sex')['record_id'].count()
print(species_counts)

y = np.array([ species_counts[0], species_counts[1]])

mylabels = ["Femenino", "Masculino"]

plt.pie(y, labels= mylabels, shadow=True)
plt.legend(title = "Sexo de especies monitoreadas:")
plt.show()