import Motor






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
