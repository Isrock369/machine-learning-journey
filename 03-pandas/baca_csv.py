import pandas as pd
from pathlib import Path

# Menentukan lokasi file CSV
lokasi_file = Path(__file__).with_name("data_siswa.csv")

# Membaca data
df = pd.read_csv(lokasi_file)

print("=== DATA SISWA ===")
print(df)

print("\n=== JUMLAH BARIS DAN KOLOM ===")
print(df.shape)

print("\n=== TOP 3 SISWA ===")
print(df.sort_values(by="nilai", ascending=False).head(3))
