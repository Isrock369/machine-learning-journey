harga_pc = int(input("Masukkan harga PC: "))
tabungan = int(input("Masukkan Tabungan: "))

if tabungan >= harga_pc:
	print("Target PC tercapai")
elif tabungan >= harga_pc / 2:
	print('Sudah setengah jalan')
else:
	print('perlu menabung')
