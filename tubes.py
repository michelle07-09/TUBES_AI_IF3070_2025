import math, random, copy, time
import matplotlib.pyplot as plt

class Konfigurasi:
    def __init__(self):
        self.representasi_barang = []
        self.ukuran_barang = []
        self.banyak_barang = 0
        self.terisi_kotak = []
        self.kapasitas_kotak = 0
        self.banyak_kotak = 1

    def __repr__(self):
        print(f'''
        ====================================================================
        Representasi Barang == {self.representasi_barang}
        Ukuran Barang       == {self.ukuran_barang}
        Banyak Barang       == {self.banyak_barang}
        Keterisian Kotak    == {self.terisi_kotak}
        Kapasitas Kotak     == {self.kapasitas_kotak}
        Banyak Kotak        == {self.banyak_kotak}
        ====================================================================
        ''')

def inisialisasi(konfigurasi):
    # kapasitas kotaknya berapa?
    konfigurasi.kapasitas_kotak = int(input("Kotaknya sebesar apa? "))

    # barangnya mau ada berapa?
    konfigurasi.banyak_barang = int(input("Mau ada berapa barang? "))

    # ukuran tiap barang berapa?
    for i in range (konfigurasi.banyak_barang):
        ukuran = int(input(f"Barang ke-{i+1} sebesar apa? "))
        konfigurasi.ukuran_barang.append(ukuran)
        konfigurasi.representasi_barang.append(1)
    
    # DEBUG
    # print("====================================================================")
    # print("CEK INISIALISASI")
    # print("====================================================================")
    # konfigurasi.__repr__()

    # sekarang konfigurasi awal terlihat seperti ini 
    # (misal ada 4 barang berukuran 1,2,3,4)
    # representasi_barang = [1,1,1,1]
    # ukuran_barang = [1,2,3,4]
    # banyak_barang = 4
    # terisi_kotak = [] --> nanti diisi oleh bagi adil
    # kapasitas_kotak = 5
    # banyak_kotak = 1

def bagi_adil(konfigurasi):
    # bagi adil maksudnya membuat kotak sebanyak total ukuran/kapasitas kotak 
    # (tapi dibulatkan ke atas), kepake di awal aja
    # hitung banyak kotak

    # TODO : REFAKTOR ke heuristik_kotak
    total_ukuran = sum(konfigurasi.ukuran_barang)
    konfigurasi.banyak_kotak = math.ceil(total_ukuran / konfigurasi.kapasitas_kotak)
    for i in range (konfigurasi.banyak_kotak):
        konfigurasi.terisi_kotak.append(0)

    # print("====================================================================")
    # print("CEK BAGI ADIL")
    # print("====================================================================")
    # konfigurasi.__repr__()  

    # sekarang konfigurasi awal terlihat seperti ini (misal ada 4 barang)
    # representasi_barang = [1,1,1,1]
    # ukuran_barang = [1,2,3,4]
    # banyak_barang = 4
    # terisi_kotak = [0,0]
    # kapasitas_kotak = 5
    # banyak_kotak = 2

def muat_duluan(konfigurasi):
    # setelah dibagi adil, kotaknya masih 0 semua kan
    # nah kita masukin tuh barangnya
    index_kotak = 0
    for i in range(konfigurasi.banyak_barang):
        # cek ukuran barang, kalau kotaknya masih muat masukin barangnya
        
        # print("----------")
        # print(f"INDEX KOTAK == {index_kotak}")
        # print(f"UKURAN BARANG KE {i} == {konfigurasi.ukuran_barang[i]}")
        # print(f"KETERISIAN KOTAK KE {i} == {konfigurasi.terisi_kotak[index_kotak]}")
        # print(f"BANYAK KOTAK == {konfigurasi.banyak_kotak}")
        # print(f"INDEX KOTAK == {index_kotak}")

        # ukuran barang + terisi kotak harus kurang dari kapasitas
        if konfigurasi.ukuran_barang[i] + konfigurasi.terisi_kotak[index_kotak] > konfigurasi.kapasitas_kotak:
            index_kotak += 1
            if index_kotak + 1> konfigurasi.banyak_kotak:
                konfigurasi.banyak_kotak += 1
                konfigurasi.terisi_kotak.append(0)


        konfigurasi.representasi_barang[i] = index_kotak + 1
        konfigurasi.terisi_kotak[index_kotak] += konfigurasi.ukuran_barang[i]

        # DEBUG
        # print(f"MUAT DULUAN - {i}")
        # print("====================================================================")
        # print("CEK MUAT DULUAN")
        # print("====================================================================")
        # konfigurasi.__repr__()

    # sekarang konfigurasi awal terlihat seperti ini (misal ada 4 barang)
    # representasi_barang = [1,1,1,1]
    # ukuran_barang = [1,2,3,4]
    # banyak_barang = 4
    # terisi_kotak = [3,3,4]
    # kapasitas_kotak = 5
    # banyak_kotak = 2

