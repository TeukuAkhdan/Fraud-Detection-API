# Machine Learning Fraud Detection
Problems
Perusahaan harus mengadopsi strategi dan teknologi yang canggih untuk secara proaktif mengurangi, mencegah, dan menanggulangi kerugian finansial yang disebabkan oleh penipuan transaksi. Dengan mengimplementasikan sistem deteksi dini yang efektif, pelatihan yang komprehensif bagi staf terkait, serta kerangka kerja keamanan yang ketat, perusahaan bertujuan untuk meminimalkan dampak keuangan dari segala jenis aktivitas penipuan yang terjadi dalam transaksi.

Selain itu, perusahaan juga harus mengembangkan pendekatan yang seimbang antara keamanan dan kenyamanan pengguna dalam menghadapi aktivitas penipuan. Langkah-langkah yang diambil untuk mendeteksi dan mencegah penipuan haruslah terintegrasi secara halus ke dalam pengalaman pengguna, tanpa mengurangi kemudahan atau memberikan gangguan yang berarti.


Architecture
Poryek ini berfokus pada Fraud Detection menggunakan Machine Learning. Berikut adalah langkah-langkah utama yang dikerjakan:
## Config
mengatur parameter, path, dan konfigurasi penting lainnya dalam proyek ini.

## Models
file-file pkl yang sudah di serialisasikan dari masing masing model machine learning dari training sampai ke tuning.

## src
bagian utama dalam proyek ini, memuat semua kode yang berperan dalam fungsionalitas dan pengoperasian proyek ini.

### 1. 'helper.py
Code yang berisi fungsi-fungsi yang di butuhkan.

### 2. 'training.py'
Pada tahap ini, dilakukan pengembangan model machine learning untuk deteksi penipuan. Langkah-langkahnya antara lain:
- Menyiapkan dengan mendownload data dari google drive dengan size sebesar 470.7 MB.
- Membagi data menjadi set pelatihan (train), validasi (val), dan pengujian (testing).
- Melakukan preprocessing data, seperti One-Hot Encoding (OHE).
- Melatih model menggunakan algoritma XGBoost.
- Mencari parameter optimal menggunakan teknik random search.
- Setelah mendapatkan parameter optimal, model disimpan ke dalam file pkl (pickle).

### 3. `main.py`

File ini menggunakan FastAPI untuk membangun layanan deteksi penipuan. Langkah-langkahnya mencakup:
- Memanfaatkan model XGBoost yang telah diserialisasikan dari model terbaik.
- Menerima fitur-fitur sebagai input sesuai dengan data pelatihan.
- Proses input data termasuk OHE dan prediksi berdasarkan fitur yang sudah bersih.
- Menghitung probabilitas hasil prediksi.

### 4. `app.py`

File ini bertanggung jawab untuk menampilkan hasil prediksi melalui antarmuka Streamlit yang terhubung ke API FastAPI (`API_URL`).

## Pyhton notebook files
Eksperimentasi dari hasil eksplorasi data 

## requirement.txt
Library dependencies yang diperlukan untuk menjalankan code python.

Rincian dan dataset dapat diunduh pada link dibawah ini.
- data: https://www.kaggle.com/datasets/ealaxi/paysim1
- Artikel: https://medium.com/@akhdansyah/machine-learning-fraud-detection-0e10308b9ee1

# Proyek Workflow
# Menjalankan Proyek dengan Docker

Untuk menjalankan proyek menggunakan Docker, ikuti langkah-langkah di bawah ini:

## Langkah-langkah

1. **Membangun Image Docker:**
   - Pastikan Docker telah terinstal di komputer Anda.
   - Buka terminal/cmd, masuk ke dalam direktori proyek yang berisi Dockerfile.
   - Jalankan perintah untuk membangun image Docker:
     ```
     docker build -t nama_image .
     ```
     Gantilah `nama_image` dengan nama yang ingin Anda berikan pada image Docker.

2. **Menjalankan Container:**
   Setelah berhasil membangun image Docker, jalankan container dengan perintah:

Perintah ini akan menjalankan container dari image yang telah dibuat sebelumnya. Opsi `-p` digunakan untuk memetakan port dari container ke port lokal komputer Anda.

3. **Akses Proyek:**
- Setelah container berjalan, API akan dapat diakses melalui `http://localhost:8000`.
- Aplikasi Streamlit akan dapat diakses melalui web browser pada `http://localhost:8501`.

Pastikan untuk mengganti `nama_image` dengan nama yang relevan atau sesuai dengan keinginan Anda. Langkah-langkah ini akan membangun image Docker dari proyek deteksi penipuan Anda dan menjalankan container untuk mengakses API dan aplikasi Streamlit melalui port yang telah ditetapkan.