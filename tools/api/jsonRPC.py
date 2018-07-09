import uuid, json, requests
from tools.logging.jsonRpcAPILogger import jsonRpcAPILog
from tools.general.tools import printFunctionFailure

class jsonRPC:
    def __init__(self, host, port):
        jsonRpcAPILog("creating jsonRPC Object with host:'%s' port:'%s'" % (host, port))
        self.host=host
        self.port=port

    def makeReq(self, method, paramsData):
        data = {
                "jsonrpc":"2.0",
                "id":str(uuid.uuid4()),
                "method":method,
                "params":[paramsData]
            }
        jsonRpcAPILog("Make jsonRPCAPI Request to method: ''%s'.\n\tData:\n\t%s" % (method, paramsData))
        try:
            response = requests.post("http://%s:%s/api" % (self.host, self.port), json=data, headers={"content-type":"application/json"})
        except requests.Exceptions.RequestException as e:
            printFunctionFailure(e = e)
            raise e
        try:
            bodyJsonContent =  response.json()
            print(bodyJsonContent)
        except Exception as e:
            raise Exception("Error JSON: " + str(e))
