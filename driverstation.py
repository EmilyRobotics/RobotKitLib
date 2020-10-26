from networktables import NetworkTables
import pygame, sys, time    #Imports Modules
from pygame.locals import *

#def stick_stats(joystick):

# parse command line argument
if len(sys.argv) != 2:
    print("Error: specify robot IP to connect; Bye!")
    exit(0)

# assume the first arg is the robot IP address
ip = sys.argv[1]
NetworkTables.initialize(ip)


pygame.init()#Initializes Pygame
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()#Initializes Joystick

joystick_count = pygame.joystick.get_count()

# save reference to table for each xbox controller
xbc_nt = []
for stick_idx in range(0, joystick_count):
    xbc_nt.append(NetworkTables.getTable('XboxController/{}'.format(stick_idx)))


# This is just demo code.   Need to respond to events and update
# the state in the networktables.
# Nothing there yet.
numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)
print("--------------")

loopQuit = False
while loopQuit == False:

    # test joystick axes and prints values
    outstr = "Axes :"
    for i in range(0,4):
        axis = joystick.get_axis(i)
        outstr = outstr + str(i) + ":" + str(axis) + "|"
        print(outstr)

    # test controller buttons
    outstr = "Buttons: "
    for i in range(0,numbuttons):
           button = joystick.get_button(i)
           outstr = outstr + str(i) + ":" + str(button) + "|"
    print(outstr)

    for event in pygame.event.get():
        if event.type == QUIT:
            loopQuit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopQuit = True

        print("Event type:", event.type) 
        # Returns Joystick Button Motion
        if event.type == pygame.JOYBUTTONDOWN:
            print("joy button down")
        if event.type == pygame.JOYBUTTONUP:
            print("joy button up")
        if event.type == pygame.JOYBALLMOTION:
            print("joy ball motion")
        # axis motion is movement of controller
        # dominates events when used
        if event.type == pygame.JOYAXISMOTION:
            pass

    time.sleep(0.5)

pygame.quit()
sys.exit()
