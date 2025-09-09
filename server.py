import socket

def run_server():
    """
    Runs the TCP server to handle one client connection.
    """
    # 1. Server setup [cite: 20]
    server_name = "room 109c kalam"
    server_integer = 77  # A number between 1 and 100 [cite: 26]
    host = '127.0.0.1'  # Localhost
    port = 8888        # Port > 5000 [cite: 43]

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(f"Error binding port: {e}")
        return

    # 2. Listen for incoming connections [cite: 21]
    server_socket.listen(1)
    print(f"Server '{server_name}' is listening on {host}:{port}...")

    try:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        with client_socket:
            # 3. Receive message from the client [cite: 22]
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                return
                
            client_name, client_num_str = data.split(',')
            client_integer = int(client_num_str)

            # 4. Check if the client's number is valid [cite: 35]
            if not (1 <= client_integer <= 100):
                print(f"Received number {client_integer} is out of range. Shutting down.")
                return # This will lead to finally block and close sockets

            # 5. Display received data and the sum [cite: 23, 27, 30]
            total_sum = client_integer + server_integer
            print("\n--- Data at Server ---")
            print(f"Client's name: {client_name}")
            print(f"Server's name: {server_name}")
            print(f"Client's integer: {client_integer}")
            print(f"Server's integer: {server_integer}")
            print(f"Sum of integers: {total_sum}")
            print("----------------------\n")


            # 6. Send server's name and integer back to the client [cite: 31, 33, 34]
            response = f"{server_name},{server_integer}"
            client_socket.sendall(response.encode('utf-8'))
            print("Response sent to client.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 7. Close all sockets [cite: 35, 44]
        server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    run_server()