from gpiozero import DistanceSensor, PWMLED
from time import sleep
from signal import SIGTERM, SIGHUP, pause, signal

''' Student Name: Daniel Agbay
    Sudent ID: 220224024
    
    Inspired by code from Peter Stacy: youtube.com/watch?v=9kvuJ4ujkA
    The following code is modified by Daniel Agbay for the task's requirements
'''

# Setup
redLED = PWMLED(2) # LED Device interpreting the distance as light level. PWMLED is used as it has a brightness variable.
distanceSensor = DistanceSensor(echo=4, trigger=17) # Distance Sensor 

# Provides a safer way to exit the program.
def exit_safe():
    exit(1)

# Main Class
def main():
    checkingStatus = True # Is True while the program is still running.
    try:
        signal(SIGTERM, exit_safe) # Termination Signal.
        signal(SIGHUP, exit_safe) # Hangup Signal.
        redLED.on() # Turns on LED Device.
        while checkingStatus:
            distance = distanceSensor.value # Distance variable is initialised containing sensor value.
            print(f'Distance {distance:1.2f} ,') # Distance is conveyed on the console.
            duty_cycle = round(1.0 - distance,1) # Duty cycle variable is initialised containing rounded value of distance.
            print(f'Duty cycle: {duty_cycle}') # Duty Cycle is conveyed on the console (used to brightness configuration of LED Light).
            # Prevents the duty cycle from going below zero by setting duty cycle to 0.
            if duty_cycle < 0:
                duty_cycle = 0.0
            redLED.value = duty_cycle # LED light takes in duty cycle variable for brightness change.
            sleep(0.1) # Delays for 0.1 seconds
    except KeyboardInterrupt:
        pass
    finally:
        checkingStatus = False
        distanceSensor.close()

if __name__ == '__main__':
    main()
