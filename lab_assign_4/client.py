import cv2
import socket
import numpy as np

# Client settings
IP = "0.0.0.0"
PORT = 5000
ADDR = (IP, PORT)

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)

buffer = b""

while True:
    packet, _ = sock.recvfrom(4096)

    marker = packet[0]  # first byte is marker
    buffer += packet[1:]

    if marker == 1:  # last packet of frame
        frame = cv2.imdecode(np.frombuffer(buffer, dtype=np.uint8), cv2.IMREAD_COLOR)
        if frame is not None:
            cv2.imshow("Video Stream", frame)

        buffer = b""

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

sock.close()
cv2.destroyAllWindows()