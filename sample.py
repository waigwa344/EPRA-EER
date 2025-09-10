import pandas as pd

# Create 24 months of sample data for 2 facilities
months = pd.date_range("2022-01-01", periods=24, freq="M")

data = []
for facility in ["Facility A", "Facility B"]:
    for m in months:
        energy = 1000 + (hash(facility + str(m)) % 200)   # pseudo-random energy
        production = 200 + (hash("prod" + facility + str(m)) % 50)
        weather1 = 20 + (hash("w1" + facility + str(m)) % 5)
        weather2 = 10 + (hash("w2" + facility + str(m)) % 3)
        data.append([facility, m.strftime("%Y-%m"), energy, production, weather1, weather2])

df = pd.DataFrame(data, columns=["Facility", "Month", "Energy", "Production", "Weather1", "Weather2"])

# Save locally where you run this script
df.to_excel("sample_data.xlsx", index=False)

print("✅ sample_data.xlsx created successfully!")
