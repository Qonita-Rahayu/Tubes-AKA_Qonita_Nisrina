# Tugas Akhir: Analisis Kompleksitas Algoritma

## Anggota Kelompok:
- **Qonita Rahayu Atmi** (2311102128)
- **Nisrina Amalia Iffatunnisa** (2311102156)

---

## Perbandingan 

Program ini membandingkan waktu eksekusi untuk mencari kelas BPJS menggunakan dua metode **Sequential Search** yaitu **iteratif** dan **rekursif**. Pengguna dapat memasukkan jumlah pasien (`n`) dan kelas BPJS yang ingin dicari (kelas 1, 2, atau 3). Program akan menampilkan hasilnya dalam bentuk tabel dan grafik yang menunjukkan perbandingan waktu eksekusi. 

## Fitur Utama
- Implementasi algoritma **Sequential Search** menggunakan **iteratif** dan **rekursif**.
- Pengguna diminta untuk memasukkan jumlah pasien (n) dan kelas BPJS yang ingin dicari (kelas 1, 2, atau 3).
- Kemudian, program akan menampilkan data perbandingannya ke dalam tabel.
- Setelah, ditambilkan tabelnya program akan membentuknya ke dalam grafik perbanfingan iteratif vs rekursif.

```python
# Fungsi untuk Sequential Search Iteratif
def sequential_search_iterative(data, target_kelas, key):
    for i in data:
        if str(i[key]) == str(target_kelas):  
            return i
    return None

# Fungsi untuk Sequential Search Rekursif
def sequential_search_recursive(data, target_kelas, key, index=0):
    if index >= len(data):
        return None
    if str(data[index][key]) == str(target_kelas): 
        return data[index]
    return sequential_search_recursive(data, target_kelas, key, index + 1)
```

## Output Terminal
![Grafik1](assets\Grafik1.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 5
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 1
+---+--------------------+--------------------+
| n | Recursive Time (s) | Iterative Time (s) |
+---+--------------------+--------------------+
| 5 |     0.00000834     |     0.00001478     |
+---+--------------------+--------------------+

```
## Output Grafik
![Output Grafik1](assets\Grafik1.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 10
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 2
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000834     |     0.00001478     |
| 10 |     0.00001264     |     0.00001597     |
+----+--------------------+--------------------+

```
## Output Grafik
![Output Grafik2](assets\Grafik2.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 15
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 1
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000834     |     0.00001478     |
| 10 |     0.00001264     |     0.00001597     |
| 15 |     0.00000525     |     0.00001097     |
+----+--------------------+--------------------+
```
## Output Grafik
![Output Grafik3](assets\Grafik3.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 20
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 3
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000834     |     0.00001478     |
| 10 |     0.00001264     |     0.00001597     |
| 15 |     0.00000525     |     0.00001097     |
| 20 |     0.00001287     |     0.00001979     |
+----+--------------------+--------------------+
```
## Output Grafik
![output Grafik4](assets\Grafik4.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 25
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 2
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000954     |     0.00001764     |
| 10 |     0.00000644     |     0.00001144     |
| 15 |     0.00000548     |     0.00001144     |
| 20 |     0.00001335     |     0.00001955     |
| 25 |     0.00000715     |     0.00001168     |
+----+--------------------+--------------------+
```
## Output Grafik
![Output Grafik5](assets\Grafik5.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 30
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 1
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000954     |     0.00001764     |
| 10 |     0.00000644     |     0.00001144     |
| 15 |     0.00000548     |     0.00001144     |
| 20 |     0.00001335     |     0.00001955     |
| 25 |     0.00000501     |     0.00001001     |
| 30 |     0.00000548     |     0.00001216     |
+----+--------------------+--------------------+

```
## Output Grafik
![Output Grafik6](assets\Grafik6.png)

```plaintext

Program selesai!
```


