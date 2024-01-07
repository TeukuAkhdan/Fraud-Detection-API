# Machine Learning Fraud Detection <br>
   
## Problems <br>
Perusahaan harus mengadopsi strategi dan teknologi yang canggih untuk secara proaktif mengurangi, mencegah, dan menanggulangi kerugian finansial yang disebabkan oleh penipuan transaksi. Dengan mengimplementasikan sistem deteksi dini yang efektif, pelatihan yang komprehensif bagi staf terkait, serta kerangka kerja keamanan yang ketat, perusahaan bertujuan untuk meminimalkan dampak keuangan dari segala jenis aktivitas penipuan yang terjadi dalam transaksi. <br>
Selain itu, perusahaan juga harus mengembangkan pendekatan yang seimbang antara keamanan dan kenyamanan pengguna dalam menghadapi aktivitas penipuan. Langkah-langkah yang diambil untuk mendeteksi dan mencegah penipuan haruslah terintegrasi secara halus ke dalam pengalaman pengguna, tanpa mengurangi kemudahan atau memberikan gangguan yang berarti.
<br>
### Config <br>
mengatur parameter, path, dan konfigurasi penting lainnya dalam proyek ini. <br>
   
### Models <br>
file-file pkl yang sudah di serialisasikan dari masing masing model machine learning dari training sampai ke tuning. <br>
   
### src <br>
bagian utama dalam proyek ini, memuat semua kode yang berperan dalam fungsionalitas dan pengoperasian proyek ini.<br>
   
#### 1. 'helper.py' <br>
Code yang berisi fungsi-fungsi yang diperlukan. <br>
   
#### 2. 'training.py' <br>
Pada tahap ini, dilakukan pengembangan model machine learning untuk deteksi penipuan. Langkah-langkahnya antara lain: <br>
- Menyiapkan dengan mendownload data dari google drive dengan size sebesar 470.7 MB. <br>
- Membagi data menjadi set pelatihan (train), validasi (val), dan pengujian (testing). <br>
- Melakukan preprocessing data, seperti One-Hot Encoding (OHE). <br>
- Melatih model menggunakan algoritma XGBoost. <br>
- Mencari parameter optimal menggunakan teknik random search. <br>
- Setelah mendapatkan parameter optimal, model disimpan ke dalam file pkl (pickle). <br>
   
#### 3. `main.py` <br>
File ini menggunakan FastAPI untuk membangun layanan deteksi penipuan. Langkah-langkahnya mencakup: <br>
- Memanfaatkan model XGBoost yang telah diserialisasikan dari model terbaik. <br>
- Menerima fitur-fitur sebagai input sesuai dengan data pelatihan. <br>
- Proses input data termasuk OHE dan prediksi berdasarkan fitur yang sudah bersih. <br>
- Menghitung probabilitas hasil prediksi. <br>
   
#### 4. `app.py` <br>
File ini bertanggung jawab untuk menampilkan hasil prediksi melalui antarmuka Streamlit yang terhubung ke API FastAPI (`API_URL`). <br>
   
### Docker <br>
MMemudahkan penggunaan machine learning Fraud Detection, proyek ini dapat dijalankan dalam lingkungan Docker. <br>
   
### Pyhton notebook files <br>
Eksperimentasi dari hasil eksplorasi data. <br>
   
### requirement.txt <br>
Library dependencies yang diperlukan untuk menjalankan code python. <br>
   
Rincian dan dataset dapat diunduh pada link dibawah ini. <br>
- data: https://www.kaggle.com/datasets/ealaxi/paysim1 <br>
- Artikel: https://medium.com/@akhdansyah/machine-learning-fraud-detection-0e10308b9ee1 <br>
<br>

## Architecture <br>
Poryek ini berfokus pada Fraud Detection menggunakan Machine Learning. Berikut adalah langkah-langkah utama yang dikerjakan: <br>
![Training Model](https://github.com/TeukuAkhdan/Fraud-Detection-API/blob/master/image/training%20model.jpeg?raw=true)

   
# Proyek Workflow <br>
![Workflow](https://github.com/TeukuAkhdan/Fraud-Detection-API/blob/master/image/Diagram%20worklflow.drawio.png?raw=true)
## Menjalankan Proyek dengan Docker <br>
   
Untuk menjalankan proyek menggunakan Docker, ikuti langkah-langkah di bawah ini. <br>
   
### Langkah-langkah <br>
   

1. **Membangun Image Docker:** <br>
   - Pastikan Docker telah terinstal di komputer Anda.
   - Buka terminal/cmd, masuk ke dalam direktori proyek yang berisi Dockerfile.
   - Jalankan perintah untuk membangun image Docker:
     ```
     docker build -t nama_image .
     ```
     Gantilah `nama_image` dengan nama yang ingin Anda berikan pada image Docker. <br>

2. **Menjalankan Container:** <br>
   Setelah berhasil membangun image Docker, jalankan container dengan perintah: <br>
   ```
   docker run -p 8000:8000 -p 8501:8501 nama_image
   ```
   jika pesan docker **Killed** ketika run training.py, maka jalankan perintah <br>
   ```
   docker run -p 8000:8000 -p 8501:8501 --cpus=0.5 --memory=2g my_image_name
   ```
   sesuaikan dengan core cpu dan memory/ram lokal agar dapat berjalan 

Perintah ini akan menjalankan container dari image yang telah dibuat sebelumnya. Opsi `-p` digunakan untuk memetakan port dari container ke port lokal komputer Anda. <br>
Akses Proyek: <br>
- Setelah container berjalan, API akan dapat diakses melalui `http://localhost:8000`. <br>
- Aplikasi Streamlit akan dapat diakses melalui web browser pada `http://localhost:8501`. <br>
![Streamlit](https://github.com/TeukuAkhdan/Fraud-Detection-API/blob/master/image/Fraud_Detection_streamlit_prediction.png?raw=true)
   
Pastikan untuk mengganti `nama_image` dengan nama yang relevan atau sesuai dengan keinginan Anda. Langkah-langkah ini akan membangun image Docker dari proyek deteksi penipuan Anda dan menjalankan container untuk mengakses API dan aplikasi Streamlit melalui port yang telah ditetapkan.
