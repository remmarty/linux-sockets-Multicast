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
def update_lists(q1, q2, q3, message):
    if "A" in message:
        q1.append(message); q1.sort()
    if "B" in message:
        q2.append(message); q2.sort()
    if "C" in message: 
        q3.append(message); q3.sort()

def value_of(message):
    value = re.split("(\d+)", message)[1]
    return int(value)
   
def print_list(list, prev_len):
    if len(list) != 0:
        if len(list) == value_of(list[-1]) and len(list) != prev_len:
            print(list)
        elif value_of(list[0]) == 1 and len(list) != prev_len:
            print(f"['{list[0]}']")

def listen(sock):
    q1, q2, q3 = [], [], []
    prev_q1_len, prev_q2_len, prev_q3_len = 0, 0, 0
    while True:
        data, addr = sock.recvfrom(256)
        received_message = data.decode("utf-8")
        update_lists(q1, q2, q3, received_message)
        print_list(q1, prev_q1_len); prev_q1_len = len(q1)
        print_list(q2, prev_q2_len); prev_q2_len = len(q2)
        print_list(q3, prev_q3_len); prev_q3_len = len(q3)

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
