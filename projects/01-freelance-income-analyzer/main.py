import numpy as np

# Data penghasilan freelance (simulasi)
pendapatan = np.array([
    200000, 350000, 150000, 500000, 700000
])

# Target PC
target_pc = 30000000

# 1. Hitung total pendapatan
total_pendapatan = np.sum(pendapatan)

# 2. Hitung rata-rata pendapatan
rata_rata = np.mean(pendapatan)

# 3. Cari pendapatan terbesar
pendapatan_terbesar = np.max(pendapatan)

# 4. Hitung sisa target PC
sisa_target = max(0, target_pc - total_pendapatan)

# 5. Hitung persentase pencapaian
persentase = (total_pendapatan / target_pc) * 100

# 6. Tampilkan hasil analisis
print("=== FREELANCE INCOME ANALYZER ===")

print(f"Total Pendapatan    : Rp {total_pendapatan:,.0f}")
print(f"Rata-rata Pendapatan: Rp {rata_rata:,.0f}")
print(f"Pendapatan Terbesar : Rp {pendapatan_terbesar:,.0f}")
print(f"Target PC           : Rp {target_pc:,.0f}")
print(f"Pencapaian Target   : {persentase:.1f}%")

if total_pendapatan >= target_pc:
    print("Status              : Target PC tercapai!")
else:
    print(f"Sisa Menuju Target  : Rp {sisa_target:,.0f}")

