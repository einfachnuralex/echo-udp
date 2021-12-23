
import signal
import os
import socket
import sys

if os.environ.get('PORT'):
  server_port = int(os.environ.get('PORT'))
else:
  server_port = 31337

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'

server = ("0.0.0.0", server_port)
server_v6 = ("::/0", server_port)
sock.bind(server)
#sock.bind(server_v6)

print("Listening on :" + str(server_port))

signal.signal(signal.SIGTERM, sigterm_handler)

try:
    while True:
      payload, client_address = sock.recvfrom(1)
      print("Echoing data back to " + str(client_address))
      sent = sock.sendto(payload, client_address)
finally:
    print("Goodbye")