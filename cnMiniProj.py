import socket as socketModule
server = socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

server.bind(('localhost',9999))

server.listen(2)
print("waiting for connections\n")

while True:
    clientSocket,clientAddress=server.accept()
    clientName=clientSocket.recv(1024).decode()
    print("server with ip "+str(clientAddress)+" has connected with the name "+clientName+"\n")
    clientSocket.send("welcome to server".encode())


    #client status
    print(clientSocket.recv(1024).decode())
    print("\n")

    #authentication
    print(clientSocket.recv(1024))
    print("\n")
    
    passwordClientSend=input()
    clientSocket.send(passwordClientSend.encode())

    clientSocket.close()