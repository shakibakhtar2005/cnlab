import socket

def run_client():
    """
    Runs the TCP client to connect to the server.
    """
    # 1. Client setup
    client_name = "shakib"
    host = '127.0.0.1'  # Server's IP address
    port = 8888        # Server's port

    # 2. Get integer from user [cite: 6]
    client_integer = 0
    while True:
        try:
            num_input = input("Enter an integer between 1 and 100: ")
            client_integer = int(num_input)
            if 1 <= client_integer <= 100:
                break
            else:
                print("Error: Number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 3. Connect to the server [cite: 7]
        print(f"Connecting to server at {host}:{port}...")
        client_socket.connect((host, port))
        print("Connection successful.")

        # 4. Send client's name and integer [cite: 8, 9]
        message = f"{client_name},{client_integer}"
        client_socket.sendall(message.encode('utf-8'))

        # 5. Wait for and receive the server's reply [cite: 10]
        data = client_socket.recv(1024).decode('utf-8')
        server_name, server_num_str = data.split(',')
        server_integer = int(server_num_str)

        # 6. Display all required information [cite: 12]
        total_sum = client_integer + server_integer
        print("\n--- Data at Client ---")
        print(f"Client's name: {client_name}")
        print(f"Server's name: {server_name}")
        print(f"Client's integer: {client_integer}")
        print(f"Server's integer: {server_integer}")
        print(f"Sum of integers: {total_sum}")
        print("----------------------\n")

    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 7. Terminate by closing the socket [cite: 18]
        client_socket.close()
        print("Client socket closed.")


if __name__ == "__main__":
    run_client()