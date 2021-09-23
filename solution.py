# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("localhost", port))
    # Fill in start
    serverSocket.listen(1)  # server listens for incoming TCP requests
    #print("created server socket")
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        #print("Ready to serve...")
        # returns the client socket and address
        connectionSocket, addr = serverSocket.accept() # Fill in start     #Fill in end
        #print("accepted incoming connection")

        try:

            try:
                message = connectionSocket.recv(1024).decode() # Fill in start    #Fill in end
                #print("received connection")
                filename = message.split()[1]
                f = open(filename[1:])
                #print("opened file")
                outputdata = f.read()  # Fill in start     #Fill in end
                #print("read data from client")

                # Send one HTTP header line into socket.
                # Fill in start
                headerLine = "\n HTTP/1.1 200 OK \n\n"
                headerInBytes = str.encode(headerLine)
                connectionSocket.send(headerInBytes)
                #print("sent HTTP 200 ok message")
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                #print("except IOError")
                response = "\n HTTP/1.1 404 Not Found \n\n"
                responseInBytes = str.encode(response)
                connectionSocket.send(responseInBytes)
                # Fill in end

                # Close client socket
                # Fill in start
                connectionSocket.close()
                # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            #print("except error 2")
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
