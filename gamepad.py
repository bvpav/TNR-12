import evdev


class Gamepad:
    CENTER = 128
    # there's a lot of drift at 128,
    # so don't report changes within (128 - CENTER)
    BLIND = 6
    # max number of milliseconds between taps to qualify as an emergency
    # double-tap
    MAX_EMERGENCY_DELAY = 1000

    def __init__(self):
        self.joy_l_x = Gamepad.CENTER
        self.joy_l_y = Gamepad.CENTER

        self.joy_r_x = Gamepad.CENTER
        self.joy_r_y = Gamepad.CENTER

        self.l1 = self.l2 = self.l3 = False
        self.r1 = self.r2 = self.r3 = False

        self.square = self.triangle = self.circle = self.x = False
        self.share = self.pause = False
        self.playstation = False
        self.touchpad = False

        self.l2_analog = self.r2_analog = 0

        self.leftpad_up = self.leftpad_down = False
        self.leftpad_left = self.leftpad_right = False

        self.__square_up_handlers = []
        self.__square_down_handlers = []

        self.__x_up_handlers = []
        self.__x_down_handlers = []

        self.__circle_up_handlers = []
        self.__circle_down_handlers = []

        self.__triangle_up_handlers = []
        self.__triangle_down_handlers = []

        self.__l1_up_handlers = []
        self.__l1_down_handlers = []

        self.__r1_up_handlers = []
        self.__r1_down_handlers = []

        self.__l2_up_handlers = []
        self.__l2_down_handlers = []

        self.__r2_up_handlers = []
        self.__r2_down_handlers = []

        self.__share_up_handlers = []
        self.__share_down_handlers = []

        self.__pause_up_handlers = []
        self.__pause_down_handlers = []

        self.__l3_up_handlers = []
        self.__l3_down_handlers = []

        self.__r3_up_handlers = []
        self.__r3_down_handlers = []

        self.__playstation_up_handlers = []
        self.__playstation_down_handlers = []

        self.__touchpad_up_handlers = []
        self.__touchpad_down_handlers = []

        self.__joy_l_x_handlers = []
        self.__joy_l_y_handlers = []
        self.__joy_r_x_handlers = []
        self.__l2_analog_handlers = []
        self.__r2_analog_handlers = []
        self.__joy_r_y_handlers = []

        self.__leftpad_left_down_handlers = []
        self.__leftpad_left_up_handlers = []
        self.__leftpad_right_down_handlers = []
        self.__leftpad_right_up_handlers = []
        self.__leftpad_up_down_handlers = []
        self.__leftpad_up_up_handlers = []
        self.__leftpad_down_down_handlers = []
        self.__leftpad_down_up_handlers = []

    def _handle_key(self, event: evdev.InputEvent):
        dispatch = {
            304: self._handle_square_press,
            305: self._handle_x_press,
            306: self._handle_circle_press,
            307: self._handle_triangle_press,
            308: self._handle_l1_press,
            309: self._handle_r1_press,
            310: self._handle_l2_press,
            311: self._handle_r2_press,
            312: self._handle_share_press,
            313: self._handle_pause_press,
            314: self._handle_l3_press,
            315: self._handle_r3_press,
            316: self._handle_playstation_press,
            317: self._handle_touchpad_press
        }
        try:
            dispatch[event.code](bool(event.value))
        except KeyError:
            pass
        # TODO: emergency check

    def _handle_touchpad_press(self, is_down: bool):
        self.touchpad = not is_down
        if self.touchpad:
            for handler in self.__touchpad_down_handlers:
                handler()
        else:
            for handler in self.__touchpad_up_handlers:
                handler()

    def _handle_playstation_press(self, is_down: bool):
        self.playstation = not is_down
        if self.playstation:
            for handler in self.__playstation_down_handlers:
                handler()
        else:
            for handler in self.__playstation_up_handlers:
                handler()

    def _handle_r3_press(self, is_down: bool):
        self.r3 = not is_down
        if self.r3:
            for handler in self.__r3_down_handlers:
                handler()
        else:
            for handler in self.__r3_up_handlers:
                handler()

    def _handle_l3_press(self, is_down: bool):
        self.l3 = not is_down
        if self.l3:
            for handler in self.__l3_down_handlers:
                handler()
        else:
            for handler in self.__l3_up_handlers:
                handler()

    def _handle_pause_press(self, is_down: bool):
        self.pause = not is_down
        if self.pause:
            for handler in self.__pause_down_handlers:
                handler()
        else:
            for handler in self.__pause_up_handlers:
                handler()

    def _handle_share_press(self, is_down: bool):
        self.share = not is_down
        if self.share:
            for handler in self.__share_down_handlers:
                handler()
        else:
            for handler in self.__share_up_handlers:
                handler()

    def _handle_r2_press(self, is_down: bool):
        self.r2 = not is_down
        if self.r2:
            for handler in self.__r2_down_handlers:
                handler()
        else:
            for handler in self.__r2_up_handlers:
                handler()

    def _handle_l2_press(self, is_down: bool):
        self.l2 = not is_down
        if self.l2:
            for handler in self.__l2_down_handlers:
                handler()
        else:
            for handler in self.__l2_up_handlers:
                handler()

    def _handle_r1_press(self, is_down: bool):
        self.r1 = not is_down
        if self.r1:
            for handler in self.__r1_down_handlers:
                handler()
        else:
            for handler in self.__r1_up_handlers:
                handler()

    def _handle_l1_press(self, is_down: bool):
        self.l1 = not is_down
        if self.l1:
            for handler in self.__l1_down_handlers:
                handler()
        else:
            for handler in self.__l1_up_handlers:
                handler()

    def _handle_triangle_press(self, is_down: bool):
        self.triangle = not is_down
        if self.triangle:
            for handler in self.__triangle_down_handlers:
                handler()
        else:
            for handler in self.__triangle_up_handlers:
                handler()

    def _handle_circle_press(self, is_down: bool):
        self.circle = not is_down
        if self.circle:
            for handler in self.__circle_down_handlers:
                handler()
        else:
            for handler in self.__circle_up_handlers:
                handler()

    def _handle_x_press(self, is_down: bool):
        self.x = not is_down
        if self.x:
            for handler in self.__x_down_handlers:
                handler()
        else:
            for handler in self.__x_up_handlers:
                handler()

    def _handle_square_press(self, is_down: bool):
        self.square = not is_down
        if self.square:
            for handler in self.__square_down_handlers:
                handler()
        else:
            for handler in self.__square_up_handlers:
                handler()

    def _handle_abs(self, event: evdev.InputEvent):
        absolutes = {
            0: self._handle_joy_l_x,
            1: self._handle_joy_l_y,
            2: self._handle_joy_r_x,
            3: self._handle_l2_analog,
            4: self._handle_r2_analog,
            5: self._handle_joy_r_y,
            16: self._handle_leftpad_left_right,
            17: self._handle_leftpad_up_down,
        }
        try:
            absolutes[event.code](event.value)
        except KeyError:
            pass

    def _handle_joy_r_y(self, value: float):
        self.joy_r_y = value
        for handler in self.__joy_r_y_handlers:
            handler(value)

    def _handle_r2_analog(self, value: float):
        self.r2_analog = value
        for handler in self.__r2_analog_handlers:
            handler(value)

    def _handle_l2_analog(self, value: float):
        self.l2_analog = value
        for handler in self.__l2_analog_handlers:
            handler(value)

    def _handle_joy_r_x(self, value: float):
        self.joy_r_x = value
        for handler in self.__joy_r_x_handlers:
            handler(value)

    def _handle_joy_l_y(self, value: float):
        self.joy_l_y = value
        for handler in self.__joy_l_y_handlers:
            handler(value)

    def _handle_joy_l_x(self, value: float):
        self.joy_l_x = value
        for handler in self.__joy_l_x_handlers:
            handler(value)

    def _handle_leftpad_left_press(self, is_down: bool):
        self.leftpad_left = not is_down
        if self.leftpad_left:
            for handler in self.__leftpad_left_down_handlers:
                handler()
        else:
            for handler in self.__leftpad_left_up_handlers:
                handler()

    def _handle_leftpad_right_press(self, is_down: bool):
        self.leftpad_right = not is_down
        if self.leftpad_right:
            for handler in self.__leftpad_right_down_handlers:
                handler()
        else:
            for handler in self.__leftpad_right_up_handlers:
                handler()

    def _handle_leftpad_up_press(self, is_down: bool):
        self.leftpad_up = not is_down
        if self.leftpad_up:
            for handler in self.__leftpad_up_down_handlers:
                handler()
        else:
            for handler in self.__leftpad_up_up_handlers:
                handler()

    def _handle_leftpad_down_press(self, is_down: bool):
        self.leftpad_down = not is_down
        if self.leftpad_down:
            for handler in self.__leftpad_down_down_handlers:
                handler()
        else:
            for handler in self.__leftpad_down_up_handlers:
                handler()

    def _handle_leftpad_left_right(self, value: float):
        if value < 0:
            self._handle_leftpad_left_press(True)
        elif value > 0:
            self._handle_leftpad_right_press(True)
        else:
            if self.leftpad_left:
                self._handle_leftpad_left_press(False)
            if self.leftpad_right:
                self._handle_leftpad_right_press(False)

    def _handle_leftpad_up_down(self, value: float):
        if value < 0:
            self._handle_leftpad_up_press(True)
        elif value > 0:
            self._handle_leftpad_down_press(True)
        else:
            if self.leftpad_up:
                self._handle_leftpad_up_press(False)
            if self.leftpad_down:
                self._handle_leftpad_down_press(False)


    def handle_event(self, event: evdev.InputEvent):
        if event.type == evdev.ecodes.EV_KEY:
            self._handle_key(event)
        elif event.type == evdev.ecodes.EV_ABS:
            self._handle_abs(event)

    def on_square_down(self, handler):
        self.__square_down_handlers.append(handler)

    def on_square_up(self, handler):
        self.__square_up_handlers.append(handler)

    def on_x_down(self, handler):
        self.__x_down_handlers.append(handler)

    def on_x_up(self, handler):
        self.__x_up_handlers.append(handler)

    def on_circle_down(self, handler):
        self.__circle_down_handlers.append(handler)

    def on_circle_up(self, handler):
        self.__circle_up_handlers.append(handler)

    def on_triangle_down(self, handler):
        self.__triangle_down_handlers.append(handler)

    def on_triangle_up(self, handler):
        self.__triangle_up_handlers.append(handler)

    def on_l1_down(self, handler):
        self.__l1_down_handlers.append(handler)

    def on_l1_up(self, handler):
        self.__l1_up_handlers.append(handler)

    def on_r1_down(self, handler):
        self.__r1_down_handlers.append(handler)

    def on_r1_up(self, handler):
        self.__r1_up_handlers.append(handler)

    def on_l2_down(self, handler):
        self.__l2_down_handlers.append(handler)

    def on_l2_up(self, handler):
        self.__l2_up_handlers.append(handler)

    def on_r2_down(self, handler):
        self.__r2_down_handlers.append(handler)

    def on_r2_up(self, handler):
        self.__r2_up_handlers.append(handler)

    def on_share_down(self, handler):
        self.__share_down_handlers.append(handler)

    def on_share_up(self, handler):
        self.__share_up_handlers.append(handler)

    def on_pause_down(self, handler):
        self.__pause_down_handlers.append(handler)

    def on_pause_up(self, handler):
        self.__pause_up_handlers.append(handler)

    def on_l3_down(self, handler):
        self.__l3_down_handlers.append(handler)

    def on_l3_up(self, handler):
        self.__l3_up_handlers.append(handler)

    def on_r3_down(self, handler):
        self.__r3_down_handlers.append(handler)

    def on_r3_up(self, handler):
        self.__r3_up_handlers.append(handler)

    def on_playstation_down(self, handler):
        self.__playstation_down_handlers.append(handler)

    def on_playstation_up(self, handler):
        self.__playstation_up_handlers.append(handler)

    def on_touchpad_down(self, handler):
        self.__touchpad_down_handlers.append(handler)

    def on_touchpad_up(self, handler):
        self.__touchpad_up_handlers.append(handler)

    def on_joy_l_x(self, handler):
        self.__joy_l_x_handlers.append(handler)

    def on_joy_l_y(self, handler):
        self.__joy_l_y_handlers.append(handler)

    def on_joy_r_x(self, handler):
        self.__joy_r_x_handlers.append(handler)

    def on_l2_analog(self, handler):
        self.__l2_analog_handlers.append(handler)

    def on_r2_analog(self, handler):
        self.__r2_analog_handlers.append(handler)

    def on_joy_r_y(self, handler):
        self.__joy_r_y_handlers.append(handler)

    def on_leftpad_left_down(self, handler):
        self.__leftpad_left_down_handlers.append(handler)

    def on_leftpad_left_up(self, handler):
        self.__leftpad_left_up_handlers.append(handler)

    def on_leftpad_right_down(self, handler):
        self.__leftpad_right_down_handlers.append(handler)

    def on_leftpad_right_up(self, handler):
        self.__leftpad_right_up_handlers.append(handler)

    def on_leftpad_up_down(self, handler):
        self.__leftpad_up_down_handlers.append(handler)

    def on_leftpad_up_up(self, handler):
        self.__leftpad_up_up_handlers.append(handler)

    def on_leftpad_down_down(self, handler):
        self.__leftpad_down_down_handlers.append(handler)

    def on_leftpad_down_up(self, handler):
        self.__leftpad_down_up_handlers.append(handler)

