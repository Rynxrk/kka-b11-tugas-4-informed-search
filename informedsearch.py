import heapq

graf = {
    "S": {"A": 2, "B": 4},
    "A": {"C": 7},
    "B": {"D": 2},
    "C": {"G": 3},
    "D": {"G": 3},
    "G": {}
}

heuristik = {
    "S": 7,
    "A": 4,
    "B": 5,
    "C": 2,
    "D": 2,
    "G": 0
}

lokasi = {
    "S": "Kantin ITS",
    "A": "Koridor Utama",
    "B": "Taman Kampus",
    "C": "Area Parkir",
    "D": "Jalur Fakultas",
    "G": "Gedung Informatika"
}

def greedy(awal, tujuan):
    antrian = [(heuristik[awal], 0, awal, [awal])]
    dikunjungi = set()
    jumlah = 0

    while antrian:
        h, biaya, node, rute = heapq.heappop(antrian)

        if node in dikunjungi:
            continue

        dikunjungi.add(node)
        jumlah += 1

        if node == tujuan:
            return rute, biaya, jumlah

        for tetangga, jarak in graf[node].items():
            if tetangga not in dikunjungi:
                heapq.heappush(antrian, (
                    heuristik[tetangga],
                    biaya + jarak,
                    tetangga,
                    rute + [tetangga]
                ))

def astar(awal, tujuan):
    antrian = [(heuristik[awal], 0, awal, [awal])]
    terbaik = {awal: 0}
    jumlah = 0

    while antrian:
        f, biaya, node, rute = heapq.heappop(antrian)

        if biaya > terbaik[node]:
            continue

        jumlah += 1

        if node == tujuan:
            return rute, biaya, jumlah

        for tetangga, jarak in graf[node].items():
            biaya_baru = biaya + jarak

            if biaya_baru < terbaik.get(tetangga, float("inf")):
                terbaik[tetangga] = biaya_baru
                f_baru = biaya_baru + heuristik[tetangga]

                heapq.heappush(antrian, (
                    f_baru,
                    biaya_baru,
                    tetangga,
                    rute + [tetangga]
                ))

awal = "S"
tujuan = "G"

hasil_greedy = greedy(awal, tujuan)
hasil_astar = astar(awal, tujuan)

print("=== GREEDY BEST-FIRST SEARCH ===")
print("Rute:", " -> ".join(hasil_greedy[0]))
print("Total biaya:", hasil_greedy[1])
print("Node dieksplorasi:", hasil_greedy[2])

print("\n=== A* SEARCH ===")
print("Rute:", " -> ".join(hasil_astar[0]))
print("Total biaya:", hasil_astar[1])
print("Node dieksplorasi:", hasil_astar[2])

print("\n=== PERBANDINGAN ===")
selisih = hasil_greedy[1] - hasil_astar[1]
print("Selisih biaya:", selisih)
print("Penghematan A*:", round(selisih / hasil_greedy[1] * 100, 2), "%")
