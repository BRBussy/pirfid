# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:54:17 2018

@author: imran
"""

import websocket
import threading
import time
try:
    import thread
except ImportError:
    import _thread as thread
    
    
class webSocket(threading.Thread):
#    def __init__(self, ip, port, on_open, on_error, on_message, on_close):
#        websocket.enableTrace(True)
#        self.ws = websocket.WebSocketApp("ws://" + str(ip) + ":" + str(port)+ "/ws",
#                              on_message = on_message,
#                              on_error = on_error,
#                              on_close = on_close)
#        self.ws.on_open = on_open
#        self.ws.run_forever()
#        self.wst = threading.Thread(target=self.ws.run_forever)
#        self.wst.daemon = True
#        self.wst.start()
#        
#    def getWebSocket(self):
#        return self.ws
    
    def __init__(self, url):
        self.url = url
        self.ws = None
        threading.Thread.__init__(self)

    def run(self):

        # Running the run_forever() in a seperate thread.
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message = self.on_message,
                                         on_error = self.on_error,
                                         on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()
    
    def send(self, data):

        # Wait till websocket is connected.
        while not self.ws.sock.connected:
            time.sleep(0.25)

        self.ws.send("Hello %s" % data)

    def stop(self):
        self.ws.keep_running = False
        self.ws.close()

    def on_message(self, ws, message):
        print('Received data...', message)

    def on_error(self, ws, error):
        print('Received error...')
        print(error)

    def on_close(self, ws):
        print('Closed the connection...')

    def on_open(self, ws):
        print('Opened the connection...')