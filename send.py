import socket
import sys

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 50001

# MULTICAST_TTL = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)


if len(sys.argv) > 1:
    with open(sys.argv[1], 'rb') as f:
        sock.sendto(f.read(), (MCAST_GRP, MCAST_PORT))
        sock.sendto(b'', (MCAST_GRP, MCAST_PORT))
        sys.exit(0)

while True:
    try:
        sock.sendto(input().encode() + b'\n', (MCAST_GRP, MCAST_PORT))
    except:
        break