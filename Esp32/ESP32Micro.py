from machine import Pin, ADC
import json
import network
import utime as time
import dht
import urequests as requests

#Constants (Isi yang sesuai)
WIFI_SSID = ""
WIFI_PASSWORD = ""
URL = "http://<IpAdressHere>:5000/data"

#ESP32 Pins dan variables
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
DHT_PIN = Pin(15)
Motion_PIN = Pin(4,Pin.IN)

#Global Variables
dht_sensor = dht.DHT11(DHT_PIN)
ldr_value = -1
motion = False
counter = 0
telemetry_data_old = ""

#Mengconvert data menjadi json data
def create_json_data(temperature, humidity, light, motion):
    data = json.dumps({
        "temp": temperature,
        "humidity": humidity,
        "ldr_value": light,
        "motion" : int(motion)
    })
    return data

#Send data ke Flask REST API Application
def send_data(temperature, humidity, light, motion):
    headers = {"Content-Type": "application/json"}
    data = create_json_data(temperature, humidity, light, motion)
    try:
        response = requests.post(URL, json=data, headers=headers)
        print(data)
    except Exception as e:
        print("Failed to send data:", e)

#Mencoba untuk connect ke WIFI
wifi_client = network.WLAN(network.STA_IF)
wifi_client.active(True)
print("Connecting device to WiFi")
wifi_client.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi_client.isconnected():
    print("Connecting")
    time.sleep(0.1)
print("WiFi Connected!")
print(wifi_client.ifconfig())


# For Motion Sensor
#Function ini akan ketrigger ketika IOT LDR mendeteksi sebuah motion
def handle_interrupt(pin):
    global motion
    motion=True

#Setiap delay interval, akan mengecek ketika motion adalah true
#ketika true akan menambah counter +1
def motion_sensor_check():
    global counter
    if motion:
        counter += 1
        
#Ketika counter sudah samadengan atau melebihi 2, akan merubah motion menjadi false
#Ini akan berfungsi sebagai buffer untuk motion ketika tidak ada motion terjadi.
def motion_counter():
    global counter, motion
    if counter >= 2:
        motion = False
        counter = 0 
         
Motion_PIN.irq(trigger=Pin.IRQ_RISING,handler=handle_interrupt)

#Membandingkan data lama dengan data terbaru, dan jika ada perubahan maka akan di post ke REST API.
#Juga mengupdate data lama menjadi data baru
def evaluate_data():
    global telemetry_data_old
    telemetry_data_new = create_json_data(dht_sensor.temperature(), dht_sensor.humidity(), ldr_value, motion)
    if telemetry_data_new != telemetry_data_old and telemetry_data_old != "":
        # Call the send_data function to send data to Ubidots
        send_data(dht_sensor.temperature(), dht_sensor.humidity(), ldr_value, motion)
    telemetry_data_old = telemetry_data_new

#While loop dengan 0.5 + 0.3 jeda
#Mengecek IOT sensors pada motion, DHT, dan DLR dan merubah global variable ketika ada perubahan
#kemudian ketika ada perubahan dibanding data sebelumnya, maka akan di post
while True:
    try:
        motion_sensor_check()
        dht_sensor.measure()
        ldr_value = ldr.read()
        time.sleep(0.5)
    except:
        pass

    evaluate_data()
    time.sleep(0.3)
    # setelah 3 kali cycle, motion sensor akan menjadi false
    motion_counter()



