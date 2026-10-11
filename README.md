# kka-b11-tugas-4-informed-search

| No | Nama | NRP |
| :--: | :--- | :--- |
| 1 | Maulana Bagas Rizqi Pratama | 5025251248 |
| 2 | Daffa Arya Satyatma | 5025251269 |
| 3 | Raka Rajendra Dipo Alam | 5025251272 |

# Implementasi dan Analisis Algoritma Informed Search pada Robot Pengantar Makanan di Kampus ITS

**Algoritma:** Greedy Best-First Search dan A* Search  
**Studi Kasus:** Optimasi rute robot pengantar makanan di lingkungan kampus ITS  
**Bahasa Pemrograman:** Python

## 1. Deskripsi Masalah

- Robot bertugas mengantarkan makanan dari Kantin ITS menuju Gedung Informatika.
- Setiap jalur memiliki biaya perjalanan yang berbeda, bergantung pada jarak dan tingkat hambatannya.
- Robot perlu menentukan rute yang paling efisien agar total biaya perjalanan seminimal mungkin.
- Dua algoritma Informed Search yang digunakan:
  - **Greedy Best-First Search:** Memilih jalur berdasarkan perkiraan biaya menuju tujuan menggunakan heuristik `h(n)`.
  - **A* Search:** Memilih jalur berdasarkan biaya yang sudah ditempuh `g(n)` dan perkiraan biaya menuju tujuan `h(n)`.
- Kedua algoritma dibandingkan berdasarkan rute yang ditemukan, total biaya, dan jumlah node yang dieksplorasi.
- Seluruh lokasi, jalur, dan biaya yang digunakan merupakan simulasi untuk pembelajaran, bukan data pengukuran sebenarnya di ITS.

## 2. Representasi Graf

- Graf digunakan untuk merepresentasikan lokasi dan jalur yang dapat dilewati robot.
- Terdapat enam node yang mewakili lokasi perjalanan:
  - **S:** Kantin ITS sebagai titik awal.
  - **A:** Koridor Utama sebagai jalur relatif dekat.
  - **B:** Taman Kampus sebagai jalur alternatif.
  - **C:** Area Parkir sebagai jalur dengan hambatan.
  - **D:** Jalur Fakultas sebagai jalur yang lebih lancar.
  - **G:** Gedung Informatika sebagai titik tujuan.
- Graf yang digunakan merupakan graf berarah, sehingga setiap jalur menunjukkan arah perpindahan dari satu node ke node berikutnya.

### Biaya Perjalanan Antar-Node

| Dari | Ke | Biaya |
|---|---|---:|
| S | A | 2 |
| S | B | 4 |
| A | C | 7 |
| B | D | 2 |
| C | G | 3 |
| D | G | 3 |

- Biaya merepresentasikan gabungan jarak dan tingkat hambatan perjalanan.
- Semakin kecil biaya suatu jalur, semakin efisien jalur tersebut dalam simulasi.

## 3. Nilai Heuristik

- Heuristik `h(n)` merupakan perkiraan biaya yang diperlukan untuk mencapai Gedung Informatika dari suatu node.
- Nilai heuristik digunakan untuk membantu algoritma menentukan node yang perlu diprioritaskan.

| Node | Nilai Heuristik |
|---|---:|
| S | 7 |
| A | 4 |
| B | 5 |
| C | 2 |
| D | 2 |
| G | 0 |

- Node tujuan `G` memiliki nilai heuristik 0 karena robot sudah mencapai tujuan.
- Heuristik yang digunakan bersifat **admissible**, yaitu tidak melebihi biaya minimum sebenarnya menuju tujuan.
- Sifat tersebut mendukung A* dalam menemukan rute optimal pada graf simulasi ini.

## 4. Rumus Algoritma

### Greedy Best-First Search

- Menggunakan fungsi evaluasi:

  `f(n) = h(n)`

