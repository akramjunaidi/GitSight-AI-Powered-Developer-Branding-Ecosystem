import matplotlib.pyplot as plt
import numpy as np

GRAVITASI = 9.8      # Percepatan gravitasi (m/s^2)
RHO_UDARA = 1.225    # Kepadatan udara (kg/m^3)

H_NAMA = "Hezarfen Ahmad Celebi"
H_MASSA = 90.0
H_V = 15.0
H_A = 15.0
H_CL = 0.8
H_CD = 0.05
H_D_VER = 60.0

H_W = H_MASSA * GRAVITASI
H_L = 0.5 * RHO_UDARA * (H_V ** 2) * H_A * H_CL
H_D = 0.5 * RHO_UDARA * (H_V ** 2) * H_A * H_CD
H_GR = H_L / H_D


B_NAMA = "Abbas Bin Firnas"
B_MASSA = 80.0
B_V = 12.0
B_A = 10.0
B_CL = 0.6
B_CD = 0.1
B_D_VER = 20.0

B_W = B_MASSA * GRAVITASI
B_L = 0.5 * RHO_UDARA * (B_V ** 2) * B_A * B_CL
B_D = 0.5 * RHO_UDARA * (B_V ** 2) * B_A * B_CD
B_GR = B_L / B_D


# Data yang akan divisualisasikan
nama_tokoh = [H_NAMA, B_NAMA]
rasio_luncur = [H_GR, B_GR]
gaya_angkat = [H_L, B_L]
gaya_berat = [H_W, B_W]

plt.figure(figsize=(8, 6))
plt.bar(nama_tokoh, rasio_luncur, color=['#1f77b4', '#ff7f0e'])
plt.title('Perbandingan Rasio Luncur (L/D)', fontsize=14)
plt.ylabel('Rasio Luncur (L/D)', fontsize=12)
plt.xlabel('Tokoh Sejarah', fontsize=12)

for i, v in enumerate(rasio_luncur):
    plt.text(i, v + 0.5, f'{v:.2f}:1', ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

x = np.arange(len(nama_tokoh))  # Label lokasi untuk tokoh
width = 0.35  # Lebar bar

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, gaya_angkat, width, label='Daya Angkat (L)', color='skyblue')
rects2 = ax.bar(x + width/2, gaya_berat, width, label='Gaya Berat (W)', color='darkred')

ax.set_ylabel('Gaya (Newton)', fontsize=12)
ax.set_title('Perbandingan Daya Angkat (L) vs Gaya Berat (W)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(nama_tokoh)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f} N',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()