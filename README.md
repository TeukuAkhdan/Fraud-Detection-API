# Machine Learning Fraud Detection <br>
   
## Problems <br>
Perusahaan harus mengadopsi strategi dan teknologi yang canggih... <br>
   
## Architecture <br>
Proyek ini berfokus pada Fraud Detection menggunakan Machine Learning... <br>
   
### Config <br>
Mengatur parameter, path, dan konfigurasi penting lainnya dalam proyek ini... <br>
   
### Models <br>
File-file pkl yang sudah di serialisasikan dari masing masing model machine learning dari training sampai ke tuning... <br>
   
### src <br>
Bagian utama dalam proyek ini, memuat semua kode yang berperan dalam fungsionalitas dan pengoperasian proyek ini... <br>
   
#### 1. 'helper.py' <br>
Code yang berisi fungsi-fungsi yang diperlukan... <br>
   
#### 2. 'training.py' <br>
Pada tahap ini, dilakukan pengembangan model machine learning untuk deteksi penipuan... <br>
   
#### 3. `main.py` <br>
File ini menggunakan FastAPI untuk membangun layanan deteksi penipuan... <br>
   
#### 4. `app.py` <br>
File ini bertanggung jawab untuk menampilkan hasil prediksi melalui antarmuka Streamlit yang terhubung ke API FastAPI... <br>
   
### Docker <br>
Memudahkan penggunaan machine learning Fraud Detection, proyek ini dapat dijalankan dalam lingkungan Docker... <br>
   
### Pyhton notebook files <br>
Eksperimentasi dari hasil eksplorasi data... <br>
   
### requirement.txt <br>
Library dependencies yang diperlukan untuk menjalankan code python... <br>
   
Rincian dan dataset dapat diunduh pada link dibawah ini... <br>
   
# Proyek Workflow <br>
## Menjalankan Proyek dengan Docker <br>
   
Untuk menjalankan proyek menggunakan Docker, ikuti langkah-langkah di bawah ini... <br>
   
## Langkah-langkah <br>
   
1. **Membangun Image Docker:** <br>
   - Pastikan Docker telah terinstal di komputer Anda... <br>
     ```
     docker build -t nama_image . <br>
     ```  
     Gantilah `nama_image` dengan nama yang ingin Anda berikan pada image Docker. <br>
   
2. **Menjalankan Container:** <br>
   Setelah berhasil membangun image Docker, jalankan container dengan perintah... <br>
   
Akses Proyek: <br>
- Setelah container berjalan, API akan dapat diakses melalui `http://localhost:8000`. <br>
- Aplikasi Streamlit akan dapat diakses melalui web browser pada `http://localhost:8501`. <br>
   
Pastikan untuk mengganti `nama_image` dengan nama yang relevan atau sesuai dengan keinginan Anda. Langkah-langkah ini akan membangun image Docker dari proyek deteksi penipuan Anda dan menjalankan container untuk mengakses API dan aplikasi Streamlit melalui port yang telah ditetapkan.
