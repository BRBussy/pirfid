from tools.general.tools import printFunctionFailure
from tools.logging.tagEventLogger import tagEventLog



def getTagUUID(reader):
    try:
        (error, requestData) = reader.request()
    except Exception as e:
        printFunctionFailure(e = e)
        raise Exception("Exception during reader request. Exception: " + str(e))
    else:
        if error:
            raise Exception("UnknownError During reader request.")
    try:
        (error, uid) = reader.anticoll()
    except Exception as e:
        printFunctionFailure(e=e)
        raise Exception("Exception during reader anticoll. Exception: " + str(e))
    else:
        if error:
            raise Exception("Unknown error during reader anticoll.")
    return uid
