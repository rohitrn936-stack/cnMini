import socket as socketModule
import json
import time   

def send_message(sock, data):
    sock.send((json.dumps(data) + "\n").encode())   

def receive_message(sock):
    buffer = ""
    while "\n" not in buffer:                      
        chunk = sock.recv(1024).decode()
        if not chunk:
            raise ConnectionError("Server disconnected")
        buffer += chunk
    message, _ = buffer.split("\n", 1)
    return json.loads(message)


import tkinter as tk
from tkinter import scrolledtext
import threading

def run_client_ui():
    def start_client():
        name = name_entry.get()
        password = pass_entry.get()

        output_box.insert(tk.END, "Connecting...\n")

        def client_logic():
            try:
                local_client = socketModule.socket(socketModule.AF_INET, socketModule.SOCK_STREAM)
                local_client.connect(('localhost',9999))

                send_message(local_client, {"type": "name", "data": name})
                output_box.insert(tk.END, receive_message(local_client)["data"] + "\n")

                send_message(local_client, {"type": "status", "data": name+" is online \n"})
                send_message(local_client, {"type": "password", "data": password})

                start_time = time.time()

                sentPassword = receive_message(local_client)["data"]

                if sentPassword == password:
                    authValue="authentication successful connection not broken"
                    send_message(local_client, {"type": "result", "data": authValue})
                else:
                    authValue="authentication unsuccessful"
                    send_message(local_client, {"type": "result", "data": authValue})

                end_time = time.time()
                latency = (end_time - start_time) * 1000

                output_box.insert(tk.END, authValue + "\n")
                output_box.insert(tk.END, f"Latency: {latency:.2f} ms\n\n")

                local_client.close()  

            except Exception as e:
                output_box.insert(tk.END, f"Error: {e}\n")

        threading.Thread(target=client_logic).start()

    window = tk.Tk()
    window.title("Client UI")

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Password").pack()
    pass_entry = tk.Entry(window, show="*")
    pass_entry.pack()

    tk.Button(window, text="Connect", command=start_client).pack()

    output_box = scrolledtext.ScrolledText(window, width=50, height=15)
    output_box.pack()

    window.mainloop()


run_client_ui()

