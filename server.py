import socket
server = socket.socket()
server.bind(("localhost", 8080))
server.listen()
print("Server is listening...")

while True:
    client, address = server.accept()

    print("someone connected!")
    print(address)

    request = client.recv(1024)

    response = """HTTP/1.1 200 ok
Content-Type: text/html

<h1>Hello World</h1>
<h2>My First Web Server</h2>
<p>I build this with python Socket</p>
"""

    client.send(response.encode())
    client.close()




