import RPi.GPIO as GPIO
from tools.constants import constants
from threading import Thread

class io_thread(Thread):
    def __init__(self, pin, iterations, delay):
        super(io_thread, self).__init__()
        self.pin = pin
        self.iterations = iterations
        self.delay = delay
        self.state = False
        self.start()
    def run(self):
        for iter in self.iterations:
            GPIO.output(self.pin, self.toggle())
            time.sleep(self.delay)
    def toggle(self):
        self.state = not self.state
        return self.state

class timekeeper_io():

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(buzzer_pin, GPIO.OUT)
        GPIO.setup(connected_led_pin, GPIO.OUT)
        GPIO.setup(read_ok_led_pin, GPIO.OUT)
        GPIO.setup(read_fail_led_pin, GPIO.OUT)
        GPIO.setup(read_processing_led_pin, GPIO.OUT)

    def connected_io(self, connected):
        GPIO.output(connected_led_pin, connected)

    def make_sound_io(self, sound):
        if sound == 1:
            io_thread(buzzer_pin, 50, 0.01)
        else:
            io_thread(buzzer_pin, 50, 0.01)

    def read_ok_io(self):
        io_thread(read_ok_led_pin, 5, 0.5)

    def read_fail_io(self):
        io_thread(read_fail_led_pin, 5, 0.5)

    def read_processing_io(self):
        io_thread(read_processing_led_pin, 5, 0.5)
