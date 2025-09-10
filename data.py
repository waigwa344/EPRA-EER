import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Facilities and months
facilities = [f"Facility_{i}" for i in range(1, 11)]
months = pd.date_range("2020-01-01", periods=60, freq="M")

data = []

for facility in facilities:
    for month in months:
        energy_consumption = np.random.uniform(2000, 8000)   # kWh consumed
        energy_production = np.random.uniform(1000, 6000)    # kWh produced
        weather_var1 = np.random.uniform(10, 40)             # avg temp °C
        weather_var2 = np.random.uniform(20, 95)             # humidity %

        data.append([
            facility,
            month.strftime("%b-%Y"),
            round(energy_consumption, 2),
            round(energy_production, 2),
            round(weather_var1, 2),
            round(weather_var2, 2)
        ])

# Create DataFrame
df_large = pd.DataFrame(data, columns=[
    "Facility", "Month", "Energy_Consumption_kWh", 
    "Energy_Production_kWh", "Weather_Var1_Temperature_C", 
    "Weather_Var2_Humidity_%"
])

# Save to CSV and Excel
csv_path = "energy_dataset_2020_2024.csv"
excel_path = "energy_dataset_2020_2024.xlsx"

df_large.to_csv(csv_path, index=False)
df_large.to_excel(excel_path, index=False)

print(f"Datasets saved:\n- {csv_path}\n- {excel_path}")
