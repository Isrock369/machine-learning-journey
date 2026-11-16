import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print("Shape:", data.shape)
print("Dimensi:", data.ndim)

hasil = data.reshape(2, 6)
print("Hasil reshape:")
print(hasil)
