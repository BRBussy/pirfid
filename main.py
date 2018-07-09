#!/usr/bin/env python
## TODO: _____Version 1 ToDos_______
## TODO: Add command line argument to tell program what host-string to use. Or Local Config file?
## TODO: Make the program into a daemon.
## TODO: All logging to then take place to a pysical log file.
##       Or multiple? One for errors/system stuff, one just for recording tag events? New one each day?
##       This is NB For when it is daemonized. you can tail the log file to get a console effect. (tail -f mylog.txt)
## TODO: Make an LED Flash and a buzzer beep when the tag event happens

## TODO:____Future Possible Features List___
#on an LCD SCREED: Welcome employee by name

import signal
import time
import sys
import time
import requests
import uuid
import json
import argparse, sys
from tools.tools import printFunctionFailure, printFunctionStart, getCmdLineArgs
from pirc522 import RFID

## Reserve Variable Names in Global Namespace
run = None
rdr = None
util = None

def initGlobals():
    printFunctionStart()
    try:
        global run
        run = True
        global rdr
        rdr = RFID()
        global util
        util = rdr.util()
        util.debug = True
    except exception as e:
        printFunctionFailure(e)
        rdr.cleanup()
    return True

def end_read(signal,frame):
    printFunctionStart()
    print("\nCtrl+C captured, Ending Program.")
    run = False
    rdr.cleanup()
    sys.exit()

def handleTagEvent(error, data):
    print("Handle tag event!")
    print(error)
    print(data)
    # if not error:
    #     print("\nDetected: " + format(data, "02x"))
    # (error, uid) = rdr.anticoll()
    # if not error:
    #     print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
    #
    #
    #
    #     id_str = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    #
    #     data = {
    #         "jsonrpc":"2.0",
    #         "id":str(uuid.uuid4()),
    #         "method":"TagEvent.Create",
    #         "params":[{
    #             "tag_event":{
    #                 "tag_id":id_str,
    #                 "tag_time": int(time.time())
    #             }
    #         }]
    #     }
    #
    #
    #     try:
    #         response = requests.post("http://192.168.8.103:9004/api", json=data, headers={"content-type":"application/json"})
    #         print(str(response.content))
    #     except requests.exceptions.RequestException as e:  #
    #         print(e)


if __name__ == "__main__":
    ## Initialise Global variables
    if not initGlobals():
        printFunctionFailure(additionalMessage = "Error in main")
        sys.exit()
    ## Set function to run on system cancel event
    signal.signal(signal.SIGINT, end_read)

    while run:
        rdr.wait_for_tag()
        #(error, data) = rdr.request()
        handleTagEvent(*rdr.request())

        time.sleep(1)
    time.sleep(1)
