import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('averages_per_sol_data.txt', header=None, names=['BOOM1_HORIZONTAL_WIND_SPEED'])


x = np.arange(36, 36+len(df))
y = df['BOOM1_HORIZONTAL_WIND_SPEED'].values

plt.figure(figsize=(10,5))
plt.plot(x, y, label='Boom 1 Wind Speed', color='blue', linewidth=0.5)

mask = ~np.isnan(y)
m, b = np.polyfit(x[mask], y[mask], 1)

trendline = m*x + b

plt.plot(x, trendline, color='red', label='trendline', linewidth=1)

plt.title('Average wind speeds per sol between sol 36-309')
plt.xlabel('Sol number')
plt.ylabel('Horizontal Wind Speed (m/s)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
