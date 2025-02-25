from flask import Flask, request
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from datetime import datetime

# Ubidots API Credentials (isi dengan sesuai)
TOKEN = " " 
DEVICE_ID = " "
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID 

# MongoDB Credentials (isi dengan sesuai)
MONGODB_URL = ""
DB_NAME = "WeKnowNowDatabase"
COLLECTION_NAME = "SensorData"


# Function untuk post data ke Ubidots
# Dengan token dan device id, data dapan di teruskan ke Ubidots
def post_data_ubidots(json_data):
    if json_data:
        headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
        response = requests.post(UBIDOTS_URL, json=json_data, headers=headers)
        print("Ubidots Response:", response.status_code, response.text)

# Function untuk store data ke MongoDB dengan tambahan data current server time
# function akan membuka client Monggodb dengan URLnya kemudian menaruh data pada DB_NAME
# dan Collections yang sesuai.
def store_data_mongodb(json_data, cur_server_time):
    if json_data:
        json_data["timestamp"] = cur_server_time
        client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        # client.admin.command('ping')

        collection.insert_one(json_data)
        print("Data stored in MongoDB:", json_data, end="\n\n")

        client.close()

# Rest API Flask untuk recieve data
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        json_data = json.loads(request.get_json())
        cur_server_time = str(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
        post_data_ubidots(json_data)
        store_data_mongodb(json_data, cur_server_time)

        return {"status": "success", "message": "Data received successfully"}
    except Exception as e:
        print("Error:", e)
        return {"status": "error", "message": str(e)}

# Applikasi di run dengan port 5000 dan mencari LAN ip address untuk di connect
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


