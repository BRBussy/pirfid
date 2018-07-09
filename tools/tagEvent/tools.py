from tools.general.tools import printFunctionFailure
from tools.logging.tagEventLogger import tagEventLog

def getTagUUID(rdr):
  try:
        (error, requestData) = rdr.request()
    except Exception as e:
        printFunctionFailure(e = e)
        tagEventLog("Exception during rdr request. Exception: " + str(e))
        return
    else:
        if error:
            tagEventLog("UnknownError During rdr request.")
            return
    try:
        (error, uid) = rdr.anticoll()
    except Exception as e:
        printFunctionFailure(e=e)
        tagEventLog("Exception during rdr anticoll. Exception: " + str(e))
        return
    else:
        if error:
            tagEventLog("Unknown error during rdr anticoll.")
            return
