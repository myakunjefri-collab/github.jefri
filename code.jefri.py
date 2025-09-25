import json
import csv

# Path file JSON dan CSV
json_file = "Jefri Nur Cholis Hidayat_V3925026.json"
csv_file = "Data_Demonstrasi.csv"

# Baca file JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil key utama (karena di JSON kamu ada 1 key besar)
key = list(data.keys())[0]
records = data[key]

# Tulis ke file CSV
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print(f"Data berhasil disimpan ke {csv_file}")
