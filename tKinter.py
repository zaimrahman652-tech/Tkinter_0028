import tkinter as tk
from tkinter import messagebox


def hitung_prediksi():
  # Validasi sederhana apakah semua kolom input terisi
  for entry in entry_list:
    if not entry.get():
      messagebox.showwarning(
          "Peringatan", "Semua nilai mata pelajaran harus diisi terlebih dahulu!"
      )
      return

  # Sesuai ketentuan tugas: fungsi menuliskan prodi Teknologi Informasi apapun input yang diberikan
  hasil_label.config(
      text="Hasil Prediksi: Teknologi Informasi", fg="darkgreen"
  )


# Inisialisasi Jendela Utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x600")
root.config(bg="#f0f0f0")

# --- FRAME UTAMA ---
main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# 1. Label Judul Aplikasi
judul_label = tk.Label(
    main_frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
judul_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# 2. Pembuatan 10 Input Nilai Mata Pelajaran
entry_list = []
mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sosiologi",
    "Sejarah",
]

for i, mapel in enumerate(mata_pelajaran):
  # Label nama mata pelajaran
  lbl = tk.Label(
      main_frame,
      text=f"Nilai {mapel}:",
      font=("Arial", 10),
      bg="#f0f0f0",
      anchor="w",
  )
  lbl.grid(row=i + 1, column=0, sticky="w", pady=4)

  # Kolom input (Entry) nilai
  ent = tk.Entry(main_frame, font=("Arial", 10), width=15)
  ent.grid(row=i + 1, column=1, sticky="e", pady=4)
  entry_list.append(ent)

# 3. Button Bertuliskan "Hasil Prediksi"
prediksi_button = tk.Button(
    main_frame,
    text="Hasil Prediksi",
    font=("Arial", 11, "bold"),
    bg="#007ACC",
    fg="white",
    padx=10,
    pady=5,
    command=hitung_prediksi,
)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# 4. Label Luaran Hasil Prediksi
hasil_label = tk.Label(
    main_frame,
    text="Hasil Prediksi: -",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()