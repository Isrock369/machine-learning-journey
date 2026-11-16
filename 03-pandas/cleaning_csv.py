import pandas as pd
from pathlib import Path

lokasi = Path(__file__).with_name("data_kotor.csv")

df = pd.read_csv(lokasi)

print("=== DATA AWAL ===")
print(df)

print("\n=== DATA KOSONG ===")
print(df.isnull().sum())

print("\n=== JUMLAH DUPLIKAT ===")
print(df.duplicated().sum())

# Hapus baris duplikat
df = df.drop_duplicates().copy()

# Isi nilai kosong dengan rata-rata
rata_rata = df["nilai"].mean()
df["nilai"] = df["nilai"].fillna(rata_rata)

# Rapikan index
df = df.reset_index(drop=True)

print("\n=== DATA BERSIH ===")
print(df)

# Simpan hasil cleaning
output = Path(__file__).with_name("data_bersih.csv")
df.to_csv(output, index=False)

print("\nData berhasil disimpan ke data_bersih.csv")
