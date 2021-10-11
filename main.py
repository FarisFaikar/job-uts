def soal_1():
    while True:
        print("--- Soal 1 ---")
        print("Program perhitungan perkalian dan pembagian")
        angka_1 = int(input("Masukkan angka pertama: "))
        angka_2 = int(input("Masukkan angka kedua: "))
        hasil_kali = angka_1 * angka_2
        hasil_bagi = angka_1 / angka_2
        print(f"Hasil kali kedua angka tersebut adalah: {hasil_kali}")
        print(f"Hasil bagi kedua angka tersebut adalah: {hasil_bagi}")

        jawaban = input("Apakah anda ingin mengulangi kalkulasi? [y]: ")
        if jawaban.lower() == 'y':
            print("Program diulang")
            continue
        else:
            print("Program selesai")
            break


def kalkulasi_hasil(umur, jenis_kelamin, hasil_tes_1, hasil_tes_2):
    skor_tes_1 = 0
    skor_tes_2 = 0

    if 20 <= umur <= 30:
        # Kalkulasi skor tes 1
        if jenis_kelamin == 'lelaki':
            if 38 <= hasil_tes_1 <= 40:
                skor_tes_1 = 3
            elif 35 < hasil_tes_1 <= 37:
                skor_tes_1 = 2
            elif hasil_tes_1 <= 35:
                skor_tes_1 = 1
            else:
                print(f"ERROR -- Hasil tes 1 {jenis_kelamin} luar jangkauan")
        elif jenis_kelamin == 'perempuan':
            if 34 <= hasil_tes_1 <= 36:
                skor_tes_1 = 3
            elif 32 <= hasil_tes_1 <= 34:
                skor_tes_1 = 2
            elif hasil_tes_1 <= 31:
                skor_tes_1 = 1
            else:
                print(f"ERROR -- Hasil tes 1 {jenis_kelamin} luar jangkauan")
        else:
            print("ERROR -- Jenis kelamin tidak valid")

        # Kalkulasi skor tes 2
        if jenis_kelamin == 'lelaki':
            if 14 <= hasil_tes_2 <= 16:
                skor_tes_2 = 3
            elif 11 < hasil_tes_2 <= 13:
                skor_tes_2 = 2
            elif hasil_tes_2 <= 11:
                skor_tes_2 = 1
            else:
                print(f"ERROR -- Hasil tes 2 {jenis_kelamin} luar jangkauan")
        elif jenis_kelamin == 'perempuan':
            if 10 < hasil_tes_2 <= 13:
                skor_tes_2 = 3
            elif 8 <= hasil_tes_2 <= 10:
                skor_tes_2 = 2
            elif hasil_tes_2 < 8:
                skor_tes_2 = 1
            else:
                print(f"ERROR -- Hasil tes 2 {jenis_kelamin} luar jangkauan")
        else:
            print("ERROR -- Jenis kelamin tidak valid")

    elif 31 <= umur <= 40:
        # Kalkulasi skor tes 1
        if jenis_kelamin == 'lelaki':
            if 35 < hasil_tes_1 <= 37:
                skor_tes_1 = 3
            elif 32 < hasil_tes_1 <= 35:
                skor_tes_1 = 2
            elif 30 <= hasil_tes_1 <= 32:
                skor_tes_1 = 1
            else:
                print(f"ERROR -- Hasil tes 1 {jenis_kelamin} luar jangkauan")
        elif jenis_kelamin == 'perempuan':
            if 30 < hasil_tes_1 <= 32:
                skor_tes_1 = 3
            elif 28 <= hasil_tes_1 <= 30:
                skor_tes_1 = 2
            elif hasil_tes_1 < 28:
                skor_tes_1 = 1
            else:
                print(f"ERROR -- Hasil tes 1 {jenis_kelamin} luar jangkauan")
        else:
            print("ERROR -- Jenis kelamin tidak valid")

        # Kalkulasi skor tes 2
        if jenis_kelamin == 'lelaki':
            if 28 <= hasil_tes_2 <= 30:
                skor_tes_2 = 3
            elif 25 < hasil_tes_2 <= 27:
                skor_tes_2 = 2
            elif hasil_tes_2 < 25:
                skor_tes_2 = 1
            else:
                print(f"ERROR -- Hasil tes 2 {jenis_kelamin} luar jangkauan")
        elif jenis_kelamin == 'perempuan':
            if 22 < hasil_tes_2 <= 24:
                skor_tes_2 = 3
            elif 20 <= hasil_tes_2 <= 22:
                skor_tes_2 = 2
            elif hasil_tes_2 < 20:
                skor_tes_2 = 1
            else:
                print(f"ERROR -- Hasil tes 2 {jenis_kelamin} luar jangkauan")
        else:
            print("ERROR -- Jenis kelamin tidak valid")

    else:
        print("ERROR -- Umur anda di luar jangkauan")

    hasil = (skor_tes_1 + skor_tes_2) / 2
    return hasil


