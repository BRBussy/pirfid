import uuid, json, requests
from tools.general.tools import printFunctionFailure

class jsonRPC:
    def __init__(self, host, port):
        print("creating jsonRPC Object with host:'%s' port:'%s'" % (host, port))
        self.host=host
        self.port=port

    def makeReq(self, method, paramsData):
        data = {
                "jsonrpc":"2.0",
                "id":str(uuid.uuid4()),
                "method":method,
                "params":[paramsData]
            }
        print("Make request with data:")
        print(data)
        # try:
        #     response = requests.post("http://%s:%s/api" % (self.host, self.port), json=data, headers={"content-type":"application/json"})
        #     print(str(response.content))
        # except requests.Exceptions.RequestException as e:
        #     printFunctionFailure(e = e)
        #     raise e
