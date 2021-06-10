import socket
import datetime
import os

# Define socket host and port
HOSTNAME = socket. gethostname()
SERVER_HOST = socket. gethostbyname(HOSTNAME)
SERVER_PORT = 80

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)
    current_date = datetime.date.today()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World ! I am Running on : ' + str(SERVER_HOST) + ' And Today is : ' + str(current_date)
    client_connection.sendall(response.encode())
    client_connection.close()
# Close socket
server_socket.close()