def atur_konfig(konfigurasi, representasi, ukuran_barang, kapasitas_kotak, banyak_kotak):
    konfigurasi.representasi_barang = representasi
    konfigurasi.ukuran_barang = ukuran_barang

    banyak_barang = len(representasi)
    konfigurasi.banyak_barang = banyak_barang

    konfigurasi.terisi_kotak = []
    for i in range (banyak_kotak):
        konfigurasi.terisi_kotak.append(0)

    konfigurasi.kapasitas_kotak = kapasitas_kotak
    konfigurasi.banyak_kotak = banyak_kotak

    for i in range (konfigurasi.banyak_barang):
        konfigurasi.terisi_kotak[konfigurasi.representasi_barang[i]-1] += konfigurasi.ukuran_barang[i]

    # print("CEK ATUR KONFIG")
    # konfigurasi.__repr__()

def fungsi_objektif(konfigurasi):
    densitas_total = 0
    penalti = 0
    for i in range (konfigurasi.banyak_kotak):
        densitas_total += konfigurasi.terisi_kotak[i] / konfigurasi.kapasitas_kotak
        if konfigurasi.terisi_kotak[i] > konfigurasi.kapasitas_kotak:
            penalti += konfigurasi.terisi_kotak[i] - konfigurasi.kapasitas_kotak
    densitas_rataan = densitas_total / konfigurasi.banyak_kotak

    heuristik_kotak = math.ceil(sum(konfigurasi.ukuran_barang) / konfigurasi.kapasitas_kotak)
    efisiensi = heuristik_kotak / konfigurasi.banyak_kotak


    fx = (3 * densitas_rataan + efisiensi) / ((100 * penalti) + 4)
    # return fx
    return round(fx * 1000, 0)

def cari_tetangga(konfigurasi):
    konfigurasi_sekarang = copy.copy(konfigurasi)

    representasi_sekarang = konfigurasi_sekarang.representasi_barang

    daftar_calon_representasi = []

    # buat beberapa tetangga acak, kita geser sedikit
    for i in range (1000):
        calon_representasi = copy.copy(representasi_sekarang)
        indeks_ganti = random.randint(1,len(calon_representasi) - 1)
        tipe_ganti = random.randint(1,100)
        if 1 <= tipe_ganti <= 59:
            maks_ganti = konfigurasi_sekarang.banyak_kotak - 1
        elif 60 <= tipe_ganti <= 89:
            maks_ganti = konfigurasi_sekarang.banyak_kotak
        else:
            maks_ganti = konfigurasi_sekarang.banyak_kotak + 1

        calon_representasi[indeks_ganti] = random.randint(1, maks_ganti)
        daftar_calon_representasi.append(calon_representasi)

    # print(daftar_calon_representasi)
    # semua tetangga ini harus dibuat konfigurasinya 
    # supaya kita bisa mendapatkan nilainya
    daftar_calon_konfigurasi = []
    nilai_terbaik = 0
    indeks_terbaik = 0
    for i in range (1000):
        calon_konfigurasi = Konfigurasi()
        atur_konfig(calon_konfigurasi, daftar_calon_representasi[i], konfigurasi_sekarang.ukuran_barang, konfigurasi_sekarang.kapasitas_kotak, max(daftar_calon_representasi[i]))
        daftar_calon_konfigurasi.append(calon_konfigurasi)

        nilai_calon = fungsi_objektif(calon_konfigurasi)

        if nilai_terbaik < nilai_calon:
            nilai_terbaik = nilai_calon
            indeks_terbaik = i

    tetangga_terpilih = daftar_calon_konfigurasi[indeks_terbaik]

    # DEBUG : NGECEK NILAI DARI 100 TETANGGA
    # for i in range(100):
    #     print(fungsi_objektif(daftar_calon_konfigurasi[i]))
    return tetangga_terpilih

