from zipfile import ZipFile
import os

path = "/Users/evabatal/Exposcience-25-26-Aeolus/pulling_wind_data/downloads"

os.chdir(path)

for file_name in os.listdir(path):
    if file_name.endswith('zip'):
        with ZipFile(file_name, 'r') as file:
            file.extractall(path)



