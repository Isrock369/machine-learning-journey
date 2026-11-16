import pandas as pd

data = {
    "nama": ["Andi", "Budi", "Citra", "Doni", "Eka"],
    "nilai": [85, None, 95, 70, None]
}

df = pd.DataFrame(data)

print("=== DATA AWAL ===")
print(df)

print("\n=== JUMLAH DATA KOSONG ===")
print(df.isnull().sum())

# Mengisi nilai kosong dengan rata-rata
rata_rata = df["nilai"].mean()
df["nilai"] = df["nilai"].fillna(rata_rata)

print("\n=== DATA SETELAH CLEANING ===")
print(df)

print("\n=== DATA KOSONG TERSISA ===")
print(df.isnull().sum())
