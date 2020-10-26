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
        
        # A-0,B-1,X-2,Y-3
        self.lastButtonValues = []
        self.lastButtonValues.append(self.nt.getBoolean('Button0'))
        self.lastButtonValues.append(self.nt.getBoolean('Button1'))
        self.lastButtonValues.append(self.nt.getBoolean('Button2'))
        self.lastButtonValues.append(self.nt.getBoolean('Button3'))


    def getButton(self, v) -> bool:
        newB = self.nt.getBoolean('Button' + str(v))
        self.lastButtonValues[v] = newB
        return newB

    def getButtonPressed(self, v) -> bool:
        newB = self.nt.getBoolean('Button' + str(v))
        pressed = newB and not self.lastButtonValues[v]
        self.lastButtonValues[v] = newB
        return pressed

    def getButtonReleased(self, v) -> bool:
        newB = self.nt.getBoolean('Button' + str(v))
        released =  not newB and self.lastButtonValues[v]
        self.lastButtonValues[v] = newB
        return released


    #TODO: put these values in a variable
    def getAButton(self):
        return self.getButton(0)

    def getAButtonPressed(self):
        return self.getButtonPressed(0)

    def getAButtonReleased(self):
        self.getButtonReleased(0)

    def getBButton(self):
        return self.getButton(1)

    def getBButtonPressed(self):
        return self.getButtonPressed(1)

    def getBButtonReleased(self):
        self.getButtonReleased(1)

    def getXButton(self):
        return self.getButton(2)

    def getXButtonPressed(self):
        return self.getButtonPressed(2)

    def getXButtonReleased(self):
        self.getButtonReleased(2)

    def getYButton(self):
        return self.getButton(3)

    def getYButtonPressed(self):
        return self.getButtonPressed(3)

    def getYButtonReleased(self):
        self.getButtonReleased(3)


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
