# Write arduino from ps2_logger events to file
import serial
import sys
import time
import datetime
import argparse

# Config 
PORT = '/dev/cu.usbmodem621'
RATE = 115200


def loop(ser, output, log=False):
    while True:
        line = ser.readline()
        data = "{0}, {1}".format(datetime.datetime.now(), line)
        output.write(data)
        if log:
            sys.stdout.write(data)


def main(output_file, log=False):
    with serial.Serial(port=PORT, baudrate=RATE) as ser:
        print("Connected to %s" % ser.name)
        with open(output_file, 'w') as out:
            loop(ser, out, log=log)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('output', help='output file')
parser.add_argument('--log', default=False, action='store_true', help='Enable printing to console?')

args = parser.parse_args()
main(args.output, log=args.log)