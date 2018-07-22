# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:54:17 2018

@author: imran
"""

import websocket
try:
    import thread
except ImportError:
    import _thread as thread
    
    
class webSocket():
    def __init__(self, ip, port, on_open, on_error, on_message, on_close):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://" + str(ip) + ":" + str(port)+ "/ws",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        self.ws.on_open = on_open
        self.ws.run_forever()
    
    def getWebSocket(self):
        return self.ws