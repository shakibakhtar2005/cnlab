import cv2
import socket
import math
import time

# Server settings
SERVER_IP = "127.0.0.1"   # Change to your server IP
PORT = 5000
ADDR = (SERVER_IP, PORT)
CHUNK_SIZE = 4096

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open video file
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for efficiency
    frame = cv2.resize(frame, (400, 300))

    # Encode frame to JPEG
    _, buffer = cv2.imencode(".jpg", frame)
    data = buffer.tobytes()

    # Split into chunks
    total_packets = math.ceil(len(data) / CHUNK_SIZE)
    for i in range(total_packets):
        start = i * CHUNK_SIZE
        end = start + CHUNK_SIZE
        chunk = data[start:end]

        # Marker: 1 for last packet, 0 otherwise
        marker = 1 if i == total_packets - 1 else 0
        sock.sendto(marker.to_bytes(1, "big") + chunk, ADDR)

    time.sleep(1 / 24)  # maintain ~24 FPS

cap.release()
sock.close()