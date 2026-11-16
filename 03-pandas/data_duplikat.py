import pandas as pd

data = {
    "nama": ["Andi", "Budi", "Citra", "Andi", "Eka"],
    "nilai": [85, 70, 95, 85, 90]
}

df = pd.DataFrame(data)

print("=== DATA AWAL ===")
print(df)

print("\n=== JUMLAH DUPLIKAT ===")
print(df.duplicated().sum())

hasil = df.drop_duplicates()

print("\n=== SETELAH DUPLIKAT DIHAPUS ===")
print(hasil)

