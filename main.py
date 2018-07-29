#!/usr/bin/env python
## TODO: _____Version 1 ToDos_______
## TODO: Add command line argument to tell program what host-string to use. Or Local Config file?
## TODO: Make the program into a daemon.
## TODO: All logging to then take place to a pysical log file.
##       Or multiple? One for errors/system stuff, one just for recording tag events? New one each day?
##       This is NB For when it is daemonized. you can tail the log file to get a console effect. (tail -f mylog.txt)
## TODO: Make an LED Flash and a buzzer beep when the tag event happens
## TODO: Build in 2 events somewhere. One that happens at start of scan, one happens at end of successful api / on failure?
##       Need way to give feedback to person tagging of [a.]success, [b.]failure or [c.]pleaseTryAgain.
## TODO: Build tag event class. When a new tag event happens an instance of this class is initialised with data from reader.request() and reader.anticoll()
##       Class Methods for posting itself, logging everything that it does etc. Basically it can handle() itself. Arguments to it's handle() method will tell it how
##       best to handle itself?

## TODO:____Future Possible Features List___
#on an LCD SCREED: Welcome employee by name

import signal
import time
import sys
import time
import requests
import uuid
import json
import queue
import argparse, sys
from threading import Thread
from pirc522 import RFID
from tools.general.tools import printFunctionFailure, printFunctionStart, CmdLineParser
from tools.logging.tagEventLogger import tagEventLog
from tools.logging.jsonRpcAPILogger import jsonRpcAPILog
from tools.logging.websocketLogger import websocketLog
from tools.tagEvent.tools import getTagUUID
from tools.api.jsonRPC import jsonRPC
from tools.webSocket.webSocket import web_socket
#from tools.GPIO.io import timekeeper_io

## Reserve Variable Names in Global Namespace
cmdLineArgs = None


class timekeeper(Thread):

    def __init__(self, ip=None, port=None):
        self.reader = RFID()

        self.ip ="localhost" if ip == None else ip
        self.port="9004" if port == None else port
        self.ip_str = "ws://" + str(self.ip) + ":" + str(self.port)+ "/ws"

        #self.queue = queue.Queue()
        try:
            self.web_socket = web_socket(
                url = self.ip_str
                #queue = self.queue
            )
            self.web_socket.start()
        except Exception as e:
            raise Exception(e)

        try:
            self.util = self.reader.util()
            self.util.debug = True
        except Exception as e:
            if not self.reader == None:
                try:
                    self.reader.cleanup()
                except Exception as e:
                    raise Exception(e)
            raise Exception(e)

        Thread.__init__(self)
        self.start()


    def __del__(self):
        if not self.reader == None:
            try:
                self.reader.cleanup()
            except Exception as e:
                raise Exception(e)

    def run(self):
        while True:

            self.wait_for_tag_event()
            self.handle_tag_event()

        #    for item in iter(self.queue.get, None):
        #        print("queue: {0}".format(item))

            time.sleep(1) #Sleep for 1 second to debounce


    def wait_for_tag_event(self):
        self.reader.wait_for_tag()

    def handle_tag_event(self):
        try:
            #self.tk_io.read_processing_io()
            uuid = getTagUUID(self.reader)
        except Exception as e:
            tagEventLog("Exception while running getTagUUID: " + str(e))
            #self.tk_io.read_fail_io()

            # TODO: Deal with failed read
        else:
            self.send_tag_websocket(uuid)
            tagEventLog("Successful Tag Event. UUID: %s" % (uuid))


    def send_tag_websocket(self, _uuid):
        try:
            json_data = {
                "method":"TagEvent.Create",
                "paramsData": {
                    "tag_event":{
                        "tag_id":str(_uuid),
                        "tag_time": int(time.time())
                    }
                }
            }
            json_string = json.dumps(json_data)
            self.web_socket.send(json_string)
        except Exception as e:
            websocketLog("Exception while making WebSocket Request: " + str(e))
            # TODO: Deal with failed WebSocket Request
            return


def setCmdLineArgsNameSpace():
    try:
        cmdLineParser = CmdLineParser()
        cmdLineParser.addArg(cmdFlag='--goHost', help='The IP Address/host of the go Server.')
        cmdLineParser.addArg(cmdFlag='--goPort', help='The port to address the go API/Socket Server')
        global cmdLineArgs
        cmdLineArgs = cmdLineParser.parse_args()
    except Exception as e:
        printFunctionFailure(e = e)
        raise e

if __name__ == "__main__":
    setCmdLineArgsNameSpace()

    try:
        print("Waiting for tags")
        tk = timekeeper(cmdLineArgs.goHost, cmdLineArgs.goPort)
    except KeyboardInterrupt:
        print("Ctrl-c pressed ...")
        sys.exit(1)
