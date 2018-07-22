# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:06:21 2018

@author: imran
"""

from datetime import datetime

#TODO: Make printer that prints lines to an actual log file instead of cmdline

def cmdLnPrinter(logEntry):
    print(logEntry)


def websocketLog(logData = "", printFunc = cmdLnPrinter):
    logEntry = "%s - %s" % (str(datetime.now()), logData)
    printFunc(logEntry)
