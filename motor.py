import RPi.GPIO as GPIO
from dataclasses import dataclass


@dataclass
class MotorConfig:
    pin_en: int
    pin_forward: int
    pin_backward: int


class MotorController:
    def __init__(
        self,
        left_motor: MotorConfig,
        right_motor: MotorConfig,
        drum_motor: MotorConfig,
    ):
        self.__left_motor = left_motor
        self.__right_motor = right_motor
        self.__drum_motor = drum_motor

        GPIO.setmode(GPIO.BCM)
        self.__left_pwm = self.__setup_motor_pwm(self.__left_motor)
        self.__right_pwm = self.__setup_motor_pwm(self.__right_motor)
        self.__setup_motor(self.__drum_motor)

        self._drum_on = False
        self._forward_backward = 0.0
        self._steer = 0.0

    def __del__(self):
        GPIO.cleanup()

    @staticmethod
    def __setup_motor_pwm(motor):
        GPIO.setup(motor.pin_forward, GPIO.OUT)
        GPIO.setup(motor.pin_backward, GPIO.OUT)
        GPIO.setup(motor.pin_en, GPIO.OUT)
        GPIO.output(motor.pin_forward, GPIO.LOW)
        GPIO.output(motor.pin_backward, GPIO.LOW)
        pwm = GPIO.PWM(motor.pin_en, 1000)
        pwm.start(0)
        return pwm

    @staticmethod
    def __setup_motor(motor):
        GPIO.setup(motor.pin_forward, GPIO.OUT)
        GPIO.setup(motor.pin_backward, GPIO.OUT)
        GPIO.setup(motor.pin_en, GPIO.OUT)
        GPIO.output(motor.pin_forward, GPIO.HIGH)
        GPIO.output(motor.pin_backward, GPIO.LOW)
        GPIO.output(motor.pin_en, GPIO.LOW)

    def toggle_drum(self):
        self._drum_on = not self._drum_on
        print('drum_on', self._drum_on)
        if self._drum_on:
            GPIO.output(self.__drum_motor.pin_en, GPIO.HIGH)
        else:
            GPIO.output(self.__drum_motor.pin_en, GPIO.LOW)

    def set_forward_backward(self, value: float):
        print('forward_backward', value)
        self._forward_backward = value
        self.__update_left_right_motors()

    def set_steer(self, value: float):
        print('steer', value)
        self._steer = value
        self.__update_left_right_motors()

    def __update_left_right_motors(self):
        left = self._forward_backward + self._steer
        right = self._forward_backward - self._steer

        if left < 0:
            GPIO.output(self.__left_motor.pin_forward, GPIO.HIGH)
            GPIO.output(self.__left_motor.pin_backward, GPIO.LOW)
        else:
            GPIO.output(self.__left_motor.pin_forward, GPIO.LOW)
            GPIO.output(self.__left_motor.pin_backward, GPIO.HIGH)

        if right < 0:
            GPIO.output(self.__right_motor.pin_forward, GPIO.HIGH)
            GPIO.output(self.__right_motor.pin_backward, GPIO.LOW)
        else:
            GPIO.output(self.__right_motor.pin_forward, GPIO.LOW)
            GPIO.output(self.__right_motor.pin_backward, GPIO.HIGH)

        left = max(0, min(abs(left), 100))
        right = max(0, min(abs(right), 100))
        self.__left_pwm.ChangeDutyCycle(left)
        self.__right_pwm.ChangeDutyCycle(right)
