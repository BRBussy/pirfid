# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:35:30 2018

@author: imran
"""

from tools.webSocket.webSocket import webSocket

def on_msg(ws, message):
    print(message)

def on_err(ws, error):
    print(error)

def on_clse(ws):
    print("### closed ###")

def on_opn(ws):
    ws.send("Hello")


webSocketTool = webSocket(
    ip="localhost",
    port="9004",
    on_message=on_msg,
    on_error=on_err,
    on_close=on_clse,
    on_open=on_opn
)
            