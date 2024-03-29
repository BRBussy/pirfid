# import RPi.GPIO as GPIO
# import time
# from threading import Thread
#
# class io_thread(Thread):
#     def __init__(self, pin, iterations, delay):
#         super(io_thread, self).__init__()
#         self.pin = pin
#         self.iterations = iterations
#         self.delay = delay
#         self.state = False
#
#
# 
#         self.start()
#
#     def __del__(self):
#         GPIO.cleanup()
#
#     def run(self):
#         for iter in range(0, self.iterations):
#             GPIO.output(self.pin, self.toggle())
#             time.sleep(self.delay)
#     def toggle(self):
#         self.state = not self.state
#         return self.state
#
# class timekeeper_io():
#
#     def __init__(self):
#         self.buzzer_pin = 3
#         self.connected_led_pin = 5
#
#         self.read_ok_led_pin = 11
#         self.read_fail_led_pin = 13
#         self.read_processing_led_pin = 15
#         GPIO.setup(self.buzzer_pin, GPIO.OUT)
#         GPIO.setup(self.connected_led_pin, GPIO.OUT)
#         GPIO.setup(self.read_ok_led_pin, GPIO.OUT)
#         GPIO.setup(self.read_fail_led_pin, GPIO.OUT)
#         GPIO.setup(self.read_processing_led_pin, GPIO.OUT)
#
#     def __del__(self):
#         GPIO.cleanup()
#
#     def connected_io(self, connected):
#         GPIO.output(self.connected_led_pin, connected)
#
#     def make_sound_io(self, sound):
#         if sound == 1:
#             io_thread(self.buzzer_pin, 50, 0.01)
#         else:
#             io_thread(self.buzzer_pin, 50, 0.01)
#
#     def read_ok_io(self):
#         io_thread(self.read_ok_led_pin, 5, 0.5)
#
#     def read_fail_io(self):
#         io_thread(self.read_fail_led_pin, 5, 0.5)
#
#     def read_processing_io(self):
#         io_thread(self.read_processing_led_pin, 5, 0.5)
