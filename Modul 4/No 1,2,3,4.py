dclass MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Rapinsha', 10, 'Salatiga', 250000)
c1 = MhsTIF('Shanum', 14, 'Solo', 260000)
c2 = MhsTIF('Sheryn', 12, 'Surabaya', 300000)
c3 = MhsTIF('Gathan', 21, 'Tangerang', 250000)
c4 = MhsTIF('Fathan', 20, 'Bogor', 350000)
c5 = MhsTIF('Jehan', 30, 'Sidoarjo', 450000)
c6 = MhsTIF('Ehrlich', 11, 'Bandung', 650000)
c7 = MhsTIF('Alaric', 13, 'Surabaya', 2750000)
c8 = MhsTIF('Heinrich', 16, 'Cilacap', 250000)
c9 = MhsTIF('Richmond', 6, 'Semarang', 565000)
c10 = MhsTIF('Carlton', 5, 'Banjarmasin', 450000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#No1
def cariKota(target):
    z = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            z.append(hasil)
    return z

#No2
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = Daftar[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil.uangSaku:
            terkecil = Daftar[i]

    return terkecil

#No3
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = [Daftar[0]]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil

#No4
def cariDaftarUangSakuKurang(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 300000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b
