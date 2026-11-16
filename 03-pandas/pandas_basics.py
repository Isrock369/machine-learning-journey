import pandas as pd

data = {
    "nama": ["Andi", "Budi", "Citra", "Doni", "Eka"],
    "kelas": ["A", "B", "A", "B", "A"],
    "nilai": [85, 60, 95, 70, 90]
}

df = pd.DataFrame(data)

print("=== DATA SISWA ===")
print(df)

print("\n=== NILAI MINIMAL 80 ===")
print(df[df["nilai"] >= 80])

print("\n=== RATA-RATA PER KELAS ===")
print(df.groupby("kelas")["nilai"].mean())

print("\n=== TOP 3 NILAI TERTINGGI ===")
print(df.sort_values(by="nilai", ascending=False).head(3))
