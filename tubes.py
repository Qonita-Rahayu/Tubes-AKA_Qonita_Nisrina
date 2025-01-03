import time
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import matplotlib.ticker as ticker

# Untuk membaca data dari file Excel
def read_excel_data(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict('records')

# Data pasien dari Excel
file_path = r"D:/data-pasien.xlsx"
pasien = read_excel_data(file_path)

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

# Grafik dan tabel
n_values = []
iterative_times = []
recursive_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.plot(n_values, recursive_times, label='Recursive', marker='o', linestyle='-')

    plt.title('Grafik Iteratif vs Rekursif')
    plt.xlabel('Jumlah Pasien (n)')
    plt.ylabel('Execution Time (seconds)')

    # Untuk mengatur format sumbu Y
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.8f}'))

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Untuk Fungsi untuk mencetak tabel
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    for i in range(len(n_values)):
        table.add_row([n_values[i], f"{recursive_times[i]:.8f}", f"{iterative_times[i]:.8f}"])
    print(table)

# Program utama
while True:
    try:
        n = int(input("Masukkan nilai n (atau ketik -1 untuk keluar): "))
        if n == -1:
            print("Program selesai. Terima kasih!")
            break
        if n <= 0:
            print("Masukkan jumlah data yang positif!")
            continue

        # Untuk membuat dataset pasien
        extended_data = pasien * (n // len(pasien)) + pasien[:n % len(pasien)]
        n_values.append(len(extended_data))

        # Untuk input kriteria pencarian berdasarkan kelas BPJS
        target_kelas = input("Masukkan kelas BPJS yang ingin dicari (1, 2, atau 3): ").strip()
        
        # Untuk ubah input pengguna menjadi format yang sesuai dengan data
        if target_kelas == '1':
            target_kelas = "Kelas 1"
        elif target_kelas == '2':
            target_kelas = "Kelas 2"
        elif target_kelas == '3':
            target_kelas = "Kelas 3"
        else:
            print("Kelas tidak valid. Pastikan memasukkan 1, 2, atau 3.")
            continue

        # Untuk ukur waktu iteratif
        iterative_time_sum = 0
        recursive_time_sum = 0
        iterations = 100  

        for i in range(iterations):  
            start_time = time.time()
            sequential_search_iterative(extended_data, target_kelas, "Kelas")
            iterative_time_sum += (time.time() - start_time)

            start_time = time.time()
            sequential_search_recursive(extended_data, target_kelas, "Kelas")
            recursive_time_sum += (time.time() - start_time)

        iterative_times.append(iterative_time_sum / iterations)
        recursive_times.append(recursive_time_sum / iterations)

        # Untuk mencetak tabel hasil
        print_execution_table()

        # Untuk memperbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan input yang valid!")