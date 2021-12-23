import socket
import sys
import signal
import os
import time

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

if os.environ.get('PORT'):
  server_port = int(os.environ.get('PORT'))
else:
  server_port = 31337

if os.environ.get('HOST'):
  server_host = os.environ.get('HOST')
else:
  server_host = "127.0.0.1"


try:
    while True:
      with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
          s.connect((server_host, server_port))
          res = s.send(b'x')
          print(time.strftime("%d%m%y-%H%M%S"), "Send", res) 
          data = s.recv(1)

      print(time.strftime("%d%m%y-%H%M%S"), 'Received', repr(data))
      #time.sleep(0.5)
finally:
    print("Goodbye")