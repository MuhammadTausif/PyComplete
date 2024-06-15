import socket

# Server script
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local host name
    host = socket.gethostname()
    
    # Set a port for the server
    port = 12345
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Start listening for connections
    server_socket.listen(5)
    
    print("Server is listening for incoming connections...")
    
    # Keep the server running
    while True:
        # Accept an incoming connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        
        # Send a thank you message to the client
        client_socket.send('Thank you for connecting'.encode('utf-8'))
        
        # Close the client connection
        client_socket.close()

# Run the server function
if __name__ == '__main__':
    start_server()
