import socket
import queue
from queue import PriorityQueue


multicast_addr = "224.3.29.71"
port = 10001
multicast_grp = (multicast_addr, port)

# Zad. 1
# def listen(sock):
#     while True:
#         data, addr = sock.recvfrom(256)
#         received_message = data.decode("utf-8")
#         print(f"Data received: '{received_message}' from {addr}")

# Zad. 2
q1 = queue.PriorityQueue()
q2 = queue.PriorityQueue()
q3 = queue.PriorityQueue()
def listen(sock):
    while True:
        data, addr = sock.recvfrom(256)
        received_message = data.decode("utf-8")

        if "A1" or "A2" or "A3" in received_message:
            q1.put(received_message)
        elif "B1" or "B2" or "B3" in received_message:
            q1.put(received_message)
        elif "C1" or "C2" or "C3" in received_message:
            q1.put(received_message)
        
        if q1.qsize() == 3:
            while not q1.empty():
                received_message = q1.get()
                print(f"Data received: '{received_message}' from {addr}")
        if q2.qsize() == 3:
            while not q2.empty():
                received_message = q2.get()
                print(f"Data received: '{received_message}' from {addr}")
        if q3.qsize() == 3:
            while not q3.empty():
                received_message = q3.get()
                print(f"Data received: '{received_message}' from {addr}")

def main():
    # Create and bind the socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(multicast_grp)
        group = socket.inet_aton(multicast_addr)
        mreq = group + socket.inet_aton("192.168.1.8")
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        # Listen to the multicast group messages
        listen(sock)
    except KeyboardInterrupt:
        print("\nClosing socket...")
        sock.close()


if __name__ == "__main__":
    main()
