# python run.py robot.py

import sys
import robot
import time

# robot loop
"""

main init

if telop:
    telop init

    loop telop until done

if auton:
    auton init
    loop auton until done

"""


class main():

    def __init__(self, mode):
        self.r = robot.MyRobot()
        

    def start(self):    
        self.r.robotInit()

    def telop(self):
        self.r.teleopPeriodic()
        time.sleep(0.02)

    
    





if __name__ == "__main__":
    if sys.argv[1] == "auton":
        mode = "a"
    else:
        mode = None
    m = main(mode)
