# Script for reading in CO data from MQ-7 and sending to base station
# Can be adapted to other sensors with minimal changes
# Multiple sensor scripts can run on one Pi
import pika
import datetime
import time
import random
import struct
import gpiozero
from math import log10
user = ''
password = ''
baseaddr = ''
base = 'base' # Identifies which base station to contact
sensor = 'co' # Identifies which gas this sensor is measuring
credentials = pika.credentials.PlainCredentials(user,password)
connection = pika.BlockingConnection(pika.ConnectionParameters(baseaddr,credentials=credentials,heartbeat=60))
channel = connection.channel()
channel.queue_declare(queue=base)
adc = gpiozero.MCP3001(device=0) # Replace with relevant ADC and pin details
rzero = 12.423994743337015 # Calculated by experiment, varies from sensor to sensor
while(True):
        x = datetime.datetime.now()
        y = adc.value
        vs = 5*y # 5V signal
        rs = 50/vs-10 # Exact equation depends on sensor
        rat = rs/rzero 
        ppml = (log10(rat)-2.0162)/-1.4065 #Magic numbers calculated from datasheet
        ppm = 10**ppml
        print(ppm)
        body = bytes(struct.pack('!5sdd',bytes(sensor),x.timestamp(),y))
        channel.basic_publish(exchange='', routing_key=base, body=body)
        print(" [X] Sent %r" % body)
        print(x,y)
        connection.process_data_events(300) # keep heartbeat going for 5 minutes before looping
connection.close()
