import socket as socketModule
import json

def send_message(sock, data):
    sock.send((json.dumps(data) + "\n").encode())   

def receive_message(sock):
    buffer = ""
    while "\n" not in buffer:                      
        chunk = sock.recv(1024).decode()
        if not chunk:
            raise ConnectionError("Client disconnected")
        buffer += chunk
    message, _ = buffer.split("\n", 1)
    return json.loads(message)


server = socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

server.bind(('localhost',9999))

server.listen(5)
print("waiting for connections\n")

while True:
    clientSocket,clientAddress=server.accept()

    clientName = receive_message(clientSocket)["data"]

    print("server with ip "+str(clientAddress)+" has connected with the name "+clientName+"\n")

    send_message(clientSocket, {"type": "msg", "data": "welcome to server"})

    #device status
    print(receive_message(clientSocket)["data"])

    #authentication (receive password from client)
    clientPassword = receive_message(clientSocket)["data"]

    correctPassword = "1234"   # server-side password

    if clientPassword == correctPassword:
        send_message(clientSocket, {"type": "password", "data": correctPassword})
    else:
        send_message(clientSocket, {"type": "password", "data": "wrong"})

    print(receive_message(clientSocket)["data"])

    clientSocket.close()