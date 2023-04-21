import evdev

from gamepad import Gamepad
import motor

CONTROLLER_MAC = '4C:B9:9B:05:D2:83'


def get_ps5_device():
    devices = map(evdev.InputDevice, evdev.list_devices())
    for device in devices:
        if device.uniq.lower() == CONTROLLER_MAC.lower():
            return device
    raise LookupError('Unable to find PS5 controller. Have you paired it?')


def main():
    device = get_ps5_device()
    gamepad = Gamepad()
    motor_controller = motor.MotorController(
        left_motor=motor.MotorConfig(
            pin_forward=23,
            pin_backward=24,
            pin_en=25,
        ),
        right_motor=motor.MotorConfig(
            pin_forward=7,
            pin_backward=8,
            pin_en=12,
        ),
        drum_motor=motor.MotorConfig(
            pin_forward=20,
            pin_backward=16,
            pin_en=21,
        ),
    )

    @gamepad.on_r2_analog
    def handle_r2_analog(value):
        r2_value = (value - 128) / 127 * 100
        l2_value = (gamepad.l2_analog - 128) / 127 * 100
        motor_controller.set_forward_backward(l2_value - r2_value)

    @gamepad.on_l2_analog
    def handle_l2_analog(value):
        r2_value = (gamepad.r2_analog - 128) / 127 * 100
        l2_value = (value - 128) / 127 * 100
        motor_controller.set_forward_backward(l2_value - r2_value)

    @gamepad.on_joy_l_x
    def handle_joy_left_x(value):
        value = (value - 128) / 127 * 100
        motor_controller.set_steer(value)

    @gamepad.on_l1_up
    def handle_l1_up():
        motor_controller.toggle_drum()

    for event in device.read_loop():
        gamepad.handle_event(event)


if __name__ == '__main__':
    main()
