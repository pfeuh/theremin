#!/usr/bin/python3
# -*- coding: utf-8 -*-

MIN = 435.0
MAX = 867.0
NB_NOTES = 23.0
FULL_RANGE = MAX - MIN
INTERVAL = (MAX - MIN) / NB_NOTES

def printNote(value):
    note  = NB_NOTES / (FULL_RANGE / ( value - MIN))
    print note    

import serial

LF = "\n"

port = serial.Serial(port="/dev/ttyUSB1")

text = ""
while 1:
    car = port.read()
    if car != LF:
        text += car
    else:
        value = float(text)
        printNote(value)
        #~ print(value)
        #~ print(LF)
        text = ""
