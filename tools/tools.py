import argparse, sys

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
      println("Error while parsing command line arguments.\n%s %s" % (type(e), e))
      return none
