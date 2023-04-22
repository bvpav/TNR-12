import evdev

from gamepad import Gamepad
from main import CONTROLLER_MAC, get_ps5_device

device = get_ps5_device()
gamepad = Gamepad()


@gamepad.on_square_down
def handle_square_down(*args):
    print('on_square_down', *args)


@gamepad.on_square_up
def handle_square_up(*args):
    print('on_square_up', *args)


@gamepad.on_x_down
def handle_x_down(*args):
    print('on_x_down', *args)


@gamepad.on_x_up
def handle_x_up(*args):
    print('on_x_up', *args)


@gamepad.on_circle_down
def handle_circle_down(*args):
    print('on_circle_down', *args)


@gamepad.on_circle_up
def handle_circle_up(*args):
    print('on_circle_up', *args)


@gamepad.on_triangle_down
def handle_triangle_down(*args):
    print('on_triangle_down', *args)


@gamepad.on_triangle_up
def handle_triangle_up(*args):
    print('on_triangle_up', *args)


@gamepad.on_l1_down
def handle_l1_down(*args):
    print('on_l1_down', *args)


@gamepad.on_l1_up
def handle_l1_up(*args):
    print('on_l1_up', *args)


@gamepad.on_r1_down
def handle_r1_down(*args):
    print('on_r1_down', *args)


@gamepad.on_r1_up
def handle_r1_up(*args):
    print('on_r1_up', *args)


@gamepad.on_l2_down
def handle_l2_down(*args):
    print('on_l2_down', *args)


@gamepad.on_l2_up
def handle_l2_up(*args):
    print('on_l2_up', *args)


@gamepad.on_r2_down
def handle_r2_down(*args):
    print('on_r2_down', *args)


@gamepad.on_r2_up
def handle_r2_up(*args):
    print('on_r2_up', *args)


@gamepad.on_share_down
def handle_share_down(*args):
    print('on_share_down', *args)


@gamepad.on_share_up
def handle_share_up(*args):
    print('on_share_up', *args)


@gamepad.on_pause_down
def handle_pause_down(*args):
    print('on_pause_down', *args)


@gamepad.on_pause_up
def handle_pause_up(*args):
    print('on_pause_up', *args)


@gamepad.on_l3_down
def handle_l3_down(*args):
    print('on_l3_down', *args)


@gamepad.on_l3_up
def handle_l3_up(*args):
    print('on_l3_up', *args)


@gamepad.on_r3_down
def handle_r3_down(*args):
    print('on_r3_down', *args)


@gamepad.on_r3_up
def handle_r3_up(*args):
    print('on_r3_up', *args)


@gamepad.on_playstation_down
def handle_playstation_down(*args):
    print('on_playstation_down', *args)


@gamepad.on_playstation_up
def handle_playstation_up(*args):
    print('on_playstation_up', *args)


@gamepad.on_touchpad_down
def handle_touchpad_down(*args):
    print('on_touchpad_down', *args)


@gamepad.on_touchpad_up
def handle_touchpad_up(*args):
    print('on_touchpad_up', *args)


@gamepad.on_joy_l_x
def handle_joy_l_x(*args):
    print('on_joy_l_x', *args)


@gamepad.on_joy_l_y
def handle_joy_l_y(*args):
    print('on_joy_l_y', *args)


@gamepad.on_joy_r_x
def handle_joy_r_x(*args):
    print('on_joy_r_x', *args)


@gamepad.on_l2_analog
def handle_l2_analog(*args):
    print('on_l2_analog', *args)


@gamepad.on_r2_analog
def handle_r2_analog(*args):
    print('on_r2_analog', *args)


@gamepad.on_joy_r_y
def handle_joy_r_y(*args):
    print('on_joy_r_y', *args)


@gamepad.on_leftpad_left_down
def handle_leftpad_left_down(*args):
    print('on_leftpad_left_down', *args)


@gamepad.on_leftpad_left_up
def handle_leftpad_left_up(*args):
    print('on_leftpad_left_up', *args)


@gamepad.on_leftpad_right_down
def handle_leftpad_right_down(*args):
    print('on_leftpad_right_down', *args)


@gamepad.on_leftpad_right_up
def handle_leftpad_right_up(*args):
    print('on_leftpad_right_up', *args)


@gamepad.on_leftpad_up_down
def handle_leftpad_up_down(*args):
    print('on_leftpad_up_down', *args)


@gamepad.on_leftpad_up_up
def handle_leftpad_up_up(*args):
    print('on_leftpad_up_up', *args)


@gamepad.on_leftpad_down_down
def handle_leftpad_down_down(*args):
    print('on_leftpad_down_down', *args)


@gamepad.on_leftpad_down_up
def handle_leftpad_down_up(*args):
    print('on_leftpad_down_up', *args)


for event in device.read_loop():
    gamepad.handle_event(event)
