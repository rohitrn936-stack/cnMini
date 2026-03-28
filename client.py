import socket as socketModule

client=socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)

client.connect(('localhost',9999))

name="panda"
client.send(name.encode())

#device status reporting
client.send(f"client {name} online".encode())

#authentication
client.send("enter the password for the device "+name+"\n".encode())
password=input("enter password for this system")
sentPasswrod=client.recv(1024).decode()
if password==sentPasswrod:
    print("authentication successful connection not lost")
else:
    print("authentication unsucessful connection lost")
    client.close()

print(client.recv(1024).decode())