import socket
from socket import *
import struct

multicast_addr = "224.0.0.1"
port = 5001
multicast_grp = (multicast_addr, port)

list_of_messages = ["A2", "A1", "C2", "C1", "A3", "C3"]
# One-liner that converts strings from the list to bytes
messages = [message.encode("utf-8") for message in list_of_messages]


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    ttl = struct.pack("b", 1)
    sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)
    sock.settimeout(10)

    # Send the messages
    for message in messages:
        input(f"Press Enter to send {message}")
        print(f">>> sent {message}")
        sock.sendto(message, multicast_grp)
    print("Closing socket...")
    sock.close()


if __name__ == "__main__":
    main()
