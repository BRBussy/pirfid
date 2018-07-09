import argparse, inspect, sys

def printFunctionFailure(*others, printFunction = print, e = 'Default Print Function Failure Message', additionalMessage = None):
    stdPrefixChar = '_'
    stdPostfixChar = '_'
    stdNoOfPostfixChars = 4
    stdNoOfPrefixChars = 4
    try:
        callerFunction =  inspect.stack()[1][3]
    except Exception as pfe:
        printFunction('printFailure Function Unable to get Caller Functions Name!\nFailed With Error: %s  - %s' % (pfe, type(pfe)))
    else:
        printFunction('\n%s Function: %s Failed %s' % (stdPrefixChar*stdNoOfPrefixChars, callerFunction, stdPostfixChar*stdNoOfPostfixChars))
        printFunction('Error Was:\n%s\n' % (e)) if type(e) == type('') else printFunction('Error Was:\n%s - Type:%s' % (e, type(e)))
        if additionalMessage:
            printFunction('Additional Error Message:\n%s' % (additionalMessage))

def printFunctionStart(*others, printFunction = print, e = 'Default Print Function Start Message', additionalMessage = None):
    stdPrefixChar = '_'
    stdPostfixChar = '_'
    stdNoOfPostfixChars = 4
    stdNoOfPrefixChars = 4
    try:
        callerFunction =  inspect.stack()[1][3]
    except Exception as pfe:
        printFunction('PrintFunctionStart Function Unable to get Caller Functions Name!\nFailed With Error: %s  - %s' % (pfe, type(pfe)))
    else:
        printFunction('\n%s Running Function: %s %s' % (stdPrefixChar*stdNoOfPrefixChars, callerFunction, stdPostfixChar*stdNoOfPostfixChars))
        if additionalMessage:
            printFunction('\n%s' % (additionalMessage))

def getCmdLineArgs():
  parser=argparse.ArgumentParser()
  # Add arguments
  parser.add_argument('--goHost', help='The IP Address of the Server go Server.')
  parser.add_argument('--goAPIPort', help='The port to address the go API Server')
  # Parse arguments
  try:
      args = parser.parse_args()
      return args
  except exception as e:
      printFunctionFailure(e)
      return none
