import socket
import random
import time

ports = [22, 80, 135, 445, 3389]

while True:
    port = random.choice(ports)

    s = socket.socket()
    s.settimeout(1)

    try:
        s.connect(("10.10.10.10", port))
        print(f"OPEN {port}")
    except:
        print(f"CLOSED {port}")

    s.close()

    time.sleep(5)