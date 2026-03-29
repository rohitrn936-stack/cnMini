import socket as socketModule
import json

def send_message(sock, data):
    sock.send(json.dumps(data).encode())

def receive_message(sock):
    return json.loads(sock.recv(1024).decode())


server = socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

server.bind(('localhost',9999))

server.listen(2)
print("waiting for connections\n")

while True:
    clientSocket,clientAddress=server.accept()

    clientName = receive_message(clientSocket)["data"]

    print("server with ip "+str(clientAddress)+" has connected with the name "+clientName+"\n")

    send_message(clientSocket, {"type": "msg", "data": "welcome to server"})

    #device status
    print(receive_message(clientSocket)["data"])

    #authentication
    print(receive_message(clientSocket)["data"])

    sendingPassword=input("enter the "+clientName+"'s password")

    send_message(clientSocket, {"type": "password", "data": sendingPassword})

    print(receive_message(clientSocket)["data"])

    clientSocket.close()