- Algoritma memilih node dengan nilai heuristik terkecil.
- Biaya perjalanan yang telah ditempuh tidak menjadi pertimbangan dalam menentukan prioritas node.
- Kelebihannya adalah dapat mencapai tujuan dengan eksplorasi yang lebih sedikit pada kasus tertentu.
- Kekurangannya adalah rute yang ditemukan belum tentu memiliki biaya total paling rendah.

### A* Search

- Menggunakan fungsi evaluasi:

  `f(n) = g(n) + h(n)`

- Keterangan:
  - `g(n)`: Total biaya perjalanan dari titik awal ke node saat ini.
  - `h(n)`: Perkiraan biaya perjalanan dari node saat ini menuju tujuan.
  - `f(n)`: Perkiraan total biaya perjalanan melalui node tersebut.
- A* mempertimbangkan biaya yang sudah dikeluarkan sekaligus perkiraan biaya menuju tujuan.
- Dengan heuristik admissible dan kondisi pencarian yang sesuai, A* dapat menemukan rute optimal.

### Perbedaan Utama

- **Greedy Best-First Search:** Memprioritaskan perkiraan kedekatan dengan tujuan.
- **A* Search:** Memprioritaskan gabungan biaya perjalanan yang sudah ditempuh dan perkiraan biaya menuju tujuan.

## 5. Implementasi Program Python

- Program menggunakan library `heapq` untuk membuat *priority queue*, sehingga node dengan prioritas terkecil diproses terlebih dahulu.
- Variabel `graf` menyimpan hubungan antar-node beserta biaya perjalanan pada setiap jalur, `heuristik` menyimpan perkiraan biaya menuju tujuan, dan `lokasi` menyimpan nama lokasi berdasarkan kode node.
- Fungsi `greedy(awal, tujuan)` menjalankan algoritma Greedy Best-First Search dengan memilih node berdasarkan nilai heuristik terkecil. Fungsi ini mencatat node yang telah dikunjungi, total biaya perjalanan, dan jumlah node yang dieksplorasi.
- Fungsi `astar(awal, tujuan)` menjalankan algoritma A* Search dengan mempertimbangkan biaya perjalanan yang telah ditempuh dan perkiraan biaya menuju tujuan. Variabel `terbaik` digunakan untuk menyimpan biaya perjalanan terbaik yang diketahui pada setiap node.
- **Alur kerja program:** Program memuat data graf dan heuristik, kemudian menjalankan algoritma Greedy dan A* dari node awal `S` menuju node tujuan `G`. Setiap algoritma memasukkan node ke dalam *priority queue*, memilih node dengan prioritas terkecil, lalu memeriksa tetangganya dan memperbarui informasi rute serta biaya perjalanan. Proses berulang sampai tujuan ditemukan. Setelah itu, program menampilkan rute yang diperoleh, total biaya perjalanan, dan jumlah node yang dieksplorasi untuk membandingkan hasil kedua algoritma.

## 6. Hasil Pengujian

Berdasarkan eksekusi algoritma pada graf simulasi, diperoleh hasil sebagai berikut.

### Output Program

```text
=== GREEDY BEST-FIRST SEARCH ===
Rute: S -> A -> C -> G
Total biaya: 12
Node dieksplorasi: 4

=== A* SEARCH ===
Rute: S -> B -> D -> G
Total biaya: 9
Node dieksplorasi: 5

=== PERBANDINGAN ===
Selisih biaya: 3
Penghematan A*: 25.0%
```

### Visualisasi Hasil Rute

