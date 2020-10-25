# python run.py robot.py

import sys
import robot
import time

from networktables import NetworkTables
import threading

import logging

logging.basicConfig(level=logging.DEBUG)
# robot loop
"""

check networktable for updates

if auton:
    auton init
    repeat auton every 20 miliseconds until not auton

if telop:
    telop init
    repeat teleop every 20 miliseconds until not teleop
    repeatly check for controller values



"""
ip = "10.10.10.10" #ip address



class main():
    def __init__(self):
        self.r = robot.MyRobot()
        self.connected = False
        
    #inital connection to networktable, check for updates
    def connect(self):
        NetworkTables.initialize(server=ip)
        NetworkTables.addConnectionListener(self.connectionListener, immediateNotify=True)

        sd = NetworkTables.getTable("TODO")
        sd.addEntryListener(self.valueChanged)

    
    def connectionListener(self, connected, info):
        print(info, "; Connected=%s" % connected)
        self.connected = True

    #Print the values changed in the network table
    def valueChanged(self, table, key, value, isNew):
        print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))

    def start(self):    
        self.r.robotInit()

    def telop(self):
        self.r.teleopPeriodic()
        time.sleep(0.02)

    
    





if __name__ == "__main__":
    m = main()
    m.connect()
