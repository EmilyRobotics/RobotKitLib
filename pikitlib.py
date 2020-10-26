import Motor
from networktables import NetworkTables


class XboxController():
    def __init__(self, id):
        self.id = id
        self.nt = NetworkTables.getTable("DriverStation/XboxController{}".format(id))
        # must initialize the state of all controls here, because
        # if the first inquiry asks if a button was pressed, then
        # it has to know if the state has changed since the last
        # time...
        # get and save button state
        self.lastA = self.nt.getBoolean('Button0')
        self.lastB = self.nt.getBoolean('Button1')

    """
    Here is an example of the AButton, this should be generalized
    so that we can use the same code/logic for all of the buttons.
    Just figure out what the function would need to look like
    to be general, and then use the specifically named function
    to call it.
    """
    def getAButton(self):
        newA = self.nt.getBoolean('Button0')
        self.lastA = newA
        return newA

    def getAButtonPressed(self):
        newA = self.nt.getBoolean('Button0')
        pressed = newA and not self.lastA
        self.lastA = newA
        return pressed

    def getAButtonReleased(self):
        newA = self.nt.getBoolean('Button0')
        released = not newA and self.lastA
        self.lastA = newA
        return released

class SpeedController():
    def __init__(self):
        self.sc = Motor.Motor()

    def convert(self, value):
        #input: value between -1 and 1
        #output: value between maybe -2000, 2000?
        return value * 2000

    def set(self, value):
        value = self.convert(value)
        self.sc.setMotorModel(value,value,value,value)

class SpeedControllerGroup(SpeedController):

    def __init__(self, *argv):
        self.motors = []
        for motor in argv:
            self.motors.append(motor)
        

    def set(self, value):
        for m in self.motors:
            m.set(value)
        
class DifferentialDrive():

    def __init__(self, left: SpeedController, right:SpeedController):
        self.left = left
        self.right = right

    def arcadeDrive(self, xspeed: float, zRotation: float):
        #some math to convert a rotation value to speed value per motor
        pass

    def tankDrive(self, leftSpeed: float, rightSpeed:float):
        self.left.set(leftSpeed)
        self.right.set(rightSpeed)
