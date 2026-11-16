import pandas as pd
from pathlib import Path

# Lokasi dataset
lokasi = Path(__file__).with_name("data_siswa.csv")

# Membaca dataset
df = pd.read_csv(lokasi)

print("=== STUDENT PERFORMANCE ANALYZER ===")

print("\n=== DATA AWAL ===")
print(df)

print("\n=== UKURAN DATASET ===")
print(df.shape)

print("\n=== INFORMASI DATASET ===")
df.info()

print("\n=== JUMLAH DATA KOSONG ===")
print(df.isnull().sum())

print("\n=== JUMLAH BARIS DUPLIKAT ===")
print(df.duplicated().sum())

print("\n=== PROSES DATA CLEANING ===")

# 1. Menghapus data duplikat
df_bersih = df.drop_duplicates().copy()

# 2. Menghitung rata-rata nilai yang tersedia
rata_rata = df_bersih["nilai"].mean()

# 3. Mengisi nilai kosong dengan rata-rata
df_bersih["nilai"] = df_bersih["nilai"].fillna(rata_rata)

# 4. Merapikan index
df_bersih = df_bersih.reset_index(drop=True)

print("\n=== DATA SETELAH CLEANING ===")
print(df_bersih)

print("\n=== HASIL VALIDASI ===")
print("Ukuran dataset:", df_bersih.shape)
print("Data kosong:", df_bersih.isnull().sum().sum())
print("Duplikat:", df_bersih.duplicated().sum())

# 5. Menyimpan data bersih
output = Path(__file__).with_name("data_bersih.csv")
df_bersih.to_csv(output, index=False)

print("\nData bersih berhasil disimpan!")

# === TAHAP 4: DATA ANALYSIS ===

print("\n=== STATISTIK KESELURUHAN ===")
print("Total siswa:", len(df_bersih))
print("Rata-rata nilai:", round(df_bersih["nilai"].mean(), 2))
print("Nilai tertinggi:", df_bersih["nilai"].max())
print("Nilai terendah:", df_bersih["nilai"].min())

print("\n=== RATA-RATA PER KELAS ===")
rata_kelas = df_bersih.groupby("kelas")["nilai"].mean()
print(rata_kelas)

print("\n=== TOP 3 SISWA ===")
top_3 = df_bersih.sort_values(
    by="nilai",
    ascending=False
).head(3)

print(top_3[["nama", "kelas", "nilai"]])

print("\n=== RINGKASAN PER KELAS ===")
ringkasan = df_bersih.groupby("kelas")["nilai"].agg(
    ["count", "mean", "min", "max"]
)

print(ringkasan)

# Simpan ringkasan ke CSV
output_ringkasan = Path(__file__).with_name("ringkasan_kelas.csv")
ringkasan.to_csv(output_ringkasan)

print("\nRingkasan berhasil disimpan!")

# === TAHAP 5: DATA VISUALIZATION ===

import matplotlib.pyplot as plt

print("\n=== MEMBUAT GRAFIK ===")

# Mengambil rata-rata nilai setiap kelas
rata_kelas = df_bersih.groupby("kelas")["nilai"].mean()

# Membuat grafik batang
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    rata_kelas.index,
    rata_kelas.values,
    color=["#3498db", "#2ecc71"]
)

# Judul dan keterangan
ax.set_title("Rata-rata Nilai Siswa per Kelas")
ax.set_xlabel("Kelas")
ax.set_ylabel("Rata-rata Nilai")
ax.set_ylim(0, 100)

# Menampilkan angka di atas batang
ax.bar_label(bars, fmt="%.2f", padding=3)

# Merapikan tampilan
fig.tight_layout()

# Simpan grafik sebagai gambar PNG
output_grafik = Path(__file__).with_name(
    "grafik_rata_rata_kelas.png"
)

fig.savefig(output_grafik, dpi=150)

print("Grafik berhasil disimpan!")

# Menampilkan grafik
plt.show()
