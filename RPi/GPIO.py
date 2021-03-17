IN = 1
OUT = 0
LOW = 0
HIGH = 1
BCM = 11
BOARD = 10
PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

def setwarnings(b):
  return b

def setmode(mode):
  return mode

def output(pin, state):
  return [pin, state]

def input(pin):
  return pin

def cleanup():
  return

def setup(pin, type, initial = 0):
  return

