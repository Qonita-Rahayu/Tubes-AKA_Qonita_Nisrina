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

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 5
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 1
+---+--------------------+--------------------+
| n | Recursive Time (s) | Iterative Time (s) |
+---+--------------------+--------------------+
| 5 |     0.00000067     |     0.00000072     |
+---+--------------------+--------------------+

```
## Output Grafik
![Output Grafik1](https://github.com/Qonita-Rahayu/Tubes-AKA_Qonita_Nisrina/blob/main/assets/Grafik1.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 10
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 2
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000067     |     0.00000072     |
| 10 |     0.00000161     |     0.00000145     |
+----+--------------------+--------------------+

```
## Output Grafik
![Output Grafik2](https://github.com/Qonita-Rahayu/Tubes-AKA_Qonita_Nisrina/blob/main/assets/Grafik2.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 20
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 2
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000067     |     0.00000072     |
| 10 |     0.00000161     |     0.00000145     |
| 20 |     0.00000221     |     0.00000144     |
+----+--------------------+--------------------+
```
## Output Grafik
![Output Grafik3](https://github.com/Qonita-Rahayu/Tubes-AKA_Qonita_Nisrina/blob/main/assets/Grafik3.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 25
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 3
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000067     |     0.00000072     |
| 10 |     0.00000161     |     0.00000145     |
| 20 |     0.00000221     |     0.00000144     |
| 25 |     0.00000081     |     0.00000063     |
+----+--------------------+--------------------+
```
## Output Grafik
![output Grafik4](https://github.com/Qonita-Rahayu/Tubes-AKA_Qonita_Nisrina/blob/main/assets/Grafik4.png)

```plaintext
Masukkan nilai n (atau ketik -1 untuk keluar): 30
Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): 2
+----+--------------------+--------------------+
| n  | Recursive Time (s) | Iterative Time (s) |
+----+--------------------+--------------------+
| 5  |     0.00000067     |     0.00000072     |
| 10 |     0.00000161     |     0.00000145     |
| 20 |     0.00000221     |     0.00000144     |
| 25 |     0.00000081     |     0.00000063     |
| 30 |     0.00000091     |     0.00000074     |
+----+--------------------+--------------------+
```
## Output Grafik
![Output Grafik5](https://github.com/Qonita-Rahayu/Tubes-AKA_Qonita_Nisrina/blob/main/assets/Grafik5.png)

```plaintext
Program selesai!
```