# def buat_konfigurasi_awal():
#     # Membuat state awal
#     konfig_sekarang = Konfigurasi()
#     inisialisasi(konfig_sekarang)
#     bagi_adil(konfig_sekarang)
#     muat_duluan(konfig_sekarang)

# def cari_tetangga_awal(konfig_sekarang):
#     # Mencari tetangga
#     konfig_tetangga = cari_tetangga(konfig_sekarang)

#     # Menghitung nilai konfigurasi awal dan tetangga awal
#     nilai_sekarang = fungsi_objektif(konfig_sekarang)
#     nilai_tetangga = fungsi_objektif(konfig_tetangga)

#     print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
#     print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
#     print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
#     print("--------------------------------------------------")
#     return tetangga_awal

def hc_steepest_ascent():
    daftar_nilai_konf = []
    # ====================================================================
    # Membuat state awal
    konfig_sekarang = Konfigurasi()
    inisialisasi(konfig_sekarang)
    bagi_adil(konfig_sekarang)
    muat_duluan(konfig_sekarang)

    # Mencari tetangga
    konfig_tetangga = cari_tetangga(konfig_sekarang)

    # Menghitung nilai konfigurasi awal dan tetangga awal
    nilai_sekarang = fungsi_objektif(konfig_sekarang)
    nilai_tetangga = fungsi_objektif(konfig_tetangga)

    print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
    print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
    konfig_sekarang.__repr__()
    print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
    konfig_tetangga.__repr__()
    print("--------------------------------------------------")

    iterasi = 0
    while fungsi_objektif(konfig_tetangga) > fungsi_objektif(konfig_sekarang):
        daftar_nilai_konf.append(nilai_sekarang)
        konfig_sekarang = konfig_tetangga
        konfig_tetangga = cari_tetangga(konfig_sekarang)

        nilai_sekarang = fungsi_objektif(konfig_sekarang)
        nilai_tetangga = fungsi_objektif(konfig_tetangga)

        print("Membandingkan nilai konfigurasi...")
        print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
        konfig_sekarang.__repr__()
        print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
        konfig_tetangga.__repr__()
        iterasi += 1
    # ====================================================================
    print("State Akhir:")
    konfig_sekarang.__repr__()
    print(f"Iterasi: {iterasi}")

def hc_sideways_move():
    daftar_nilai_konf = []
    geser_maks = int(input("Berapa kali pergeseran maksimal? "))
    geser = 0
    # ====================================================================
    # Membuat state awal
    konfig_sekarang = Konfigurasi()
    inisialisasi(konfig_sekarang)
    bagi_adil(konfig_sekarang)
    muat_duluan(konfig_sekarang)

    # Mencari tetangga
    konfig_tetangga = cari_tetangga(konfig_sekarang)

    # Menghitung nilai konfigurasi awal dan tetangga awal
    nilai_sekarang = fungsi_objektif(konfig_sekarang)
    nilai_tetangga = fungsi_objektif(konfig_tetangga)

    print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
    print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
    konfig_sekarang.__repr__()
    print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
    konfig_tetangga.__repr__()
    print("--------------------------------------------------")

    while fungsi_objektif(konfig_tetangga) >= fungsi_objektif(konfig_sekarang):
        daftar_nilai_konf.append(nilai_sekarang)
        if geser == geser_maks:
            break

        konfig_sekarang = konfig_tetangga
        konfig_tetangga = cari_tetangga(konfig_sekarang)

        nilai_sekarang = fungsi_objektif(konfig_sekarang)
        nilai_tetangga = fungsi_objektif(konfig_tetangga)
        geser += 1

        print("Membandingkan nilai konfigurasi...")
        print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
        konfig_sekarang.__repr__()
        print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
        konfig_tetangga.__repr__()
    # ====================================================================
    print("State Akhir:")
    print(f"Banyak Pergeseran: {geser}")
    konfig_sekarang.__repr__()

