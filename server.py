import socket
print("Server started, waiting for connections...")
server_socket = socket.socket()
server_name = '127.0.0.1'
server_port = 4444
server_socket.bind((server_name, server_port))
server_socket.listen(5)
c, address = server_socket.accept()
print("We got connection from: ", address)
try:
    while True:
        message = input("> ")
        if message == "\n" or message == "":
            print("[E] No command entered")
            continue
        message = str.encode(message)
        try:
            c.send(message)
        except:
            print("Client disconnected...\nExiting...")
            server_socket.close()
            exit()
        received = c.recv(100000)
        received = str(received, 'utf-8')
        if received == " ":
            print("[W] The reply has no content")
        else:
            print(received)
except KeyboardInterrupt:
    print("\nExiting...\nStopping the client process...")
    c.send(str.encode("closeConnection"))
    print("Closing socket...")
    server_socket.close()
    exit()