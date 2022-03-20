import RPi.GPIO as GPIO
import atexit
import time
import paho.mqtt.client as mqtt

BROKER="192.168.0.5"
PORT=1883

mqttc = mqtt.Client("household_gas_meter")

def exit_handler():
  GPIO.cleanup();

def on_publish(client, userdata, result):
  print("mqtt sent")
  pass

atexit.register(exit_handler)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count=0

def falling_edge_callback(channel):
  global count
  print("Detected falling edge")
  count=count+1

print('connecting to gpio')
GPIO.add_event_detect(26, GPIO.FALLING, callback=falling_edge_callback, bouncetime=1000)
print('connected')

mqttc.on_publish = on_publish
print('connecting to mqtt')
mqttc.connect(BROKER,PORT)
print('connected')

while True:
  print(count)
  mqttc.reconnect()
  mqttc.publish("meters/household_gas/total_import",count/100, retain=True)


  time.sleep(10)


