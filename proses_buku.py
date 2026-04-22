# proses_buku.py

def total_halaman(daftar_buku):
    total = 0

    for buku in daftar_buku:
        total += buku["halaman"]

    return total


def buku_terbanyak(daftar_buku):
    terbanyak = daftar_buku[0]

    for buku in daftar_buku:
        if buku["halaman"] > terbanyak["halaman"]:
            terbanyak = buku

    return terbanyak


def rata_rata_halaman(daftar_buku):
    total = total_halaman(daftar_buku)
    return total / len(daftar_buku)
