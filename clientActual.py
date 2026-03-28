import socket as socketModule

client=socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

client.connect(('localhost',9999))

name=input("enter the name of the client\n")
password=input("enter the password \n")

client.send(name.encode())

print(client.recv(1024).decode())

#device status
client.send(name.encode()+" is online \n".encode())

#authentication 
client.send(password.encode())
sentPassword=client.recv(1024).decode()
if sentPassword==password:
    authValue="authentication successful connection not broken"
    client.send(authValue.encode())
    print(authValue)
else:
    authValue="authenticaiton unsuccessful"
    print(authValue)
    client.send(authValue.encode())
    client.close()