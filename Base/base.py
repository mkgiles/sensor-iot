# Base station script, reads data from individual devices and adds them to the remote database
import struct
import pika
import time
import datetime
import mysql.connector
import signal
import sys
if(len(sys.argv) > 1):
    basename = sys.argv[1]
else:
    basename = "base"
db = mysql.connector.connect(user='username', password='password', host='remotehost', database='database')
cursor = db.cursor()
add_data = "INSERT INTO %s " % basename + "(type, time, ppm) " + "VALUES (%s, %s, %s)"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=basename)
def callback(ch,method,properties,body):
    print(" [x] Received %r" % body)
    d,x,y = struct.unpack('!5sdd',body)
    t = datetime.datetime.fromtimestamp(x)
    data = (d,t,y)
    print(*data)
    cursor.execute(add_data, data)
    db.commit()
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    connection.close()
    cursor.close()
    db.close()
    sys.exit(0)
channel.basic_consume(basename, auto_ack=True, on_message_callback=callback)
signal.signal(signal.SIGINT, signal_handler)
channel.start_consuming()
