"""
A. Buatlah sebuah dictionary transaksi yang digunakan untuk menyimpan data transaksi, 
di mana key berupa bulan dan tahun (format m/yyyy) dan value berupa akumulasi transaksi pada bulan dan tahun tersebut. 
Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini.
"""


def make_dict(filename):
    # membaca file input pada parameter 'filename'
    data = open(filename).readlines()
    # melakukan instansisasi dictionary
    output = dict()
    # melakukan iterasi pada data yang telah dibaca
    for text in data:
        # melakukan split pada text
        obj = text.split(" ")
        # melakukan konversi format pada key menjadi bulan/tahun. contoh : 02/1995
        key = obj[0].split("/")
        key = f"{key[1]}/{key[2]}"
        # melakukan konversi format pada total menjadi integer
        total = int(obj[1].replace("\n", ""))
        if key in output:  # jika key berada didalam output dictionary
            # menambahkan transaksi kedalam dictionary
            output[key].append(total)
        else:  # jika key tidak ada didalam output dictionary
            # melakukan instansiasi list beserta datanya pada key tersebut
            output[key] = [total]
    # mereturn dictionary
    return output


"""
B. Buatlah fungsi terendah untuk mengembalikkan (return) 
bulan dan tahun dengan nilai transaksi paling sedikit.
"""


def fungsi_terendah(data_dict):
    # melakukan instansiasi variabel date (yang dipakai untuk nilai return)
    date = ""
    # melakukan instansiasi variabel value
    value = 0
    # melakukan interasi pada setiap data didalam data dict
    for key in data_dict:
        if date == "":  # jika variabel date kosong
            # mengassign variabel date dengan key
            date = key
            # value = jumlah transaksi pada bulan dan tahun pada key tersebut
            value = sum(data_dict[key])
        else:  # jika variable date tidak kosong
            if value > sum(
                data_dict[key]
            ):  # jika value lebih dari jumlah transaksi pada bulan dan tahun pada key tersebut
                # mengassign variable date dengan key
                date = key
                # value = jumlah transaksi pada bulan dan tahun pada key tersebut
                value = sum(data_dict[key])
    # mereturn date dengan transaksi terendah
    return date


"""
C. Buatlah fungsi report yang digunakan untuk menampilkan rata-rata 
nilai transaksi setiap bulan pada tahun tertentu.
"""


def fungsi_report(data_dict):
    # instansiasi dictionary baru untuk menampung tahun yang unik
    data = dict()
    # melakukan iterasi pada data_dict
    for key in data_dict:
        # mendapatkan tahun dari key pada index ke-i dari data_dict
        tahun = key.split("/")[1]
        # mendapatkan bulan dari key pada index ke-i dari data_dict
        bulan = key.split("/")[0]
        if tahun in data:  # jika tahun ada didalam data
            # data dengan key 'tahun' di tambahkan dengan list baru dengan format [bulan, rata rata nilai transaksi]
            data[tahun].append([bulan, sum(data_dict[key]) / len(data_dict[key])])
        else:  # jika tahun tidak terdapat didalam data
            # menginstansiasi list baru pada data dengan key 'tahun' yang berisi list dengan format [bulan, rata rata nilai transaksi]
            data[tahun] = [[bulan, sum(data_dict[key]) / len(data_dict[key])]]

    # melakukan iterasi pada data dict
    for key in data:
        # melakukan print tahun
        print(key)
        print("---------")
        # melakukan iterasi pada setiap transaksi pada tahun ke-n
        for data_transaksi in data[key]:
            # melakukan print transaksi dengan format 'bulan - jumlah transaksi'
            print(f"{data_transaksi[0]} - {data_transaksi[1]}")
        # print spasi pemisah baris
        print()


"""
D. Buatlah main program yang digunakan untuk menampilkan 
dictionary dan memanggil fungsi yang dibuat.
"""


def main():
    # memanggil fungsi untuk membaca file "text.txt" dan melakukan konversi kedalam format dictionary yang diminta
    data = make_dict("text.txt")
    # melakukan print pada variabel data
    print("A")
    print("======================================")
    print(data)
    print()

    # memanggil fungsi untuk mengambil bulan dan tahun dari nilai transaksi terendah
    bulan_terendah = fungsi_terendah(data)
    # melakukan print pada variabel bulan_terendah
    print("B")
    print("======================================")
    print(bulan_terendah)
    print()

    # memanggil fungsi dan melakukan print untuk menampilkan rata-rata nilai transaksi setiap bulan pada tahun tertentu
    print("C")
    print("======================================")
    fungsi_report(data)
    print()


if __name__ == "__main__":
    # memanggil fungsi main
    main()
