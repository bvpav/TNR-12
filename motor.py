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

    def __del__(self):
        GPIO.cleanup()

    @staticmethod
    def __setup_motor_pwm(motor):
        GPIO.setup(motor.pin_forward, GPIO.OUT)
        GPIO.setup(motor.pin_backward, GPIO.OUT)
        GPIO.setup(motor.pin_enable, GPIO.OUT)
        GPIO.output(motor.pin_forward, GPIO.LOW)
        GPIO.output(motor.pin_backward, GPIO.LOW)
        return GPIO.PWM(motor.enable, 1000)

    @staticmethod
    def __setup_motor(motor):
        GPIO.setup(motor.pin_forward, GPIO.OUT)
        GPIO.setup(motor.pin_backward, GPIO.OUT)
        GPIO.setup(motor.pin_enable, GPIO.OUT)
        GPIO.output(motor.pin_forward, GPIO.LOW)
        GPIO.output(motor.pin_backward, GPIO.LOW)
        GPIO.output(motor.pin_backward, GPIO.HIGH)
