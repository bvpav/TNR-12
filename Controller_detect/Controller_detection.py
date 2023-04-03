from evdev import InputDevice, categorize, ecodes
import time

gamepad = InputDevice('/dev/input/event7')

left_joystick_for_car_movement = 128
rigth_joystick_for_hammer_movement = [128, 128]
R2_for_car_gas = 0
X_for_hammer_hit = 0
L1_for_barrel_movement = 0

def joytick_left(event):
    if event.code == 0:
        left_joystick_for_car_movement = event.value


def joytick_right(event):
    if event.code == 2:
        rigth_joystick_for_hammer_movement[0] = event.value
    elif event.code == 5:
        rigth_joystick_for_hammer_movement[1] = event.value

def triggers(event):
    if event.code == 3:
        R2_for_car_gas = event.value
    elif event.code == 305:
        X_for_hammer_hit = event.value
    elif event.code == 308:
        L1_for_barrel_movement = event.value

def main():
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
            joytick_left(event)
            joytick_right(event)
            triggers(event)
            #code
        

