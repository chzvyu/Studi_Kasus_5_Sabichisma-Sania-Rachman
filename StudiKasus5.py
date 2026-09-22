def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "standard": 
        tarif = 200000
    elif jenis_kamar == "deluxe":
        tarif = 350000
    else:
        return 0

    total = tarif * lama_menginap
    return total

# masukkan data
jenis_kamar = input("Masukkan jenis kamar (standard/deluxe): ")
tanggal_check_in = int(input("Tanggal check-in: "))
tanggal_check_out = int(input("Tanggal check-out: "))

# hitung lama menginap dan total
lama_menginap = tanggal_check_out - tanggal_check_in
total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

# hasil
print("-----PEMESANAN HOTEL-----")
print("Jenis Kamar       :", jenis_kamar)
print("Tanggal Check-in  :", tanggal_check_in)
print("Tanggal Check-out :", tanggal_check_out)
print("Lama Menginap     :", lama_menginap, "malam")
print("Total Biaya       : Rp", total_biaya)