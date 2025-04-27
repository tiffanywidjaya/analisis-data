# Bike Sharing Analysis Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda harian dan per jam.  
Analisis dilakukan menggunakan Python (pandas, seaborn, matplotlib) dan dashboard interaktif dibangun dengan Streamlit.

## Struktur File
- `notebook.ipynb` — Notebook berisi proses eksplorasi data dan insight.
- `dashboard/dashboard.py` — Dashboard Streamlit untuk visualisasi interaktif.
- `dashboard/day.csv` — Dataset penyewaan sepeda harian.
- `dashboard/hour.csv` — Dataset penyewaan sepeda per jam.
- `requirements.txt` — Daftar library yang dibutuhkan.

## Cara Menjalankan Dashboard
1. Pastikan semua library dalam `requirements.txt` sudah terinstall.
2. Jalankan perintah berikut di terminal: streamlit run dashboard/dashboard.py
3. Dashboard akan terbuka di browser secara otomatis.

## Library yang Digunakan
- pandas
- matplotlib
- seaborn
- streamlit

## Insight Singkat
- Jumlah penyewaan sepeda meningkat di musim panas.
- Pola penyewaan berbeda antara hari kerja dan hari libur, dengan puncak sewa terjadi pagi dan sore pada hari kerja, serta siang hari pada hari libur.
