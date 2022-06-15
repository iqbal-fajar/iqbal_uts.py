class sim:
    def __init__(self, formulir, ktp, sertifikat_kendaraan, sidik_jari, nota_pembayaran):
        self.formulir = formulir
        self.ktp = ktp
        self.sertifikat_kendaraan = sertifikat_kendaraan
        self.sidik_jari = sidik_jari
        self.nota_pembayaran = nota_pembayaran

    def keterangan(self):
        ket =""
        if sertifikat_kendaraan == "S" or sertifikat_kendaraan =="s":
            ket = "sepeda"
        elif sertifikat_kendaraan == "m" or sertifikat_kendaraan =="m":
            ket = "mobil"
        elif sertifikat_kendaraan == "t" or sertifikat_kendaraan =="t":
            ket = "truck"
        print("sim dengan\n formulir : {}\n ktp")
        print("sidik_jari:{}\n nota_pembayaran{}\n ")
# mengisi identitas
formulir = input("masukan formulir:")

# tanda identitas
ktp = input("masukan ktp")

sertifikat_kendaraan = input("masukan sertifikat_kendaraan")

sidik_jari = input("masukan sidik_jari")

#pengesahan identitas

nota_pembayaran = input("mengambil nota_pembayaran")

# s = sepeda
# m = mobil
# t = truck

sertifikat_kendaraan = input("pilih sertifikat_kendaraan [s/m/t]: ")

sim = sim(formulir, ktp, sertifikat_kendaraan, sidik_jari, nota_pembayaran)
sim.keterangan()








