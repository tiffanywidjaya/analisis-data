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

## ⚙️ Setup Environment
### Via Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Via Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Cara Menjalankan Dashboard
1. Pastikan semua library dalam `requirements.txt` sudah terinstall.
2. Jalankan perintah berikut di terminal: streamlit run dashboard/dashboard.py
3. Dashboard akan terbuka di browser secara otomatis.

## Library yang Digunakan
1. pandas 2.2.2
2. matplotlib 3.10.0
3. seaborn 0.13.2
4. streamlit 1.45.0
