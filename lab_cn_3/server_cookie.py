import socket

HOST, PORT = "127.0.0.1", 8081

def handle_client(conn):
    request = conn.recv(1024).decode("utf-8")
    print("Received request:\n", request)

    headers = request.split("\r\n")
    cookie = None
    for h in headers:
        if h.startswith("Cookie:"):
            cookie = h.split(":", 1)[1].strip()

    if cookie:
        response_body = f"<html><body><h1>Welcome back, {cookie}!</h1></body></html>"
        response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
    else:
        cookie_value = "User123"
        response_body = "<html><body><h1>Welcome, new user!</h1></body></html>"
        response_headers = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nSet-Cookie: {cookie_value}\r\n\r\n"

    response = response_headers + response_body
    conn.sendall(response.encode("utf-8"))
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Serving on port {PORT}...")
    while True:
        conn, addr = server.accept()
        handle_client(conn)
