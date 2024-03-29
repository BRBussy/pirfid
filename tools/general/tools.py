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
    stdPrefixChar = ''
    stdPostfixChar = '...'
    stdNoOfPostfixChars = 1
    stdNoOfPrefixChars = 1
    try:
        callerFunction =  inspect.stack()[1][3]
    except Exception as pfe:
        printFunction('PrintFunctionStart Function Unable to get Caller Functions Name!\nFailed With Error: %s  - %s' % (pfe, type(pfe)))
    else:
        printFunction('%srunning %s%s' % (stdPrefixChar*stdNoOfPrefixChars, callerFunction, stdPostfixChar*stdNoOfPostfixChars))
        if additionalMessage:
            printFunction('%s' % (additionalMessage))

class CmdLineParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def addArg(self, cmdFlag, help="no help text defined"):
        try:
            help = help if help[0] == "-" else "-" + help
            self.parser.add_argument(cmdFlag, help)
        except Exception as e:
            printFunctionFailure(e=e)
            raise e

    def parse_args(self):
        try:
            args = self.parser.parse_args()
        except Exception as e:
            printFunctionFailure(e=e)
            raise e
        else:
            return args
