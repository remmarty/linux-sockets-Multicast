import socket
from socket import *
import queue
import re

interface_ip = "192.168.1.8"
multicast_addr = "224.0.0.1"
port = 5001
multicast_grp = (multicast_addr, port)

# Zad. 1
# def listen(sock):
#     while True:
#         data, addr = sock.recvfrom(256)
#         received_message = data.decode("utf-8")
#         print(f"Data received: '{received_message}' from {addr}")


# Zad. 2
def value_of(message):
    value = re.split("(\d+)", message)[1]
    return int(value)


def listen(sock):
    q1, q2, q3 = [], [], []
    prev_q1_len, prev_q2_len, prev_q3_len = 0, 0, 0
    while True:
        data, addr = sock.recvfrom(256)
        received_message = data.decode("utf-8")

        if "A" in received_message:
            q1.append(received_message)
            q1.sort()
        if "B" in received_message:
            q2.append(received_message)
            q2.sort()
        if "C" in received_message: 
            q3.append(received_message)
            q3.sort()

        if len(q1) != 0:
            if len(q1) == value_of(q1[-1]) and len(q1) != prev_q1_len:
                print(q1)
                prev_q1_len = len(q1)
        if len(q2) != 0:
            if len(q2) == value_of(q2[-1]) and len(q2) != prev_q2_len:
                print(q2)
                prev_q2_len = len(q2)
        if len(q3) != 0:
            if len(q3) == value_of(q3[-1]) and len(q3) != prev_q3_len:
                print(q3)
                prev_q3_len = len(q3)


def main():
    # Create and bind the socket
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(multicast_grp)
        mreq = inet_aton(multicast_addr) + inet_aton(interface_ip)
        sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
        # Listen to the multicast group messages
        listen(sock)
    except KeyboardInterrupt:
        print("\nClosing socket...")
        sock.close()


if __name__ == "__main__":
    main()
