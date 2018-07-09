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
import argparse, sys
from pirc522 import RFID
from tools.general.tools import printFunctionFailure, printFunctionStart, CmdLineParser
from tools.logging.tagEventLogger import tagEventLog
from tools.logging.jsonRpcAPILogger import jsonRpcAPILog
from tools.tagEvent.tools import getTagUUID
from tools.api.jsonRPC import jsonRPC

## Reserve Variable Names in Global Namespace
cmdLineArgs = None

run = None
reader = None
util = None
jsonRPCTool = None

def setCmdLineArgsNameSpace():
        try:
            cmdLineParser = CmdLineParser()
            cmdLineParser.addArg(cmdFlag='--goHost', help='The IP Address/host of the go Server.')
            cmdLineParser.addArg(cmdFlag='--goAPIPort', help='The port to address the go API Server')
            global cmdLineArgs
            cmdLineArgs = cmdLineParser.parse_args()
        except Exception as e:
            printFunctionFailure(e = e)
            raise es

def initGlobals():
    printFunctionStart()
    try:
        # Get and set command line arguments name space
        setCmdLineArgsNameSpace()
        # Create jsonRPC Object to perform requests
        global jsonRPCTool
        jsonRPCTool = jsonRPC(
            host="localhost" if cmdLineArgs.goHost == None else cmdLineArgs.goHost,
            port="9004" if cmdLineArgs.goAPIPort == None else cmdLineArgs.goAPIPort,
        )

        # Set others manually
        global run
        run = True
        global reader
        reader = RFID()
        global util
        util = reader.util()
        util.debug = True
    except Exception as e:
        printFunctionFailure(e=e)
        if not reader == None:
            try:
                reader.cleanup()
            except Exception as e:
                printFunctionFailure(e=e)
        return False
    return True

def end_read(signal,frame):
    printFunctionStart()
    print("Ctrl+C captured, Ending Program.")
    run = False
    reader.cleanup()
    sys.exit()

def handleTagEvent():
    printFunctionStart()
    try:
        uiid = getTagUUID(reader)
    except Exception as e:
        tagEventLog("Exception while running getTagUUID: " + str(e))
        # TODO: Deal with failed read
        return
    else:
        tagEventLog("Successful Tag Event. UUID: %s" % (uiid))

    try:
        jsonRPCTool.makeReq(
                method="TagEvent.Create",
                paramsData= {
                    "tag_event":{
                        "tag_id":str(uiid),
                        "tag_time": int(time.time())
                    }
                },
        )
    except Exception as e:
        jsonRpcAPILog("Exception while making JsonRPC Request: " + str(e))
        # TODO: Deal with failed API Request
        return

    #TODO: Deal with successful API Request


if __name__ == "__main__":
    ## Initialise Global variables
    if not initGlobals():
        printFunctionFailure(e="Error Initialising Globals. Main is exiting.")
        sys.exit()
    ## Set function to run on system cancel event
    signal.signal(signal.SIGINT, end_read)

    while run:
        reader.wait_for_tag()
        handleTagEvent()
        time.sleep(1) #Sleep for 1 second to debounce
