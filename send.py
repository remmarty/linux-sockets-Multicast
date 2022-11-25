import socket
import struct

multicast_addr = "224.3.29.71"
port = 10001
multicast_grp = (multicast_addr, port)

#list_of_messages = ["ala", "ma", "kota"]
list_of_messages = ["A2", "A1", "A3"]
# One-liner that converts strings from the list to bytes
messages = [message.encode("utf-8") for message in list_of_messages]


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ttl = struct.pack("b", 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.settimeout(10)

    # Send the messages
    for message in messages:
        sock.sendto(message, multicast_grp)
    print("Closing socket...")
    sock.close()


if __name__ == "__main__":
    main()
