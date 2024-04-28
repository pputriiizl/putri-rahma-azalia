print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")


nilai_tugas = float(input("Silahkan Masukan nilai Tugas Anda: "))
nilai_uts = float(input("Silahkan Masukan nilai UTS Anda: "))
nilai_uas = float(input("Silahkan Masukan nilai UAS Anda: "))

nilai_akhir = (0.25 * nilai_tugas) + (0.35 * nilai_uts) + (0.40 * nilai_uas)


print("Nilai Akhir Anda: ", nilai_akhir)

if nilai_akhir > 85:
    print("Dalam Huruf: A")
elif nilai_akhir > 80:
    print("Dalam Huruf: A-")
elif nilai_akhir > 75:
    print("Dalam Huruf: B+")
elif nilai_akhir > 70:
    print("Dalam Huruf: B")
elif nilai_akhir > 65:
    print("Dalam Huruf: B-")
elif nilai_akhir > 60:
    print("Dalam Huruf: C+")
elif nilai_akhir > 55:
    print("Dalam Huruf: C")
elif nilai_akhir > 50:
    print("Dalam Huruf: C-")
elif nilai_akhir > 30:
    print("Dalam Huruf: D")
else:
    print("Dalam Huruf: E")