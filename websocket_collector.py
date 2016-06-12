# Write arduino from ps2_logger events to a websocket
import argparse
import datetime
import serial
import sys
import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

# Config 
PORT = '/dev/cu.usbmodem411'
RATE = 115200

SOCKET_PORT = 8000


socket = None

class Socket(WebSocket):
    def handleMessage(self):
        print self.data
        
    def handleConnected(self):
        print self.address, 'connected'
        global socket
        socket = self
        
    def handleClose(self):
        print self.address, 'closed'
        global socket
        socket = None

def loop(ser, log=False):
    while True:
        line = ser.readline()
        data = u"{0}, {1}".format(datetime.datetime.now(), line)
        if socket is not None:
            socket.sendMessage(data)
        if log:
            sys.stdout.write(data)

def main(log=False):
    with serial.Serial(port=PORT, baudrate=RATE) as ser:
        print("Connected to %s" % ser.name)
        loop(ser, log=log)


parser = argparse.ArgumentParser(description='Write arduino from ps2_logger events to a websocket.')
parser.add_argument('--log', default=False, action='store_true', help='Enable printing to console?')

args = parser.parse_args()

try:
    t = threading.Thread(target = lambda: main(log=args.log))
    t.daemon = True
    t.start()
except Exception as e:
    print e


server = SimpleWebSocketServer('', SOCKET_PORT, Socket)
server.serveforever()