def kalkulasi_keterangan(hasil):
    if hasil >= 2.5:
        keterangan = 'Sangat Bugar'
    elif hasil >= 2:
        keterangan = 'Cukup Bugar'
    elif hasil >= 1:
        keterangan = 'Kurang Bugar'
    else:
        keterangan = 'Keterangan di luar jangkauan'
        print("ERROR -- Hasil di luar jangkauan")

    return keterangan


def soal_2():
    print("--- Soal 2 ---")
    # Tampilan Masukan/Input
    umur = int(input("Masukkan Umur Anda: "))
    jenis_kelamin = input("Masukkan Jenis Kelamin Anda [lelaki/perempuan]: ")
    hasil_tes_1 = int(input("Hasil Tes 1: "))
    hasil_tes_2 = int(input("Hasil Tes 2: "))

    # Kalkulasi
    print("")
    print("--- Output ---")

    hasil = kalkulasi_hasil(umur, jenis_kelamin, hasil_tes_1, hasil_tes_2)
    keterangan = kalkulasi_keterangan(hasil)

    # Tampilan Keluaran/Output
    print(f"Umur Anda Adalah: {umur}")
    print(f"Jenis Kelamin Anda Adalah: {jenis_kelamin}")
    print(f"Tingkat Kebugaran Anda adalah: {hasil} {keterangan}")


def test_soal_2():
    orang = {
        0: {'umur': 20, 'jenis kelamin': 'lelaki', 'hasil tes 1': 40, 'hasil tes 2': 16},
        1: {'umur': 20, 'jenis kelamin': 'lelaki', 'hasil tes 1': 35, 'hasil tes 2': 11},
        2: {'umur': 20, 'jenis kelamin': 'perempuan', 'hasil tes 1': 36, 'hasil tes 2': 13},
        3: {'umur': 20, 'jenis kelamin': 'perempuan', 'hasil tes 1': 31, 'hasil tes 2': 8},
        4: {'umur': 40, 'jenis kelamin': 'lelaki', 'hasil tes 1': 37, 'hasil tes 2': 30},
        5: {'umur': 40, 'jenis kelamin': 'lelaki', 'hasil tes 1': 30, 'hasil tes 2': 25},
        6: {'umur': 40, 'jenis kelamin': 'perempuan', 'hasil tes 1': 32, 'hasil tes 2': 24},
        7: {'umur': 40, 'jenis kelamin': 'perempuan', 'hasil tes 1': 28, 'hasil tes 2': 20}
    }

    for i in range(len(orang)):
        # Input
        umur = orang[i]['umur']
        jenis_kelamin = orang[i]['jenis kelamin']
        hasil_tes_1 = orang[i]['hasil tes 1']
        hasil_tes_2 = orang[i]['hasil tes 2']

        # Tampilan Keluaran/Output
        print("")
        print(f"--- Output: #{i} ---")
        hasil = kalkulasi_hasil(umur, jenis_kelamin, hasil_tes_1, hasil_tes_2)
        keterangan = kalkulasi_keterangan(hasil)

        print(f"Umur Anda Adalah: {umur}")
        print(f"Jenis Kelamin Anda Adalah: {jenis_kelamin}")
        print(f"Hasil Tes 1 Adalah: {hasil_tes_1}")
        print(f"Hasil Tes 2 Adalah: {hasil_tes_2}")
        print(f"Tingkat Kebugaran Anda adalah: {hasil} {keterangan}")

    # Hasil test_soal_2:
    """
    Terdapat masalah pada pernyataan, "Pada kolom E Akan mendapat skor 2 pada laki-laki jika nilainya > 25 s.d <= 27'
    dan "Pada kolom E Akan mendapat skor 1 pada laki-laki jika nilainya < 25" karena
    jika usia 31-40 dan hasil_tes_2 diinput 25, maka kedua pernyataan tersebut tidak tereksekusi
    sehingga algoritma menganggap bahwa hasil_tes_2 di luar jangkauan.
    Solusinya adalah mengganti salah satu pernyataan menjadi >= 25 atau <= 25.
    """


def main():
    # soal_1()
    # soal_2()
    test_soal_2()


if __name__ == '__main__':
    main()
