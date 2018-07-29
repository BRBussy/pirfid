# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:54:17 2018

@author: imran
"""

import websocket
import time
from threading import Thread
try:
    import thread
except ImportError:
    import _thread as thread


class web_socket(Thread):
    def __init__(self, url):
        self.url = url
        self.ws = None
        #self.queue = queue
        Thread.__init__(self)

    def run(self):
        # Running the run_forever() in a seperate thread.
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message = self.on_message,
                                         on_error = self.on_error,
                                         on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.on_error = self.on_error
        while True:
            try:
                self.ws.run_forever()
            except:
                pass


    def send(self, data):
        # Wait till websocket is connected.
        while not self.ws.sock.connected:
            time.sleep(0.25)

        self.ws.send("Hello %s" % data)

    def stop(self):
        self.ws.keep_running = False
        self.ws.close()

    def on_message(self, ws, message):
        #self.queue.put('Received data: {0}'.format(message))
        print('Received data: {0}'.format(message))

    def on_error(self, ws, error):
        #self.queue.put('Received error: {0}'.format(error))
        print('Received error: {0}'.format(error))

    def on_close(self, ws):
        print('Closed the connection...')

    def on_open(self, ws):
        print('Opened the connection...')