def hc_random_restart():
    
    # Iterasi maksimal
    restart_maks = int(input("Restart maksimal? "))
    restart = 0

    daftar_calon_pemenang = []
    daftar_nilai = []
    konfig_pemenang = Konfigurasi()

    # Membuat state awal
    konfig_sekarang = Konfigurasi()
    inisialisasi(konfig_sekarang)
    bagi_adil(konfig_sekarang)
    muat_duluan(konfig_sekarang)

    # Mencari tetangga
    konfig_tetangga = cari_tetangga(konfig_sekarang)

    # Menghitung nilai konfigurasi awal dan tetangga awal
    nilai_sekarang = fungsi_objektif(konfig_sekarang)
    nilai_tetangga = fungsi_objektif(konfig_tetangga)

    print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
    print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
    konfig_sekarang.__repr__()
    print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
    konfig_tetangga.__repr__()
    print("--------------------------------------------------")

    daftar_iterasi = []

    while (restart < restart_maks and nilai_sekarang != 1000):
        daftar_nilai_konf = []
        # ====================================================================
        iterasi = 0
        while fungsi_objektif(konfig_tetangga) > fungsi_objektif(konfig_sekarang):
            konfig_sekarang = konfig_tetangga
            konfig_tetangga = cari_tetangga(konfig_sekarang)

            nilai_sekarang = fungsi_objektif(konfig_sekarang)
            nilai_tetangga = fungsi_objektif(konfig_tetangga)

            daftar_nilai_konf.append(nilai_sekarang)
            iterasi += 1

            print("Membandingkan nilai konfigurasi...")
            print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
            konfig_sekarang.__repr__()
            print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
            konfig_tetangga.__repr__()
        # ====================================================================

        daftar_calon_pemenang.append(konfig_sekarang)
        daftar_nilai.append(nilai_sekarang)
        restart += 1
        daftar_iterasi.append(iterasi)

        print("--------------------------------------------------")
        print(f"ITERASI: {iterasi}")
        konfig_sekarang.__repr__()
        print(f"Nilai Sekarang: {nilai_sekarang}")
        print("--------------------------------------------------")


    # cari pemenang sebenarnya
    nilai_pemenang = max(daftar_nilai)
    indeks_pemenang = daftar_nilai.index(nilai_pemenang)
    konfig_pemenang = daftar_calon_pemenang[indeks_pemenang]

    print("State Akhir:")
    konfig_pemenang.__repr__()
    print(f"Banyak Restart: {restart}")
    print(f"Banyak Iterasi: {daftar_iterasi}")

def hc_stochastic():
    daftar_nilai_konf = []
    probabilitas = int(input("Berapa probabilitas terjadinya pengambilan langkah jelek (dalam persen(? "))

    iterasi_maks = int(input("Iterasi maksimal? "))
    iterasi = 0

    # Membuat state awal
    konfig_sekarang = Konfigurasi()
    inisialisasi(konfig_sekarang)
    bagi_adil(konfig_sekarang)
    muat_duluan(konfig_sekarang)

    # Mencari tetangga
    konfig_tetangga = cari_tetangga(konfig_sekarang)

    # Menghitung nilai konfigurasi awal dan tetangga awal
    nilai_sekarang = fungsi_objektif(konfig_sekarang)
    nilai_tetangga = fungsi_objektif(konfig_tetangga)

    print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
    print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
    konfig_sekarang.__repr__()
    print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
    konfig_tetangga.__repr__()
    print("--------------------------------------------------")

    while (iterasi < iterasi_maks and nilai_sekarang != 1000):

        # ====================================================================

        if fungsi_objektif(konfig_tetangga) > fungsi_objektif(konfig_sekarang):
            konfig_sekarang = konfig_tetangga
            konfig_tetangga = cari_tetangga(konfig_sekarang)

        else:
            pindah = random.randint(1,100)
            if pindah <= probabilitas:
                konfig_sekarang = konfig_tetangga
                konfig_tetangga = cari_tetangga(konfig_sekarang)


        nilai_sekarang = fungsi_objektif(konfig_sekarang)
        nilai_tetangga = fungsi_objektif(konfig_tetangga)

        daftar_nilai_konf.append(nilai_sekarang)
        iterasi += 1

        print("Membandingkan nilai konfigurasi...")
        print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
        konfig_sekarang.__repr__()
        print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
        konfig_tetangga.__repr__()
        # ====================================================================
    print("State Akhir:")
    konfig_sekarang.__repr__()
    print(f"Iterasi: {iterasi}")

