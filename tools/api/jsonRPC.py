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
            # Try and parse the content of the response as JSON
            bodyJsonContent =  response.json()
        except Exception as e:
            printFunctionFailure(e = e)
            raise Exception(e)

        # Try and retrieve error field from unmarshalled 'JSON Object' (a dict)
        error = bodyJsonContent.get("error", "NF")
        if error == "NF":
            # Error Field not found. Response not a valid JSON RPC Resonse.
            jsonRpcAPILog("error field not found in JSON Response")
            raise Exception("error field not found in JSON Response")
        # Error Field exists in JSON Response
        if not error == None:
            # Error field exists, but error not None. Valid JSON RPC Response with error.
            jsonRpcAPILog("json RPC Error Response: " + error)
            raise Exception("json RPC Error Response: " + error)

        result = bodyJsonContent.get("result")
        if not result:
            jsonRpcAPILog("result field not found in JSON Response")
            raise Exception("result field not found in JSON Response")

        # Some valid Result Returned
        jsonRpcAPILog("JSON RPC Request Success. Result Data: " + str(result))

        
