import pandas as pd
import os

path = "/Users/evabatal/Exposcience-25-26-Aeolus/pulling_wind_data/downloads"

for file_name in os.listdir(path):
    if file_name.endswith('CSV'):
        file_path = os.path.join(path, file_name)
        df = pd.read_csv(file_path)

        wind_average = df['BOOM1_HORIZONTAL_WIND_SPEED'].mean()

        print(wind_average)
