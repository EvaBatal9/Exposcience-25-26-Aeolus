import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('wind_data_allsols/wind_data_sol_36.csv')

df['LTST_time'] = df['LTST'].str.split().str[-1]

def hms_to_seconds(hms):
    h, m, s = map(float, hms.split(':'))
    return h*3600 + m*60 + s

df['LTST_seconds'] = df['LTST_time'].apply(hms_to_seconds)

df['BOOM1_HORIZONTAL_WIND_SPEED'] = pd.to_numeric(df['BOOM1_HORIZONTAL_WIND_SPEED'], errors='coerce')

plt.figure(figsize=(10,5))
plt.plot(df['LTST_seconds'], df['BOOM1_HORIZONTAL_WIND_SPEED'], label='Boom 1 Wind Speed', color='blue', linewidth=0.2)
x = df['LTST_seconds'].values
y = df['BOOM1_HORIZONTAL_WIND_SPEED'].values

mask = ~np.isnan(y)
m, b = np.polyfit(x[mask], y[mask], 1)

trendline = m*x + b

plt.plot(x, trendline, color='red', label='trendline', linewidth=1)

plt.title('Wind Speed (Boom 1) over Sol 36')
plt.xlabel('Local True Solar Time (seconds since sol start)')
plt.ylabel('Horizontal Wind Speed (m/s)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
