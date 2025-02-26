## SIC Assignment 2 - We Know Now (UNI129)

Tugas membuat script ESP32 Micropython dan Flask REST API untuk visualisasi data menggunakan Ubidots dan menyimpannya ke MongoDB.

#### Hasil Visualisasi dan data Ubidots dan database MongoDB
![image](https://github.com/user-attachments/assets/77a159e4-975f-493f-af63-23edc259d535)
![image](https://github.com/user-attachments/assets/11ddd3fa-147b-40b8-98fd-8874a3443bf2)


#### Sketch dan Foto hasil rangkaian ESP32
![image](https://github.com/user-attachments/assets/283d4c1a-afe9-4583-9747-8ef6a23e7248)
![image](https://github.com/user-attachments/assets/79bcba79-8118-4712-823a-7b117f00732d)
![image](https://github.com/user-attachments/assets/2b2e2acf-8879-43ac-af12-e288bbebd112)

## How to Set up 

Sebelum memulai, pastikan sudah menginstall applikasi Visual Studio Code, Thonny IDE, dan sudah memiliki akun Ubidots dan MongoDB Cloud.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Python](https://www.python.org/downloads/) or via Microsoft Store
- [Visual Studio Code](https://code.visualstudio.com/)
- [Thonny IDE](https://thonny.org/)
- [Ubidots Stem](https://ubidots.com/stem)
- [Cloud MongoDB](https://cloud.mongodb.com/)

Main IOT Component that will be in use
- ESP32
- DHT11
- PIR Motion Sensor
- LDR Sensor

### Installing

For running the Flask API, open visual studio and install Flask library using terminal.

    $ pip install Flask

For mongoDB, install this library for submiting data to cloud (make sure the version is compatible)

	$ python -m pip install "pymongo[srv]"==3.11

## Running the Program

### Running Flask API 

After this, open up [Script.py](https://github.com/RasyaDevansyah/Assignment2WeKnowNow/blob/main/FlaskAPI/Script.py) using VS Code and it will have these constant variables that need to be filled.
	
 	# Ubidots API Credentials (isi dengan sesuai)
	TOKEN = " " 
	DEVICE_ID = " "
	UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID 
	
	# MongoDB Credentials (isi dengan sesuai)
	MONGODB_URL = ""
	DB_NAME = "WeKnowNowDatabase"
 	COLLECTION_NAME = "SensorData"


You can get TOKEN and DEVICE_ID by logging in to [stem.ubidots](https://stem.ubidots.com/) and make an ESP32 device.    
![image](https://github.com/user-attachments/assets/8224ca24-5f88-4996-a9c8-47be6ceba971)

And for MongoDB, you can login to [MongoDBCloud](https://cloud.mongodb.com/) create a new cluster, go to "connect" and copy the connection string (be sure to replace the string "db_password" to your user password.)
![image](https://github.com/user-attachments/assets/fd3d3b1f-1466-4fe4-824b-86520b464722)


After filling the credentials, you can run the program and it will make a URL to your LAN IP address
![image](https://github.com/user-attachments/assets/f6c8a1de-f8ca-42d2-b356-c031e737a5b0)

### Running Micropython

Open [ESP32Micro.py](https://github.com/RasyaDevansyah/Assignment2WeKnowNow/blob/main/Esp32/ESP32Micro.py) using Thonny IDE and plug in your IOT device to your machine. 

Next, Fill out these constant variables. (you can paste the URL LAN IP address from the Flask to the URL variable.)
![image](https://github.com/user-attachments/assets/3ceb73d7-ee08-4db1-b0e6-322b7faf871c)
