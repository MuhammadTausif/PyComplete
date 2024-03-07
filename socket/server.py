import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

port = 12345

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

print(f'Server listening on {host}:{port}...')

while True:
   # Establish a connection
   client_socket, addr = server_socket.accept()    

   print(f"Got a connection from {addr}")
   msg = 'Thank you for connecting'+ "\r\n"
   client_socket.send(msg.encode('ascii'))
   client_socket.close()
