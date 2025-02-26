# SIC Assignment 2 - We Know Now (UNI129)

Tugas ini berfokus pada pembuatan script ESP32 menggunakan MicroPython dan Flask REST API untuk visualisasi data di Ubidots serta penyimpanan ke MongoDB.

## Hasil Visualisasi dan Data

Data yang dikirimkan dari ESP32 akan divisualisasikan di Ubidots dan disimpan di MongoDB Cloud.

![image](https://github.com/user-attachments/assets/77a159e4-975f-493f-af63-23edc259d535)

![image](https://github.com/user-attachments/assets/11ddd3fa-147b-40b8-98fd-8874a3443bf2)

## Sketch dan Foto Hasil Rangkaian ESP32

Berikut adalah rangkaian ESP32 beserta sensor yang digunakan:

![image](https://github.com/user-attachments/assets/283d4c1a-afe9-4583-9747-8ef6a23e7248)

![image](https://github.com/user-attachments/assets/79bcba79-8118-4712-823a-7b117f00732d)

![image](https://github.com/user-attachments/assets/2b2e2acf-8879-43ac-af12-e288bbebd112)

## Persiapan (Prerequisites)

### Software yang Dibutuhkan:

- [Python](https://www.python.org/downloads/) (Bisa install via Microsoft Store juga)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Thonny IDE](https://thonny.org/)
- [Ubidots Stem](https://ubidots.com/stem)
- [MongoDB Cloud](https://cloud.mongodb.com/)

### Komponen IoT yang Digunakan:

- **ESP32 DIOD Micro USB Type**
- **DHT11** (Temperature & Humidity Sensor)
- **HC-SR501** (PIR Motion Sensor)
- **LDR 5mm Sensor** & **Resistor**
- **Jumper Cables**
- **ESP32 BaseBoard**
- **Breadboard**

## Instalasi

### Install Flask API

Jalankan perintah berikut di terminal untuk menginstal Flask:

```sh
pip install Flask
```

### Install MongoDB Library

Untuk menghubungkan ke MongoDB Cloud, install library berikut:

```sh
python -m pip install "pymongo[srv]"==3.11
```

## Menjalankan Program

### 1. Setup Flask API

Buka file [Script.py](https://github.com/RasyaDevansyah/Assignment2WeKnowNow/blob/main/FlaskAPI/Script.py) menggunakan Visual Studio Code, lalu isi bagian credential berikut:

```python
# Ubidots API Credentials
TOKEN = " "
DEVICE_ID = " "
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID

# MongoDB Credentials
MONGODB_URL = ""
DB_NAME = "WeKnowNowDatabase"
COLLECTION_NAME = "SensorData"
```

Untuk mendapatkan **TOKEN** dan **DEVICE\_ID**, login ke [stem.ubidots](https://stem.ubidots.com/) dan buat device ESP32.

![image](https://github.com/user-attachments/assets/8224ca24-5f88-4996-a9c8-47be6ceba971)

Untuk **MongoDB**, login ke [MongoDB Cloud](https://cloud.mongodb.com/), buat cluster baru, lalu klik **"connect"** dan copy connection string-nya (ganti `db_password` dengan password akun MongoDB kamu).

![image](https://github.com/user-attachments/assets/fd3d3b1f-1466-4fe4-824b-86520b464722)

Setelah diisi, jalankan Flask API dan program akan memberikan URL dengan LAN IP address.

![image](https://github.com/user-attachments/assets/f6c8a1de-f8ca-42d2-b356-c031e737a5b0)

### 2. Setup MicroPython di ESP32

Buka file [ESP32Micro.py](https://github.com/RasyaDevansyah/Assignment2WeKnowNow/blob/main/Esp32/ESP32Micro.py) menggunakan **Thonny IDE** dan sambungkan ESP32 ke komputer.

Isi variabel URL dengan LAN IP address dari Flask API.

![image](https://github.com/user-attachments/assets/3ceb73d7-ee08-4db1-b0e6-322b7faf871c)

⚠️ **Catatan**: Pastikan ESP32 dan Flask API berada di jaringan WiFi yang sama! Atau program tidak bisa berjalan.

## Rangkaian dan Pin ESP32

Dalam proyek ini, 3 sensor utama digunakan:

- **DHT11** → Temperatur & Kelembaban
- **LDR** → Sensor Cahaya
- **PIR** → Sensor Gerak

Berikut adalah variable pin yang digunakan (bisa disesuaikan dengan rangkaian):

![image](https://github.com/user-attachments/assets/170bcb1e-c643-4d89-ae7b-0971508392a2)

![image](https://github.com/user-attachments/assets/beed9c38-eb93-4432-9799-e241e3fc9598)

## Jalankan MicroPython di ESP32

Setelah semua siap, jalankan MicroPython di ESP32!🎉

Sekarang ESP32 akan mulai mengumpulkan data dan mengirimkannya ke Flask API. Data tersebut akan ditampilkan di **Ubidots** dan juga disimpan di **MongoDB Cloud**.

## Contributors

### Winona Patricia Pangestu
* **Universitas**: Bina Nusantara University
* **GitHub**: [wengnong](https://github.com/wengnong)
* **Program Studi**: Computer Science
* **Fakultas**: School of Computer Science

### Muhammad Rasya Devansyah
* **Universitas**: Bina Nusantara University
* **GitHub**: [rasyadevansyah](https://github.com/rasyadevansyah)
* **Program Studi**: Computer Science
* **Fakultas**: School of Computer Science

### Agnetta Indira Revata
* **Universitas**: Bina Nusantara University
* **Program Studi**: Computer Science
* **Fakultas**: School of Computer Science

### Ariel Raynara Zhang
* **Universitas**: Bina Nusantara University
* **GitHub**: [notbenjackson](https://github.com/notbenjackson)
* **Program Studi**: Computer Science
* **Fakultas**: School of Computer Science
