from datetime import datetime

#TODO: Make printer that prints lines to an actual log file instead of cmdline

def cmdLnPrinter(logEntry):
    print(logEntry)


def jsonRpcAPILog(logData = "", printFunc = cmdLnPrinter):
    logEntry = "%s - %s" % (str(datetime.now()), logData)
    printFunc(logEntry)
