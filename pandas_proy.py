# Se importa la librería

import pandas as pd

# Se generan dos listas, una que contiene los estados

# y otra que contiene la población de cada estado
states = ["California", "Texas", "Florida", "New York"]
population = [39613493, 29730311, 21944577, 19299981]

# Se almacenan estas listas en un diccionario de datos

dict_states = {'States': states, 'Population': population}

# Se crea el dataframe
df_population = pd.DataFrame.from_dict(dict_states)

# Se visualiza el contenido de ese dataframe

print(df_population)

print(df_population.columns)