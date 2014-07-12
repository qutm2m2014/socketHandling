import SocketServer
import json

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
		while True:
			# send json data back to client
			self.request.sendall(json.dumps("""array of temp data and time"""))

if __name__ == "__main__":
    HOST, PORT = "localhost", 2222

    # Create the server, binding to localhost on port 2222
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
