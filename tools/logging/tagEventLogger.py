from datetime import datetime

#TODO: Make printer that prints lines to an actual log file instead of cmdline

def cmdLnPrinter(logEntry):
    println(logEntry)


def tagEventLog(printFunc = cmdLnPrinter, logData = ""):
    logEntry = "%s - %s" % (str(datetime.now()), logData)
    printFunc(logEntry)