def sim_annealing():
    daftar_nilai_konf = []
    daftar_nilai_e = []
    t = 0

    iterasi_maks = int(input("Iterasi maksimal? "))
    iterasi = 0

    # Membuat state awal
    konfig_sekarang = Konfigurasi()
    inisialisasi(konfig_sekarang)
    bagi_adil(konfig_sekarang)
    muat_duluan(konfig_sekarang)

    # Mencari tetangga
    konfig_tetangga = cari_tetangga(konfig_sekarang)

    # Menghitung nilai konfigurasi awal dan tetangga awal
    nilai_sekarang = fungsi_objektif(konfig_sekarang)
    nilai_tetangga = fungsi_objektif(konfig_tetangga)

    print("Membandingkan nilai konfigurasi awal dengan tetangga awal...")
    print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
    konfig_sekarang.__repr__()
    print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
    konfig_tetangga.__repr__()
    print("--------------------------------------------------")

    while (iterasi < iterasi_maks and nilai_sekarang != 1000):

        # ====================================================================
        nilai_sekarang = fungsi_objektif(konfig_sekarang)
        nilai_tetangga = fungsi_objektif(konfig_tetangga)

        daftar_nilai_konf.append(nilai_sekarang)

        if fungsi_objektif(konfig_tetangga) > fungsi_objektif(konfig_sekarang):
            konfig_sekarang = konfig_tetangga
            konfig_tetangga = cari_tetangga(konfig_sekarang)

        else:
            delta_E = nilai_tetangga - nilai_sekarang
            T = 5 - (5 * t / 100)
            probabilitas = math.exp(delta_E / T)
            daftar_nilai_e.append(probabilitas)
            pindah = random.randint(1,100)
            if pindah <= probabilitas:
                konfig_sekarang = konfig_tetangga
                konfig_tetangga = cari_tetangga(konfig_sekarang)
        

        t += 1

        print("Membandingkan nilai konfigurasi...")
        print(f"Nilai Konfig Sekarang: {nilai_sekarang}")
        konfig_sekarang.__repr__()
        print(f"Nilai Konfig Tetangga: {nilai_tetangga}")
        konfig_tetangga.__repr__()
        # ====================================================================

