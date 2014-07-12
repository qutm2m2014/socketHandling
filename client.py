import socket
import json
import sys

HOST, PORT = """ Address of host that Socket reside on """, 2222
# create an AF_INET, STREAM socket (TCP)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception, e:
    print "There was a problem to create socket - ", e
	sys.exit()

# connect to socket
try:
	s.connect((HOST, PORT))
except:
	print "Could not connect to socket"

# receive the data from server
data = json.loads(s.recv(1024))
print data
s.close()
