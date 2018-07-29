from threading import Thread
import time

class led_thread(Thread):

    def __init__(self):
        super(led_thread, self).__init__()
        
        self._keepgoing = True

    def run(self):
        while (self._keepgoing):
            time.sleep(0.5)
    def stop(self):
        self._keepgoing = False