def genetic_algorithm():
    # daftar_nilai_konf = []
    jumlah_populasi = int(input("Jumlah populasi? "))
    banyak_iterasi = int(input("Maks iterasi? "))
    probabilitas_mutasi = int(input("Probabilitas mutasi? "))

    # Membuat state awal
    konfig_awal = Konfigurasi()
    inisialisasi(konfig_awal)
    bagi_adil(konfig_awal)
    muat_duluan(konfig_awal)
    konfig_sekarang = copy.copy(konfig_awal)

    representasi_populasi = []
    # 1 - Populasi
    # buat populasi sebanyak jumlah_populasi

    template_konfig = copy.copy(konfig_sekarang)
    template_representasi = template_konfig.representasi_barang

    # buat beberapa tetangga acak, kita geser sedikit
    for i in range (jumlah_populasi):
        calon_representasi = copy.copy(template_representasi)
        indeks_ganti = random.randint(1,len(calon_representasi) - 1)
        tipe_ganti = random.randint(1,100)
        if 1 <= tipe_ganti <= 59:
            maks_ganti = template_konfig.banyak_kotak - 1
        elif 60 <= tipe_ganti <= 89:
            maks_ganti = template_konfig.banyak_kotak
        else:
            maks_ganti = template_konfig.banyak_kotak + 1

        calon_representasi[indeks_ganti] = random.randint(1, maks_ganti)
        representasi_populasi.append(calon_representasi)

    # semua tadi harus dibuat menjadi konfiguarsi
    populasi = []
    for i in range (jumlah_populasi):
        konfig = Konfigurasi()
        atur_konfig(konfig, representasi_populasi[i], template_konfig.ukuran_barang, template_konfig.kapasitas_kotak, max(representasi_populasi[i]))
        populasi.append(konfig)


    for i in range (banyak_iterasi):
        # 2 - Seleksi
        # buat wheel of fortune

        # print populasi
        # for i in range (len(populasi)):
        #     print(populasi[i].__repr__())

        daftar_nilai = []
        # print("sori")
        # print(len(populasi))
        # print(jumlah_populasi)

        for i in range (jumlah_populasi):
            konfig = populasi[i]
            nilai = fungsi_objektif(konfig)
            daftar_nilai.append(nilai)

        # print(daftar_nilai)

        # roda_seleksi = []
        # for i in range(len(daftar_nilai)):
        #     for j in range(round(daftar_nilai[i] * 10)):
        #         roda_seleksi.append(j)

        # print(roda_seleksi)

        daftar_fitness = []
        # for i in range(len(daftar_nilai)):
        #     daftar_fitness(daf)
        
        for i in range(len(daftar_nilai)):
            daftar_fitness.append(daftar_nilai[i] / sum(daftar_nilai))

        # print(daftar_nilai)
        # print(daftar_fitness)

        orangtua = []
        for i in range(len(daftar_fitness)):
            # indeks_ortu = roda_seleksi[random.randint(0, len(roda_seleksi)-1)]
            daftar_index = list(range(len(daftar_fitness)))
            indeks_ortu = random.choices(daftar_index, weights=daftar_fitness, k=1)[0]
            orangtua.append(representasi_populasi[indeks_ortu])

        # 3 - Reproduksi
        generasi_baru = []
        for i in range(len(orangtua)):
            if i < (len(orangtua)-1):
                dna_baru = []
                panjang_dna = template_konfig.banyak_barang
                tengah = random.randint(1,panjang_dna)
                dna_awal = orangtua[i][0:tengah]
                dna_akhir = orangtua[i+1][tengah:panjang_dna]
                dna_baru = dna_awal + dna_akhir

            else:
                dna_baru = []
                panjang_dna = template_konfig.banyak_barang
                tengah = random.randint(1,panjang_dna)
                dna_awal = orangtua[i][0:tengah]
                dna_akhir = orangtua[0][tengah:panjang_dna]
                dna_baru = dna_awal + dna_akhir

            generasi_baru.append(dna_baru)

        # 4 - Mutasi
        for i in range (len(generasi_baru)):
            mutasi = random.randint(0,100)
            if mutasi <= probabilitas_mutasi:
                gen_termutasi = random.randint(0, template_konfig.banyak_barang-1)
                generasi_baru[i][gen_termutasi] = random.randint(1, max(generasi_baru[i]) + 1)

        # ubah generasi baru menjadi konfigurasi dan jadikan populasi
        representasi_populasi = generasi_baru

        # print("generasi baru")
        # print(len(generasi_baru))

        populasi = []
        for i in range(len(representasi_populasi)):
            konfig = Konfigurasi()
            atur_konfig(konfig, representasi_populasi[i], template_konfig.ukuran_barang, template_konfig.kapasitas_kotak, max(representasi_populasi[i]))
            
            # print("ini konfig gagal diatur ga")
            # konfig.__repr__()

            populasi.append(konfig)

        # print("ini populasinya masuk gak")
        # print(populasi)

    print("Hasil Akhir")
    for i in range(len(populasi)):
        populasi[i].__repr__()
        print(f"Nilai fungsi objektif: {fungsi_objektif(populasi[i])}")
        


# HAPUS KOMENTAR UNTUK MENJALANKAN
# HC Steepest Ascent
# waktu_mulai = time.time()
# hc_steepest_ascent()
# waktu_selesai = time.time()
# durasi_fungsi = waktu_selesai - waktu_mulai
# print(f"Durasi Fungsi HC Steepest Ascent: {durasi_fungsi}")

# HC Sideways Move
# waktu_mulai = time.time()
# hc_sideways_move()
# waktu_selesai = time.time()
# durasi_fungsi = waktu_selesai - waktu_mulai
# print(f"Durasi Fungsi HC Sideways Move: {durasi_fungsi}")

# HC Random Restart
# waktu_mulai = time.time()
# hc_random_restart()
# waktu_selesai = time.time()
# durasi_fungsi = waktu_selesai - waktu_mulai
# print(f"Durasi Fungsi HC Random Restart: {durasi_fungsi}")

# HC Stochastic
# waktu_mulai = time.time()
# hc_stochastic()
# waktu_selesai = time.time()
# durasi_fungsi = waktu_selesai - waktu_mulai
# print(f"Durasi Fungsi HC Stochastic: {durasi_fungsi}")

# Simmulated Annealing
# waktu_mulai = time.time()
# sim_annealing()
# waktu_selesai = time.time()
# durasi_fungsi = waktu_selesai - waktu_mulai
# print(f"Durasi Fungsi Simmulated Annealing: {durasi_fungsi}")

# Genetic Algorithm
waktu_mulai = time.time()
genetic_algorithm()
waktu_selesai = time.time()
durasi_fungsi = waktu_selesai - waktu_mulai
print(f"Durasi Fungsi Genetic Algorithm: {durasi_fungsi}")