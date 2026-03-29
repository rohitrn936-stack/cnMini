import socket as socketModule
import json

def send_message(sock, data):
    sock.send(json.dumps(data).encode())

def receive_message(sock):
    return json.loads(sock.recv(1024).decode())


client=socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

client.connect(('localhost',9999))

name=input("enter the name of the client\n")
password=input("enter the password \n")

send_message(client, {"type": "name", "data": name})

print(receive_message(client)["data"])

#device status
send_message(client, {"type": "status", "data": name+" is online \n"})

#authentication 
send_message(client, {"type": "password", "data": password})

sentPassword = receive_message(client)["data"]

if sentPassword == password:
    authValue="authentication successful connection not broken"
    send_message(client, {"type": "result", "data": authValue})
    print(authValue)
else:
    authValue="authenticaiton unsuccessful"
    print(authValue)
    send_message(client, {"type": "result", "data": authValue})
    client.close()