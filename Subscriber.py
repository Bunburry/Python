from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("/dev/cu.usbmodem1422",9600,timeout=2)

randomID = random()
client = Mosquitto("Gintare")
client.connect("10.212.61.136")

# The rest of your code goes in here !!!
client.subscribe("/simon/test")

def messageReceived(broker, obj, msg):
	global client
	payload = msg.payload.decode()
	print("Message " + msg.topic + " containing: " + payload)
	client = None
client.on_message = messageReceived
while (client != None): client.loop()