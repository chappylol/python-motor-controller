#!/usr/bin/python

import time
import serial
import sys
import random

def createPacket(address = 130, command = 100, data=64, badPacket=False):
    if badPacket:
        packet = str(random.getrandbits(32))
    else: 
        checksum = (address + command + data) & int('0b11111111',2) 
        address = chr(address)
        command = chr(command)
        data = chr(data)
        checksum = chr(checksum)
    
        packet = address + command + data + checksum 

    print "Address: " + address + " Command: " + command + " Data: " + data + "Checksum " + checksum
    return packet

def stepClockwise (value, command = 0):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def stepCClockwise (value, command = 1):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def changeSpeedHigh (value, command = 2):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def changeSpeedLow (value, command = 3):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def rotateClockwise (value, command = 4):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def rotateCClockwise (value, command = 5):
    packet = createPacket(command = command, data = value)
    return packet

def spinClockwise (command = 6):
    packet = createPacket(command = command)
    return packet

def spinCClockwise (command = 7):
    packet = createPacket(command = command)
    return packet

def returnToZero (command = 8):
    packet = createPacket(command = command)
    return packet

def setZeroPosition (command = 9):
    packet = createPacket(command = command)
    return packet

def setSpeedMode (value, command = 100):
    valueRange = range(0,1)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def setStepsPerRotation (value, command = 101):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def setMultiplier (value, command = 102):
    valueRange = range(0,255)
    if value in valueRange: 
        packet = createPacket(command = command, data = value)
    else:
        return False
    return packet

def printAndRunOptions():
    input = int(raw_input("""
    0) Step Clockwise. [0-255]
    1) Step Counter Clockwise. [0-255]
    2) Change High Speed. [0-255]
    3) Change Low Speed. [0-255]
    4) Rotate Clockwise. [0-255]
    5) Rotate Counter Clockwise. [0-255]
    6) Spin Clockwise.
    7) Spin Counter Clockwise. 
    8) Return to Zero.
    9) Set Zero Position
    100) Set Speed mode.
    101) Set steps per rotation. [0-255]
    102) Set stepper multiplier. [0-255]
    """).rstrip())
    if input in [0,1,2,3,4,5,9,101,102]:
        value = int(raw_input("Value: ").rstrip())

    if input == 0:
        return stepClockwise(value)
    elif input == 1:
        return stepCClockwise(value)
    elif input == 2:
        return changeSpeedHigh(value)
    elif input == 3:
        return changeSpeedLow(value)
    elif input == 4:
        return rotateClockwise(value)
    elif input == 5:
        return rotateCClockwise(value)
    elif input == 6:
        return spinClockwise(value)
    elif input == 7:
        return spinCClockwise(value)
    elif input == 8:
        return returnToZero(value)
    elif input == 9:
        return setZeroPosition(value)
    elif input == 100:
        return setSpeedMode(value)
    elif input == 101:
        return setStepsPerRotation(value)
    elif input == 102:
        return setMultiplier(value)
    else:
        print "GO FUCK YOURSELF"
        sys.exit()
