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
from tools.tools import getCmdLineArgs

from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True


def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))



        id_str = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        data = {
            "jsonrpc":"2.0",
            "id":str(uuid.uuid4()),
            "method":"TagEvent.Create",
            "params":[{
                "tag_event":{
                    "tag_id":id_str,
                    "tag_time": int(time.time())
                }
            }]
        }


        try:
            response = requests.post("http://192.168.8.103:9004/api", json=data, headers={"content-type":"application/json"})
            print(str(response.content))
        except requests.exceptions.RequestException as e:  #
            print(e)

       # print("Setting tag")
       # util.set_tag(uid)
       # print("\nAuthorizing")
       # #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
       # util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
       # print("\nReading")
       # util.read_out(4)
       # print("\nDeauthorizing")
       # util.deauth()
    time.sleep(1)
time.sleep(1)