![image alt](https://github.com/Rynxrk/kka-b11-tugas-4-informed-search/blob/c536f802f6d0eaa3e704dd0441c5794bc44d98a6/source%20image/Graf%20GBFS.jpeg)

| Algoritma | Rute | Total Biaya |
|---|---|---:|
| Greedy Best-First Search | S → A → C → G | 12 |

![image alt](https://github.com/Rynxrk/kka-b11-tugas-4-informed-search/blob/c536f802f6d0eaa3e704dd0441c5794bc44d98a6/source%20image/Graf%20A%20star.jpeg)

| Algoritma | Rute | Total Biaya |
|---|---|---:|
| A* Search | S → B → D → G | 9 |

Keterangan:
- **S**: Kantin ITS
- **A**: Koridor Utama
- **B**: Taman Kampus
- **C**: Area Parkir
- **D**: Jalur Fakultas
- **G**: Gedung Informatika

## 7. Analisis Proses Pencarian

### 7.1 Greedy Best-First Search

Greedy Best-First Search menentukan node berikutnya berdasarkan nilai heuristik terkecil, yaitu `h(n)`, tanpa mempertimbangkan biaya perjalanan yang telah ditempuh.

Urutan node yang dieksplorasi:

`S → A → C → G`

Proses pencarian:

1. Dari node S, algoritma membandingkan A dengan `h(A) = 4` dan B dengan `h(B) = 5`. Algoritma memilih A karena memiliki nilai heuristik lebih kecil.
2. Dari A, ditemukan node C dengan `h(C) = 2`.
3. Dari C, ditemukan node G dengan `h(G) = 0`.
4. Karena G merupakan tujuan, proses pencarian dihentikan.

Total biaya perjalanan:

\[
2 + 7 + 3 = 12
\]

Greedy Best-First Search mengeksplorasi empat node. Meskipun berhasil menemukan tujuan dengan jumlah eksplorasi yang lebih sedikit, algoritma ini menghasilkan rute dengan biaya lebih tinggi karena tidak mempertimbangkan biaya perjalanan sebelumnya dalam fungsi evaluasinya.

### 7.2 A* Search

A* Search menentukan prioritas node menggunakan fungsi evaluasi:

\[
f(n) = g(n) + h(n)
\]

Dengan demikian, algoritma mempertimbangkan biaya perjalanan yang telah ditempuh serta perkiraan biaya menuju tujuan.

Berikut perhitungan nilai evaluasi node berdasarkan proses pencarian:

| Langkah | Node | `g(n)` | `h(n)` | `f(n)` |
|---:|---|---:|---:|---:|
| 1 | S | 0 | 7 | 7 |
| 2 | A | 2 | 4 | 6 |
| 3 | B | 4 | 5 | 9 |
| 4 | D | 6 | 2 | 8 |
| 5 | G | 9 | 0 | 9 |

Proses pencarian:

1. Dari S, algoritma mengevaluasi A dengan `f(A) = 6` dan B dengan `f(B) = 9`, sehingga A diproses terlebih dahulu.
2. Dari A, ditemukan C dengan `g(C) = 9`, `h(C) = 2`, dan `f(C) = 11`.
3. Node B kemudian diproses karena memiliki nilai prioritas lebih kecil daripada C.
4. Dari B, ditemukan D dengan `g(D) = 6`, `h(D) = 2`, dan `f(D) = 8`.
5. Dari D, ditemukan G dengan `g(G) = 9` dan `f(G) = 9`.
6. Karena G telah dikeluarkan dari priority queue sebagai node dengan nilai evaluasi minimum, pencarian dihentikan.

Urutan node yang dieksplorasi:

`S → A → B → D → G`

Rute solusi:

`S → B → D → G`

Total biaya perjalanan:

\[
4 + 2 + 3 = 9
\]

A* Search mengeksplorasi lima node dan menghasilkan rute dengan biaya lebih rendah dibandingkan Greedy Best-First Search. Node C telah ditemukan selama proses pencarian, tetapi tidak dieksplorasi karena terdapat alternatif dengan nilai evaluasi lebih kecil.

## 8. Analisis Perbandingan Hasil

### Perbandingan Algoritma

| Aspek | Greedy Best-First Search | A* Search |
|---|---|---|
| Fungsi evaluasi | `h(n)` | `g(n) + h(n)` |
| Rute | S → A → C → G | S → B → D → G |
| Total biaya | 12 | 9 |
| Node dieksplorasi | 4 | 5 |
| Optimal pada kasus ini | Tidak | Ya |
| Karakteristik | Memprioritaskan estimasi biaya menuju tujuan | Mempertimbangkan biaya aktual dan estimasi biaya menuju tujuan |

### Perbandingan Total Biaya Perjalanan

```text
Greedy Best-First Search | █ █ █ █ █ █ █ █ █ █ █ █ 12
A* Search                | █ █ █ █ █ █ █ █ █     9
```

Semakin rendah total biaya, semakin efisien rute yang dihasilkan.

Berdasarkan hasil pengujian, Greedy Best-First Search mengeksplorasi lebih sedikit node dibandingkan A*. Namun, Greedy menghasilkan rute dengan total biaya 12, sedangkan A* menghasilkan rute dengan total biaya 9.

Selisih biaya perjalanan:

\[
12 - 9 = 3
\]

Persentase penghematan biaya menggunakan A* dibandingkan Greedy:

$$
\frac{12-9}{12}\times100\% = 25\%
$$

Dengan demikian, A* menghasilkan penghematan biaya perjalanan sebesar **25%** dibandingkan Greedy pada studi kasus ini.

Hasil tersebut menunjukkan bahwa jumlah node yang dieksplorasi lebih sedikit tidak selalu menghasilkan rute dengan biaya paling rendah. Greedy lebih mengutamakan kedekatan terhadap tujuan berdasarkan heuristik, sedangkan A* mempertimbangkan biaya perjalanan secara keseluruhan.

Perlu diperhatikan bahwa jumlah node yang dieksplorasi bukan pengukuran langsung waktu eksekusi. Selain itu, jaminan optimalitas A* bergantung pada sifat heuristik, representasi graf, dan implementasi algoritma.

## 9. Kesimpulan

Berdasarkan implementasi kedua algoritma Informed Search pada studi kasus robot pengantar makanan di kampus ITS, Greedy Best-First Search menghasilkan rute `S → A → C → G` dengan total biaya 12 dan mengeksplorasi empat node. Sementara itu, A* Search menghasilkan rute `S → B → D → G` dengan total biaya 9 dan mengeksplorasi lima node.

A* menghasilkan biaya perjalanan 25% lebih rendah dibandingkan Greedy. Hal ini menunjukkan bahwa A* lebih sesuai untuk kasus optimasi rute robot pengantar makanan ketika tujuan utamanya adalah meminimalkan biaya perjalanan.

Dengan demikian, A* Search menjadi algoritma yang lebih efektif pada studi kasus ini karena mampu menemukan rute optimal, meskipun memerlukan eksplorasi node yang sedikit lebih banyak.

## 10. Catatan Validasi dan Pengembangan

Graf dan nilai heuristik yang digunakan dirancang untuk memperlihatkan perbedaan hasil kedua algoritma.

Nilai heuristik awal bersifat *admissible*, yaitu tidak melebihi biaya optimal sebenarnya menuju tujuan. Namun, heuristik tersebut belum seluruhnya memenuhi sifat *consistent heuristic*.

Untuk menggunakan heuristik yang juga konsisten, nilai berikut dapat diubah:

```python
heuristik = {
    "S": 6,
    "A": 4,
    "B": 4,
    "C": 2,
    "D": 2,
    "G": 0
}
```

Perubahan tersebut mempertahankan sifat admissible dan membuat heuristik konsisten pada graf yang digunakan. Namun, hasil eksplorasi dan output program perlu diuji kembali setelah perubahan dilakukan.

Untuk pengembangan selanjutnya, beberapa hal yang dapat dilakukan adalah:

- Menambahkan visualisasi graf untuk memperjelas jalur yang dipilih setiap algoritma.
- Menggunakan data jarak dan hambatan perjalanan yang lebih realistis.
- Membandingkan waktu eksekusi selain jumlah node yang dieksplorasi.
- Menguji algoritma pada graf dengan jumlah node dan jalur yang lebih besar.
- Mengevaluasi pengaruh nilai heuristik terhadap efisiensi pencarian.
