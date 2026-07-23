import socket
server = socket.socket()
server.bind(("localhost", 8080))
server.listen()
print("Server is listening...")

while True:
    client, address = server.accept()

    print("\nsomeone connected!")
    print(address)

    request = client.recv(1024).decode()

    request_line = request.splitlines()[0]
    method, path, version = request_line.split()
    
    print(method)
    print(path)
    print(version)



    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        "<h1>Hello World</h1>"
        "<h2>My First Web Server</h2>"
        "<p>I built this with Python Socket</p>"
    )



    client.send(response.encode())
    client.close()




